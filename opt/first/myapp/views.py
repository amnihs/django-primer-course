from django.shortcuts import render

# Create your views here.
def index(request):
  """/トップページ"""
  context = {
    'name': 'amnihs',
  }
  return render(request, 'myapp/index.html', context)

def about(request):
  """/about アバウトページ"""
  return render(request, 'myapp/about.html')

def info(request):
  """/info インフォページ"""
  return render(request, 'myapp/info.html')
