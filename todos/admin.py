from django.contrib import admin
from todos.models import Category, Task

class TaskInline(admin.TabularInline):
  model = Task
  extra = 3

class CategoryAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,               {'fields': ['category_text']}),
  ]
  inlines = [TaskInline]
  list_display = ('category_text', 'total_tasks')
  search_fields = ['category_text']

admin.site.register(Category, CategoryAdmin)
