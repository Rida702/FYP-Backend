# views.py
from django.shortcuts import render
from .forms import ImageUploadForm
from PIL import Image
from .models import ImageModel
from io import BytesIO

def index_view(request):
    return render(request, 'index.html')

def upload_view(request):
    return render(request, 'upload.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance1_image = form.cleaned_data['image']
            instance1_image_obj = Image.open(instance1_image)
            instance2_image = instance1_image_obj.convert('L')

            my_model_instance = ImageModel()
            my_model_instance.image.save(instance1_image.name, instance1_image)

            my_model_instance.grayscale_image.save(f"grayscaled/grayscale_{instance1_image.name}", instance2_image)

            context = {
                'original_image_url': my_model_instance.image.url,
                'grayscale_image_url': my_model_instance.grayscale_image.url,
            }
            return render(request, 'result.html', context)
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})