from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('<int:bug_id>/', views.bug, name='bug'),
    path('bugs', views.bug_list, name='bug_list'),
]
