# rbac/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.get_roles, name='get_roles'),
    path('permissions/', views.get_permissions, name='get_permissions'),
    path('assign-role/<int:pk>/', views.assign_role, name='assign_role'),
    path('audit-logs/', views.get_audit_logs, name='get_audit_logs'),  # New endpoint for logs
]
