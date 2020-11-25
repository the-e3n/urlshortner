from django.shortcuts import render,redirect,HttpResponse
from nanoid import generate
from .models import Urls
# Create your views here.
def index(request,_url):
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
    base_url = request.META['REMOTE_ADDR']
    base_scheme = request.scheme
    if request.method == 'POST':
        _url = request.POST.get('url')
        if Urls.objects.filter(url=_url):
            url = Urls.objects.filter(url=_url)[0]
            complete_url = f'{base_scheme}://{base_url}:8000/go/{url.slug}' 
            print(complete_url,'.........................')
            return HttpResponse(f'Your Url is : <a href={complete_url} target=_blank>{complete_url}</a>' )
        else:
            db_url = Urls()
            db_url.slug = generate('abcdefghijklmnopqrstuvwxyz1234567890',5)
            db_url.url = request.POST.get('url')
            db_url.save()
            complete_url = f'{base_scheme}://{base_url}:8000/go/{db_url.slug}'
            return HttpResponse(f'Your Url is : <a href={complete_url} target=_blank>{complete_url}</a>' )
    else:
        return render(request,'index.html')

def list_short(request):
    context = {}
    if request.method == 'POST':
        url = Urls.objects.get(slug=request.POST.get('slug'))
        url.delete()    
        return redirect('/list')
    else:
        url_list = Urls.objects.all()
        context['list'] = url_list
        
        return render(request,'list.html',context)

            