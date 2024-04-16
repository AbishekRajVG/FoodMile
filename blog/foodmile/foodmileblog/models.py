from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse
from ckeditor.fields import RichTextField

# using google GenAI to generate summary of each post
import google.generativeai as genai
import google.ai.generativelanguage as glm

# using beautiful soup to extract just text from blog post
from bs4 import BeautifulSoup

genai.configure(api_key="AIzaSyCNGhksGyUfIxw_SH7oAp3WDTV9FFvmEx8") ## will change to dynamic 

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    
    def save(self, *args, **kwargs):
        # Convert the category name to lowercase before saving
        self.name = self.name.lower()
        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    last_updated = models.DateTimeField(default=now, blank=True)
    last_updated_short = models.DateField(default=now, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if user is deleted, we also "cascade" delete all posts of that user, default 1 is admin
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=255, default="miscellaneous")
    likes = models.ManyToManyField(User, related_name='blog_posts')
    summary = models.CharField(max_length=255, default="Summary not available.") # down the line we can use AI to summarise post content

    # Additional fields
    author_full_name = models.CharField(max_length=100)
    # author_profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True) #install pillow try later

    # tostring getter
    def __str__(self):
        return self.title + " | " + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])
    
    def get_total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        extracted_blog_text = BeautifulSoup(self.body).get_text()
        genai_model = genai.GenerativeModel("gemini-pro")
        messages = [
            {
                "role": "user",
                "parts": ["Give me a very short two-three line summary of this blog post", 
                            extracted_blog_text]
            }
        ]
        response = genai_model.generate_content(messages)
        self.summary = response.text
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    user_profile = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/profile_pictures/")
    personal_website_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user_profile)
    
    def get_absolute_url(self):
        return reverse('home')

    # def get_absolute_url(self):
    #     return reverse('show-profile-page', args=[str(self.user_profile.id)])

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "" + str(self.post.title) + '-' + str(self.name)