from django.shortcuts import render

# Create your views here.
def addnumber(request):
    context = {}
    return render(request,'mathapp/addnumber.html',context)

def rectangle(request):
    context = {}
    return render(request,'mathapp/rectangle.html',context)
