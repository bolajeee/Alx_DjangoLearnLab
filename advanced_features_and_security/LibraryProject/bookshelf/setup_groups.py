from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from .models import Post

class Command(BaseCommand):
    def handle(self, *args, **options):
        permissions = {
            'Editors': ['can_create', 'can_edit'],
            'Viewers': ['can_view'],
            'Admins': ['can_create', 'can_edit', 'can_delete', 'can_view'],
        }

        for group_name, perms in permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for codename in perms:
                permission = Permission.objects.get(codename=codename)
                group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Groups and permissions setup complete.'))
