from django.shortcuts import render

yellows = ['usama', 'romail', 'saif', 'rohan', 'sami']
# Create your views here.
def index(request):
    return render(request, 'hello/index.html', {
        "yellows": yellows
    })