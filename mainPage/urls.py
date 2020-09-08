from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('math/', views.math, name = 'mathPage' ),
    path('authenticate/', views.auth_user, name ='authenticate'),
    path('math/scoreup/', views.scoreup, name = "scoreup"),
    path('logout/', auth_views.LogoutView.as_view(template_name='store/logout.html'), name='logout'),
]