from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('employee',views.employee,name='employee'),
    path('add_user',views.add_user,name='add_user'),
    path('employee_profile',views.employee_profile,name='employee_profile'),
    path('edit_employee',views.edit_employee,name='edit_employee'),
    path('works',views.works,name='works'),
    path('works_add',views.works_add,name='works_add'),
    path('works_views',views.works_views,name='works_views'),
    path('send_message',views.send_message,name='send_message'),
]