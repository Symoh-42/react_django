from django.urls import path
from . import views


urlpatterns = [
    path('images/', views.ApplesCreate.as_view(), name="apples-create"),
    path('images/<int:pk>/', views.ApplesRetrieveUpdateDelete.as_view(), name="update"),
]
