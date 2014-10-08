from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from todos.models import Category, Task

class IndexView(generic.ListView):
  template_name = 'todos/index.html'
  context_object_name = 'all_categories'

  def get_queryset(self):
    return Category.objects.all()

def update_completed(request):
  try:
    selected_task = Task.objects.get(pk=request.POST['task'])
  except (KeyError, Task.DoesNotExist):
    return render(request, 'todos/index.html', {
      'error_message': "You didn't select a choice.",
      })
  else:
    selected_task.completed = True
    selected_task.save()
    return HttpResponseRedirect(reverse('todos:index'))
