from django.shortcuts import render, redirect
from .forms import URLForm
from .models import ShortenedURL
import random, string

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def shorten_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            short_url = generate_short_url()
            new_url = form.save(commit=False)
            new_url.short_url = short_url
            new_url.save()
            return redirect('url_list')
    else:
        form = URLForm()
    return render(request, 'shortener/shorten_url.html', {'form': form})

def url_list(request):
    urls = ShortenedURL.objects.all()
    return render(request, 'shortener/url_list.html', {'urls': urls})
