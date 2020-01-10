from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('math/', views.math, name = 'mathPage' ),
    path('authenticate/<str:username>/', views.auth_user, name ='authenticate'),
    path('math/scoreup/', views.scoreup, name = "scoreup"),
]