import random
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
import requests
from .models import *
from django.template import loader

def get_posts_data():
    random_number = random.randint(1, 100)
    urls = "https://jsonplaceholder.typicode.com/posts/"+str(random_number)
    api_request = requests.get(urls)
    try:
        api_request.raise_for_status()
        return api_request.json()
    except:
        return None
        
def extract_and_save_data(request):
    post_data = get_posts_data()
    if post_data is not None:
        data = post_data
        post_obj = Posts.objects.create(userId = data["userId"], title = data["title"], body = data["body"])
        post_obj.save()
        return HttpResponseRedirect(reverse('success'))
    
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def success(request):
    template = loader.get_template('success.html')
    posts = Posts.objects.all()
    context = {
        'posts':posts
    }
    return HttpResponse(template.render(context,request))



# Create your views here.
