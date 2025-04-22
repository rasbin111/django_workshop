from django.contrib import admin

from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner")

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_readonly_fields(request, obj)

        if request.user.has_perm('blog.can_publish'):
            return ('title', 'content', 'owner')  # Only allow editing `published`
        return super().get_readonly_fields(request, obj)

    def has_change_permission(self, request, obj=None):
        # Optional: Allow change only if user has the custom permission
        if obj and request.user.has_perm('blog.can_publish'):
            return True
        return super().has_change_permission(request, obj)