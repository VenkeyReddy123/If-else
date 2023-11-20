from django.shortcuts import render

# Create your views here.
def Condtion(request):
    max={'a':50,'b':20,'c':30,'d':40}
    return render(request,'Condtion.html',max)