from django.urls import path
from . import views

app_name = 'play_picture'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('aboutme/', views.AboutMeView.as_view(), name='me'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('personal/<int:pk>/', views.PersonalView.as_view(), name='personal'),
    path('login/validate/', views.validate, name='validate'),
    path('login/register/', views.register, name='register'),
    path('contact/commit_s/', views.commit_s, name='commit suggestion'),
    path('commit_t/', views.commit_t, name='commit new task'),
    path('personal/edit/', views.edit, name='edit'),
    path('personal/get_time/', views.get_time, name='time'),
]
