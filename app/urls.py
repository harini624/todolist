from django.urls import path
from .import views

urlpatterns=[
    path('',views.todo,name='todo'),
    path('update/<int:id>',views.Edit,name='Edit'),
    path('delete/<int:id>',views.Delete,name='Delete'),
]