from django.urls import path

from . import views
urlpatterns = [
    path('register',views.register_view,name='register_view'),
    path('saralreg',views.view_registrations,name='registees_view'),
]   
