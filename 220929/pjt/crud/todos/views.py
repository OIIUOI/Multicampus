from django.shortcuts import render, redirect
from .models import todo

# Create your views here.
def index(request):
    todos = todo.objects.all()
    context = {"todos": todos}
    return render(request, "todos/index.html", context)


def create(request):
    todo = request.GET.get(todo)
    completed = request.GET.get(completed)
    priority = request.GET.get(priority)
    created_at = request.GET.get(created_at)
    deadline = request.GET.get(deadline)

    todo.objects.create(
        content=todo,
        completed=completed,
        priority=priority,
        created_at=created_at,
        deadline=deadline,
    )
    content = {
        "todo": todo,
        "completed": completed,
        "priority": priority,
        "created_at": created_at,
        "deadline": deadline,
    }

    return redirect("todos:index.html")
