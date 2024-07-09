from django.shortcuts import render


# Create your views here.
def inicio(request):
    dic = {}
    return render(request,'inicio.html',dic)