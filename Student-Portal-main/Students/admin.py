from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "course", "year_level")
    list_filter = ("course", "year_level")
    search_fields = ("name",)
    ordering = ("name",)

    # ✅ Allow all users to add students
    def has_add_permission(self, request):
        return True

    # ❌ Only allow editing if user is superuser
    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)

    # ❌ Only allow deleting if user is superuser
    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)

    # ✅ Only show this model to non-admin users
    def get_model_perms(self, request):
        if request.user.is_superuser:
            return super().get_model_perms(request)
        return {'add': True, 'change': False, 'delete': False, 'view': True}


# ==============================
# ✅ Hide other apps for non-admins
# ==============================
original_index = admin.site.index

def custom_index(request, extra_context=None):
    if not request.user.is_superuser:
        extra_context = extra_context or {}
        # Show only the Students app for normal users
        extra_context['app_list'] = [
            app for app in admin.site.get_app_list(request)
            if app['app_label'] == 'Students'
        ]
    return original_index(request, extra_context)

admin.site.index = custom_index

# Optional: change admin header text
admin.site.site_header = "Student Management"
admin.site.site_title = "Student Management"
admin.site.index_title = "Site administration"
