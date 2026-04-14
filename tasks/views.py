from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .tasks import send_task_email

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()

        # call celery task
        send_task_email.delay(
            task.assigned_to.email,
            task.title
        )