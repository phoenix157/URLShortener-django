from django.shortcuts import render, get_object_or_404, redirect
from .forms import ShortURLForm
from url_shortener.settings import LOCAL_HOST
from .models import ShortURL

# Create your views here.
def index(request):
    form = ShortURLForm(request.POST or None)
    code = ''
    if form.is_valid():
        data = form.save(commit=False)
        url = form.cleaned_data['url']
        data.save()
        dataset = ShortURL.objects.filter(url=url)
        code = dataset[0].code
        short_url = LOCAL_HOST + '/' + code
        return render(request, 'shortener/index.html', {'form':form, 'short_url':short_url, 'code':code})
    else:
        return render(request, 'shortener/index.html', {'form':form, 'code':code})

def redirect_original(request, short_id):
    url = get_object_or_404(ShortURL, code=short_id)
    return redirect(str(url))

