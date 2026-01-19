from django.shortcuts import render
from tasks.models import Project, Task

# Create your views here.
def project_list(request):
    # print(request.tenant) # added by TenantMiddleware
    projects = Project.objects.all().prefetch_related("tasks")

    context = {
        "projects": projects,
    }

    return render(request, 'tasks/project_list.html', context)