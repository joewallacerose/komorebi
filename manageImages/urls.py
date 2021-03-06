from django.urls import path, include
from . import views

app_name = "manageImages"

urlpatterns = [
    path('closeup/<ID>/', views.closeup, name='closeup'),
    path('addimage/', views.addImage.as_view(), name='addimage'),
    path('like_picture/', views.LikePictureView.as_view(), name='like_picture'),
    path('dislike_picture/', views.DislikePictureView.as_view(), name='dislike_picture'),
    path('deletepicture/<imageID>', views.imagedelete, name='picturedelete'),
]