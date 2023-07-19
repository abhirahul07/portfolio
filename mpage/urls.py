from django.urls import path
from mpage import views

urlpatterns=[
  path('',views.index,name="index"),
]
