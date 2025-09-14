from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-only/', admin_view, name='admin_view'),
    path('librarian-only/', librarian_view, name='librarian_view'),
    path('member-only/', member_view, name='member_view'),
]
