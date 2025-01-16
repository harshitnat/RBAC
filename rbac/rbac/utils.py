# rbac/utils.py
from .models import AuditLog

def log_audit(user, action, resource, result):
    """
    Logs the action performed by the user.

    :param user: User object performing the action
    :param action: Description of the action (e.g., "assign_role")
    :param resource: The resource being accessed or modified (e.g., "Role Admin")
    :param result: Whether the action was granted or denied (e.g., "granted" or "denied")
    """
    AuditLog.objects.create(user=user, action=action, resource=resource, result=result)
