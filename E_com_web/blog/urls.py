from django.urls import path
from.import views

urlpatterns = [
    path('', views.Blog_index, name="Blog's Home")
]
