from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import UploadedImage

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'image_uploader/upload_image.html', {'form': form})

def image_list(request):
    images = UploadedImage.objects.all()
    return render(request, 'image_uploader/image_list.html', {'images': images})
