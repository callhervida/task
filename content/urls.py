from django.urls import path

from .views import ContentList, Rating


urlpatterns = [
    path('list', ContentList.as_view()),
    path('rating', Rating.as_view())
]