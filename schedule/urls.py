from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.calendar_view, name='calendar_view'),
    path('calendar_view', views.calendar_view, name='calendar_view'),
    path('weekly_calendar', views.weekly_calendar_view, name='weekly_calendar'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)