from django.contrib import admin
from authentication.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_login', 'is_superuser', 'password')

admin.site.register(User, UserAdmin)
