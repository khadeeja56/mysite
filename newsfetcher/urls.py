from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('bbc/', views.go_to_bbc, name='bbc'),   # yahan add karna hai ✅
]
