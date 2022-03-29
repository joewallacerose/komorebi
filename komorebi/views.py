import datetime
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from manageImages.forms import ImageForm
from manageImages.models import Picture


def about(request):
    return render(request, 'about.html')

def index(request):
    return redirect("/home/")

def home(request):
    context_dict = {}

    if request.user.is_authenticated:
        current_user = request.user
        pictures = Picture.objects.filter(uploaded_by != current_user).annotate(num_likes=Count('likes')).order_by('-num_likes')[:9]
    else:
        pictures = Picture.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:9]

    for image in pictures:
        print(image)

    context_dict["pictures"] = pictures
    return render(request, "home.html", context_dict)

def addimage(request):
    form = ImageForm(request.POST, request.FILES)
    print(form.is_bound)

    if request.method == "POST":
        if form.is_valid():
            form.time = datetime.datetime.now()
            picture = form.save(commit=False)
            print(picture)
            picture.image.upload_to = "/manageImages/" + str(request.user.id) + "/" + str(picture.ID)
            print(picture.image.upload_to)
            picture.save()
            return redirect("/closeup/")
        elif request.POST:
            print("ERROR IN FORM")
            print(form.errors)

    context = {
        'form': form
    }

    return render(request, 'manageImages/addImage.html', context)
