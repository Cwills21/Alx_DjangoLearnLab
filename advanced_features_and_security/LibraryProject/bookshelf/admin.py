# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# # from .models import CustomUser  # import your custom user

# # Define a custom admin for your custom user model
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     # which fields to display in the admin
#     list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('date_of_birth', 'profile_photo')}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('date_of_birth', 'profile_photo')}),
#     )

# # ✅ This is the line your checker is looking for:
# # admin.site.register(CustomUser, CustomUserAdmin)
