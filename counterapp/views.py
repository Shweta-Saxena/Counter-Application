from django.shortcuts import render,redirect
from .models import Countermodel
# Create your views here.
def helloworld(request):
    name = "shweta"
    obj = Countermodel.objects.filter(id = 1)[0]
    ournumber = obj.number
    context = {'name' : name, 'number':ournumber}
    return render(request,"helloworld/helloworld.html",context)

# def hello(request):
#     return render(request,"helloworld/hello.html")

def increment(request):
    # here we write the code to increment value
   obj = Countermodel.objects.filter(id = 1)[0]
   obj.number = int(obj.number) + 1
   obj.save()
   return redirect(request.META['HTTP_REFERER'])

def decrement(request):
    # here we write the code to decrement value
    obj = Countermodel.objects.filter(id = 1)[0]
    obj.number = int(obj.number) - 1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])



def reset(request):
    # here we write the code to reset value
    obj = Countermodel.objects.filter(id = 1)[0]
    obj.number = 0
    obj.save()
    return redirect(request.META['HTTP_REFERER'])
