from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import View,TemplateView
from app.forms import *

#creating view by using fbv
def string_by_fbv(request):
    return HttpResponse('<h1> string_by_fbv</h1>')
#creating view by using cbv
class StringByCbv(View):
    def get(self,request):
        return HttpResponse('<h1>StringByCbv</h1>')

#creating a html page by using fbv
def html_by_fbv(request):
    return render(request,'html_by_fbv.html')
#creating a html page by using fbv
class HtmlByCbv(View):
    def get(self,request):
        return render(request,'HtmlByCbv.html')


#creating form by using fbv
def school_Fbv(request):
    d={'ESFO':SchoolForm()}
    if request.method=='POST':
        SFO=SchoolForm(request.POST)
        if SFO.is_valid():
            SFO.save()
            return HttpResponse('Data is inserted succesfully')
        else:
            return HttpResponse('Data is Invalid')   
    return render(request,'school_Fbv.html',d)
#creating form by using cbv
class School_Cbv(View):
    def get(self,request):
        d={'ESFO':SchoolForm()}
        return render(request,'School_Cbv.html',d)

    def post(self,request):
        if request.method=='POST':
            SFO=SchoolForm(request.POST)
            if SFO.is_valid():
                SFO.save()
                return HttpResponse('Data is inserted succesfully')
            else:
                return HttpResponse('Data is Invalid')  


class HtmlByTv(TemplateView):
    template_name='HtmlByTv.html'
