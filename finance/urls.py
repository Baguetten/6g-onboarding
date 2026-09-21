from django.urls import include, path
from finance import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('categories/', views.CategoryList.as_view()),  # Category list and create
]

urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
]