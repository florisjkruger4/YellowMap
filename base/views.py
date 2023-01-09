from multiprocessing import context
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Post
from .forms import PostForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def default_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'default.html', 
                  { 'mapbox_access_token': mapbox_access_token })

@csrf_exempt
def homePage(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    pst = Post.objects.all()

    context = {'form': form, 'pst': pst,} 
    return render(request, 'html/home.html', context)

def postPage(request):
    pst = Post.objects.all()

    context = {'pst': pst}
    return render(request, 'html/postPage.html', context)

