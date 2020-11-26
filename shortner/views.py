from django.shortcuts import render,redirect,HttpResponse
from nanoid import generate
from .models import Urls
import os
# Create your views here.
def index(request,_url=None):
    if Urls.objects.get(slug=_url):
        url = Urls.objects.get(slug=_url)
        print(url.slug)
        url.views = url.views + 1
        url.save()
        return redirect (url.url)
    else:
        return redirect('/create')

def index2(request):
    return redirect('/create')

def create(request):
    context= {}
    base_url = os.environ['SERVER']
    if request.method == 'POST':
        _url = request.POST.get('url')
        if Urls.objects.filter(url=_url):
            url = Urls.objects.filter(url=_url)[0]
            complete_url = f'{base_url}{url.slug}' 
            print(complete_url,'.........................')
            # return HttpResponse(f'Your Url is : <a href={complete_url} target=_blank>{complete_url}</a>' )
            context['url'] = url.slug
            context['status'] = '1'
            context['server'] = base_url
            return render(request,'created.html', context)
        else:
            if request.POST.get('myslug'):
                myslug = request.POST.get('myslug')
                if Urls.objects.filter(slug=myslug):
                    url = Urls.objects.filter(slug=myslug)[0]
                    complete_url = url.url 
                    print(complete_url,'.........................')
                    # return HttpResponse(f'This URL <a href={complete_url} target=_blank>{complete_url}</a> already exists with name: {myslug}' )
                    context['url'] = complete_url
                    context['myslug'] = url.slug
                    context['status'] = '2'
                    context['server'] = base_url
                    return render(request,'created.html', context)
                else:
                    db_url = Urls()
                    db_url.slug = request.POST.get('myslug')
                    db_url.url = request.POST.get('url')
                    db_url.save()
                    complete_url = f'{base_url}{db_url.slug}'
                    # return HttpResponse(f'Your Url is : <a href={complete_url} target=_blank>{complete_url}</a>' )    
                    context['url'] = db_url.slug
                    context['myslug'] = db_url.slug
                    context['status'] = '3'
                    context['server'] = base_url
                    return render(request,'created.html', context)
            else:
                db_url = Urls()
                db_url.slug = generate('abcdefghijklmnopqrstuvwxyz1234567890',6)
                db_url.url = request.POST.get('url')
                db_url.save()
                complete_url = f'{base_url}{db_url.slug}'
                context['url'] = db_url.slug
                ontext['status'] = '4'
                context['server'] = base_url
                return render(request,'created.html', context)
                # return HttpResponse(f'Your Url is : <a href={complete_url} target=_blank>{complete_url}</a>' )
    else:
        return render(request,'index.html')

def list_short(request):
    base_url = os.environ['SERVER']
    context = {}
    myslug = request.POST.get('slug')
    if myslug:
        if request.method == 'POST':
            url = Urls.objects.filter(slug=myslug)[0]
            url.delete()    
            return redirect('/list/')
    else:
        url_list = Urls.objects.all()
        context['list'] = url_list
        context['server'] = base_url
        
    return render(request,'list.html',context)

            
