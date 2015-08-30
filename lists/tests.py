from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from . import views
from .models import Task, List


class HomePageTest(TestCase):
  def test_root_url_resolves_to_homepage(self):
    page = resolve('/lists/')
    self.assertEqual(page.func, views.index)

  def test_homepage_display_all_tasks(self):
    list_ = List.objects.create()
    Task.objects.create(description='task one', list=list_)
    Task.objects.create(description='task two', list=list_)

    response = self.client.get('/lists/')

    self.assertContains(response, 'task one')
    self.assertContains(response, 'task two')

  def test_homepage_returns_correct_template(self):
    response = self.client.get('/lists/')
    self.assertTemplateUsed(response, 'lists.html')

  def test_homepage_saves_only_when_necessary(self):
    self.client.get('/lists/')
    self.assertEqual(Task.objects.count(), 0)



class NewListTest(TestCase):
  def test_saving_post_requests(self):
    self.client.post('/lists/new/', {'task_description': 'A new list item'})
    self.assertEqual(Task.objects.count(), 1)

  def test_redirects_after_post(self):
    response = self.client.post('/lists/new/', {'task_description': 'New task'})
    self.assertRedirects(response, '/lists/unique/')



class TaskModelTest(TestCase):
  def test_saving_and_retrieving_items(self):
    list_ = List.objects.create()
    task = Task.objects.create(description='first task', list=list_)
    second_task = Task.objects.create(description='second task', list=list_)

    saved_tasks = Task.objects.all()
    first_saved_task = saved_tasks[0]
    second_saved_task = saved_tasks[1]

    self.assertEqual(saved_tasks.count(), 2)
    self.assertEqual(first_saved_task.description, 'first task')
    self.assertEqual(second_saved_task.description, 'second task')



class ListViewTest(TestCase):
  def test_displays_all_items(self):
    list_ = List.objects.create()
    Task.objects.create(description='task one', list=list_)
    Task.objects.create(description='task two', list=list_)

    response = self.client.get('/lists/unique/')

    self.assertContains(response, 'task one')
    self.assertContains(response, 'task two')


  def test_uses_correct_template(self):
    response = self.client.get('/lists/unique/')

    self.assertTemplateUsed(response, 'list.html')
