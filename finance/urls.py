from django.urls import include, path
from finance import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('categories/', views.CategoryListCreateView.as_view()),  
    path('expenses/', views.ExpenseListCreateView.as_view()),  
    path('expenses/<int:pk>/', views.ExpenseDetailView.as_view()),  
    path('incomes/', views.IncomeListCreateView.as_view()),  
]

urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
]