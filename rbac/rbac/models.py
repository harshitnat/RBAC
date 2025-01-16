from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        # Predefine roles when first creating the table
        if not self.pk:
            if self.name == "Admin":
                self.description = "Administrator with full access"
            elif self.name == "Staff":
                self.description = "Basic staff member role"
            elif self.name == "Supervisor":
                self.description = "Supervisor role with extended permissions"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.role.name}'


class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)  # Describe what action was performed (e.g., "Assigned Role")
    resource = models.CharField(max_length=255)  # Name of the resource being accessed (e.g., "Role")
    result = models.CharField(max_length=50)  # Whether the action was successful or failed
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set timestamp when log is created

    def __str__(self):
        return f"{self.user.username} - {self.action} on {self.resource} at {self.timestamp}"

    class Meta:
        verbose_name = 'Audit Log'
        verbose_name_plural = 'Audit Logs'
