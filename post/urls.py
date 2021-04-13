from django.urls import path
from .views import TimeLineView, create_post_view

urlpatterns = [
    path('', TimeLineView.as_view(), name='index'),
    path('create/', create_post_view, name='post_status_update')
]