from django.shortcuts import render
from django.http import HttpResponse
from .models import teams,adjudicators
# Create your views here.
def index(request):
    return render(request,'pd.html')

def updatedata(request):
    if request.method=='POST':
        if request.POST.get('name1') and request.POST.get('name2') and request.POST.get('name3') and request.POST.get('contactno1') and request.POST.get('college1'):
            team=teams()
            team.Name1=request.POST.get('name1')
            team.Name2=request.POST.get('name2')
            team.Name3=request.POST.get('name3')
            team.College=request.POST.get('college1')
            team.Contactno=request.POST.get('contact1')
            
            return HttpResponse("successful")
        if request.POST.get('name') and request.POST.get('college2') and request.POST.get('contactno2'):
            adjudicators=adjudicator()
            adjudicator.name=request.POST.get('name')
            adjudicator.college=request.POST.get('college2')
            adjudicator.contactno=request.POST.get('contactno2')
        