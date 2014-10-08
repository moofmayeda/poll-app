from django.db import models


class Category(models.Model):
    category_text = models.CharField(max_length=200)
    def __unicode__(self):
      return self.category_text
    def total_tasks(self):
      return self.task_set.count()
    total_tasks.admin_order_field = 'total_tasks'
    total_tasks.integer = True

class Task(models.Model):
    category = models.ForeignKey(Category)
    task_text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    def __unicode__(self):
      return self.task_text
