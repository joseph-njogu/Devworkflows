from django.urls import path
from joseph  import views

urlpatterns = [
    path('joseph/', views.joseph_list),
    path('joseph/<int:pk>/', views.joseph_detail),
]