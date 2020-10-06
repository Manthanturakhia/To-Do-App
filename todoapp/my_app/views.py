from django.shortcuts import render
from django.utils import timezone
from my_app.models import ToDo
from . import models
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items = ToDo.objects.all().order_by("-added_date")
    return render(request, template_name = 'my_app/index.html',context={
        "todo_items" : todo_items
    })

def add_todo(request):
    added_date = timezone.now()
    content = request.POST["form_content"]
    created_obj = models.ToDo.objects.create(added_date=added_date, text=content)
    length_of_todos = ToDo.objects.all().count()
    return HttpResponseRedirect("/")

def  delete_todo(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    print(todo_id)
    return HttpResponseRedirect("/")

