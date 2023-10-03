from django.urls import path
from .views import *
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('blog/',BlogView.as_view(),name='blog_single'),
    path('signup/', SignUpView.as_view(), name='signup'),
    ]