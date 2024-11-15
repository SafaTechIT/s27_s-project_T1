from django.urls import path
from . import views



urlpatterns=[
    path('user/', views.user.as_view()),
    path('allposts/',views.allposts.as_view()),
    path('post',views.post.as_view()),
    path('comment',views.comment.as_view()),
    path('reply',views.reply.as_view()),
]