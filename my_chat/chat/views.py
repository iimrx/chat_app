from django.shortcuts import render

# Create our views here.
def home(request):
  return render(request, 'index.html')