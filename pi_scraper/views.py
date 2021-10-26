from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# from pi_scraper.models import FileAdmin

# Create your views here.
def home (request):
    return render(request, 'home.html')

def upload(request):
    if request.method =='POST':
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(upload_file.name, upload_file)
    return render(request, 'upload.html')