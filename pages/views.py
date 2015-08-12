from django.shortcuts import render


def youtube(request):
  return render(request, template_name='youtube.html')
