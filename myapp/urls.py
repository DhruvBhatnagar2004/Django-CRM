from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name=''),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('create', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('onerecord/<int:pk>', views.onerecord, name="onerecord"),
    path('delete/<int:pk>', views.delete, name="delete"),
]