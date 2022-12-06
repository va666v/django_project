from django.shortcuts import HttpResponse
from datetime import datetime
from tasks.models import Task


# Create your views here.
def home_view(request):
    return HttpResponse("Hello from Django")


def welcome_page(request):
    return HttpResponse("<h3 style='text-align:center; background-color:powderblue'>Hello From 1st task</h3>")


def intro_page(request):
    return HttpResponse("<h1 style='text-align:center'> <b>Python + Django </b> </h1>"
                        "<p>Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.</p>"
                        "<p>What can Python do? <br>1.Python can be used on a server to create web applications.<br>2.Python can be used alongside software to create workflows. <br>3.Python can connect to database systems. It can also read and modify files. <br>4.Python can be used to handle big data and perform complex mathematics. <br>5.Python can be used for rapid prototyping, or for production-ready software development.</p>")


def date_time(request):
    return HttpResponse(f"<h1 style='text-align:center; background-color:DodgerBlue'> <b>{datetime.now()}</b> </h1>")


def task_page(request):
    dict_ = {}
    for i in range(1, 16):
        dict_[i] = (i**2)
    return HttpResponse(f"{str(dict_)}")


def create_task(request):
    # new_task = Task(
    #     name='task_3',
    #     description='desc_3'
    # )
    # new_task.save()

    new_task = Task.objects.create(name='task_4')
    return HttpResponse(f"task: {new_task}")


def get_all_tasks(request):
    tasks_list = Task.objects.all()
    tasks = [task.name for task in tasks_list]
    return HttpResponse(f"task: {tasks}")


def get_tasks(request):
    status = request.GET.get('status')
    if status is not None:
        tasks_list = Task.objects.filter(status='status')
    else:
        tasks_list = Task.objects.all()
    tasks_list = Task.objects.all()
    tasks = [task.name for task in tasks_list]
    return HttpResponse(f"task: {tasks}")


def update_task(request, task_id):
    task_ = Task.objects.filter(id=task_id).fisrt()
    task_ = Task.objects.get(id=task_id)
    task_.name = 'updated'
    task_.save()
    return HttpResponse(f"task: {task_}")
