from django.shortcuts import render
from django.views.generic import TemplateView




class IndexView(TemplateView):
	template_name = 'index.html'



class BlogView(TemplateView):
	template_name = 'blog_single.html'

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('signup')


