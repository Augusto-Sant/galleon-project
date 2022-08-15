from django.contrib import admin
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

#CUSTOM USERS (EXPANDED USER)
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Profiles"

class CustomizedUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)