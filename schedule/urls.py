from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]