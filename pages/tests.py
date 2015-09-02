from django.core.urlresolvers import resolve
from django.test import TestCase

from . import views


class PagesTest(TestCase):
  def test_index_page_resolves_correctly(self):
    result = resolve('/')
    self.assertIs(result.func, views.index)

  def test_about_page_resolves_correctly(self):
    result = resolve('/about/')
    self.assertIs(result.func, views.about)
