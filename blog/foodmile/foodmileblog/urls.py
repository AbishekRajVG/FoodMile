from .views import (HomeView, ArticleDetailView, NewPostView, 
                    UpdatePostView, DeletePostView, NewCategoryView,
                    CategoryView, LikeView, ChangePasswordView, AddCommentView)
from django.urls import path

# since we're using class based view, we explicitly mention it as_views
# pk is primary key or django auto assigned of id for each blog entry

urlpatterns = [
    path('', HomeView.as_view(), name="home"), 
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('article/new', NewPostView.as_view(), name="new-post"),
    path('article/update/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name="delete-post"),
    path('category/new', NewCategoryView.as_view(), name="new-category"),
    path('category/<str:ctg>/', CategoryView, name="category"),
    path('like/<int:pk>/', LikeView, name="like-post"),
    path('<int:pk>/password/', ChangePasswordView.as_view()), 
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'), 
    # path('add-comment/', AddCommentView.as_view(), name='add-comment'),
]