from django.urls import path

from . import views
urlpatterns = [
    path('showreg',views.show_reg_view,name='show_regs'),
]   
