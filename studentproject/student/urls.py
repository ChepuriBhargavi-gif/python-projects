from django.urls import path
from . import views

urlpatterns = [

    path('add_student/', views.add_student, name='add_student'),

    path('add_marks/', views.add_marks, name='add_marks'),

    path('view_student/', views.view_students, name='view_students'),

    path('edit_details/<int:id>/', views.edit_student, name='edit_student'),

    path('update_marks/<int:id>/', views.update_marks, name='update_marks'),

]