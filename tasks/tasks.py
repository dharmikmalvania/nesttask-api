from celery import shared_task

@shared_task
def send_task_email(user_email, task_title):
    print(f"📧 Email sent to {user_email} for task: {task_title}")