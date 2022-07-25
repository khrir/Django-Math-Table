from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'home.html')

def add(request):
    valor = int(request.GET['number'])
    return render(request, 'table.html', {"number": valor})