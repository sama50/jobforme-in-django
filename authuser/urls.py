from django.urls import path
from authuser import views
urlpatterns = [
     path('login/',views.login_user,name='login'),
     path('candidte-register/',views.candidateregister,name='register'),
     path('register/',views.register,name='register-user'),
     path('hr-register/',views.hrregister,name='register-hr'),
     path('logout/',views.logoutUser,name='logout')
]
