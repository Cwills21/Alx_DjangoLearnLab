# bookshelf/signals.py
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == 'bookshelf':  # only run for this app
        # Make sure permissions exist
        permissions = {
            'can_view': Permission.objects.get(codename='can_view'),
            'can_create': Permission.objects.get(codename='can_create'),
            'can_edit': Permission.objects.get(codename='can_edit'),
            'can_delete': Permission.objects.get(codename='can_delete'),
        }

        editors, _ = Group.objects.get_or_create(name='Editors')
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        admins, _ = Group.objects.get_or_create(name='Admins')

        # assign perms
        editors.permissions.set([permissions['can_create'], permissions['can_edit']])
        viewers.permissions.set([permissions['can_view']])
        admins.permissions.set([
            permissions['can_view'],
            permissions['can_create'],
            permissions['can_edit'],
            permissions['can_delete'],
        ])
