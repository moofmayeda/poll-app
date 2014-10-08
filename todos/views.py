from django.shortcuts import render
from django.views import generic

from todos.models import Category, Task

class IndexView(generic.ListView):
  template_name = 'todos/index.html'
  context_object_name = 'all_categories'

  def get_queryset(self):
    return Category.objects.all()
