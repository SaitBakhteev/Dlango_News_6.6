from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, CommListView


urlpatterns = [
        path('', PostsList.as_view()),
        path('<int:pk>',PostDetail.as_view()),
              ]