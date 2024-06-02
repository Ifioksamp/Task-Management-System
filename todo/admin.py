from django.contrib import admin
from .models import Profile, Task, Comment
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
	list_display = ('name', 'gender', 'created_by', 'created_at')

admin.site.register(Profile, ProfileAdmin)


class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'priority', 'due_date', 'status')

admin.site.register(Task, TaskAdmin)


class CommentAdmin(admin.ModelAdmin):
	list_display = ('task', 'content')

admin.site.register(Comment, CommentAdmin)