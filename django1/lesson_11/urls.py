from django.urls import path
from lesson_11.views import lesson1, lesson11


urlpatterns = [
    path('', lesson1),
    path('lesson_1_1/', lesson11)
]