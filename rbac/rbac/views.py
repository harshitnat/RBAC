from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Role, Permission, UserRole, AuditLog
from django.contrib.auth.models import User
from .serializers import RoleSerializer, PermissionSerializer, UserRoleSerializer
from .utils import log_audit  # Import the log_audit function

# Get list of roles
@api_view(['GET'])
def get_roles(request):
    roles = Role.objects.all()
    serializer = RoleSerializer(roles, many=True)
    return Response(serializer.data)

# Get a specific role by ID
@api_view(['GET'])
def get_role_by_id(request, pk):
    try:
        role = Role.objects.get(pk=pk)
    except Role.DoesNotExist:
        return Response({"error": "Role not found"}, status=404)
    
    serializer = RoleSerializer(role)
    return Response(serializer.data)

# Get list of permissions
@api_view(['GET'])
def get_permissions(request):
    permissions = Permission.objects.all()
    serializer = PermissionSerializer(permissions, many=True)
    return Response(serializer.data)

# Assign role to a user
@api_view(['POST'])
def assign_role(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    role_id = request.data.get('role_id')
    try:
        role = Role.objects.get(id=role_id)
    except Role.DoesNotExist:
        return Response({"error": "Role not found"}, status=404)

    # Assign the role to the user
    UserRole.objects.create(user=user, role=role)

    # Log the action
    log_audit(user, 'assign_role', f'Role {role.name}', 'granted')

    return Response({"message": "Role assigned successfully!"})

# Get audit logs
@api_view(['GET'])
def get_audit_logs(request):
    logs = AuditLog.objects.all()
    data = []
    for log in logs:
        data.append({
            'user': log.user.username,
            'action': log.action,
            'resource': log.resource,
            'result': log.result,
            'timestamp': log.timestamp,
        })
    return Response({"logs": data})
