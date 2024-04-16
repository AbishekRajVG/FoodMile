from typing import Any, Dict
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (ListView, DetailView, CreateView, 
                                  UpdateView, DeleteView)
from .models import Post, Category, UserProfile, Comment
from .forms import NewPostForm, UpdatePostForm, UpdateProfilePassword, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect, JsonResponse

from django.contrib.auth.views import PasswordChangeView


class BaseContextMixin:
    def get_context_data(self, *args, **kwargs) -> Dict[str, Any]:
        ctg_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context["ctg_menu"] = ctg_menu
        # if 'pk' in self.kwargs.keys():
        #     post_info = get_object_or_404(Post, id=self.kwargs['pk'])
        #     total_likes = post_info.get_total_likes()
        #     context["total_likes"] = total_likes
        return context

class HomeView(BaseContextMixin, ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-last_updated']          # ordering by last updated id

class ArticleDetailView(BaseContextMixin, DetailView) :
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs) -> Dict[str, Any]:
        ctg_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context["ctg_menu"] = ctg_menu
        post_info = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post_info.get_total_likes()

        liked = False
        if post_info.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class NewPostView(BaseContextMixin, CreateView):
    model = Post
    template_name = 'new_post.html'
    form_class = NewPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

class UpdatePostView(BaseContextMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = UpdatePostForm

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user and request.user.id != 1:
            raise Http404("You are not allowed to edit this post.")
        return super().dispatch(request, *args, **kwargs)

class DeletePostView(BaseContextMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')     # django method to set succeess url

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user and request.user.id != 1:
            raise Http404("You are not allowed to delete this post.")
        return super().dispatch(request, *args, **kwargs)


class NewCategoryView(BaseContextMixin, CreateView):
    model = Category
    template_name = 'new_category.html'
    fields = '__all__'


class ChangePasswordView(PasswordChangeView):
    form_class = UpdateProfilePassword
    template_name = 'change_password.html'
    success_url = reverse_lazy('home')


def CategoryView(request, ctg):
    posts_of_category = Post.objects.filter(category=ctg.replace('-', ' '))
    return render(request, 'categories.html', {'ctg':ctg.title().replace('-', ' '), 'posts_of_category':posts_of_category})

# save like to db
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post-id')) # get post id from button
    liked = False
    if post.likes.filter(id=request.user.id).exists(): # clicking it two times is unlike
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user) # make sure we save the user that likes
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = CommentForm
    ordering = ['-date_added']

    def get_success_url(self) -> str:
        return reverse('article-detail', args=[str(self.kwargs['pk'])])

    def form_valid(self, form):
        form.instance.name = self.request.user.first_name + " " + self.request.user.last_name
        form.instance.post_id= str(self.kwargs['pk'])
        return super().form_valid(form)
