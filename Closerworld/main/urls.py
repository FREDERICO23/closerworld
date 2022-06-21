from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='home'),
    path('register/',views.register, name="register"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path('about/', views.about, name='about'),
    path('site/', views.site, name='site'),
    path('manage/', views.manage, name='manage'),
    path('tele/', views.tele, name='tele'),
    path('work/', views.work, name='work'),
    path('growth/', views.growth, name='growth'),
    path('skills/', views.skills, name='skills'),
]
