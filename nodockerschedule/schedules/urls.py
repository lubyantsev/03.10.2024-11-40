from django.urls import path
from .views import create_schedule, home_view, schedule_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create_schedule/', create_schedule, name='create_schedule'),
    path('schedule/<int:schedule_id>/', schedule_detail_view, name='schedule_detail'),
]