from django.shortcuts import render

# Create your views here.
def credo(request):
    print('credo')
    return render(request, 'credo/credo.html')