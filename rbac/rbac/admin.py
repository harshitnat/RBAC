from django.contrib import admin
from .models import Role, Permission, UserRole, AuditLog  # Import AuditLog

admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(UserRole)
admin.site.register(AuditLog)  # Register the AuditLog model
