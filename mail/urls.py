from django.urls import path
from . import views

app_name = 'mail'
urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('view',views.view,name='view'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('mail',views.mail,name='mail')
]
