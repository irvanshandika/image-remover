from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse
import os
from PIL import Image
from rembg import remove
import io

def home(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        
        # Validasi ukuran file
        if image.size > 10 * 1024 * 1024:  # 10MB
            return render(request, 'pages/home.html', {'error': 'File size exceeds 10MB'})
        
        # Proses seperti sebelumnya
        input_path = default_storage.save('tmp/input.png', ContentFile(image.read()))
        input_path = os.path.join(settings.MEDIA_ROOT, input_path)
        input_image = Image.open(input_path)
        output = remove(input_image)
        output_path = os.path.join(settings.MEDIA_ROOT, 'tmp/output.png')
        output.save(output_path)
        output_url = settings.MEDIA_URL + 'tmp/output.png'
        os.remove(input_path)
        return redirect('result', output_url=output_url)

    return render(request, 'pages/home.html')

def result(request, output_url):
    return render(request, 'pages/result.html', {'output_image': output_url})

def download_image(request, format):
    input_path = os.path.join(settings.MEDIA_ROOT, 'tmp/output.png')
    img = Image.open(input_path)
    
    # Normalisasi format
    format = format.upper()
    if format == 'JPG':
        format = 'JPEG'
    
    # Konversi ke RGB jika format adalah JPEG
    if format == 'JPEG':
        img = img.convert('RGB')
    
    # Simpan ke BytesIO
    img_io = io.BytesIO()
    img.save(img_io, format=format)
    img_io.seek(0)
    
    # Siapkan response
    content_type = f'image/jpeg' if format == 'JPEG' else f'image/{format.lower()}'
    response = HttpResponse(img_io, content_type=content_type)
    extension = 'jpg' if format == 'JPEG' else format.lower()
    response['Content-Disposition'] = f'attachment; filename=background_removed.{extension}'
    
    return response