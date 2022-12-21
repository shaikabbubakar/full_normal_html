
from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']    
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insert_topic is successfully inserted') 

    return render(request,'insert_topic.html')
def insert_webpage(request):
    topic=Topic.objects.all()
    d={'topic':topic}
    if request.method=='POST':
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        return HttpResponse('webpage is inserted successfully')
    return render(request,'insert_webpage.html',d)
def insert_accessrecords(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    Webpage=webpage.objects.all()
    if request.method=='POST':
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        dt=request.POST['dt']
        T=Topic.objects.get_or_create(topic_name=topics)[0]
        T.save()
        W=webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()  
        A=Access_records.objects.get_or_create(name=W,date=dt)[0]
        A.save()
        return HttpResponse('accessrecords is successfully created')
    return render(request,'insert_accessrecords.html',d)
def select_topic(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    if request.method=='POST':
        tn=request.POST.getlist('topic')
        Webpage=webpage.objects.none()
        for t in tn:
            Webpage=Webpage|webpage.objects.filter(topic_name=t)
        data={'Webpage':Webpage}
        return render(request,'display_webpage.html',data)
    return render(request,'select_topic.html',d)
def checkbox(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'checkbox.html',d)
