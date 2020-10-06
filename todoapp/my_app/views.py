from django.shortcuts import render
from django.utils import timezone
from my_app.models import ToDo
from . import models


# Create your views here.
def home(request):
    return render(request, template_name = 'my_app/index.html')

def add_todo(request):
    added_date = timezone.now()
    content = request.POST["form_content"]
    models.ToDo.objects.create(added_date=added_date, text=content)
    return render(request, template_name = 'my_app/index.html')
