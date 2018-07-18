from django.urls import path
from . import views



urlpatterns = [
    path('', views.employee_list , name='employee_list'),
    path('siblings/<int:id>/', views.siblings_list , name='siblings_list'),
    path('salarys/<int:id>/', views.salarys_list , name='salarys_list'),
    path('<int:id>/delete', views.employee_delete , name='employee_delete'),
    path('siblings/<int:id>/delete', views.sibling_delete , name='sibling_delete'),
    path('salarys/<int:id>/delete', views.salary_delete , name='salary_delete'),
    path('<int:id>/edit', views.employee_edit , name='employee_edit'),
    path('siblings/<int:id>/edit', views.sibling_edit , name='sibling_edit'),
    path('salarys/<int:id>/edit', views.salary_edit , name='salary_edit'),
    path('positions/', views.positions_list , name='positions_list'),
    path('<int:id>/position/edit', views.position_edit , name='position_edit'),
    path('<int:id>/position/delete', views.position_delete , name='position_delete'),
]

