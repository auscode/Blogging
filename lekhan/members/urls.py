
from django.urls import path
from .views import *
from . import views
# from django.contr>ib.auth import views as auth_views

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('user.id/password/', PassowrdsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/',views.password_success,name ='password_success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page')
]
