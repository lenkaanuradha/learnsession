from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']='Sonam'
    return render(request,'setsession.html')

def getsession(request):
    nm=request.session.get('name',default="Guest")
    return render(request,'getsession.html',{'n':nm})

def delsession(request):
    if 'name' in request.session:
     del request.session['name']
     return render(request,'delsession.html')