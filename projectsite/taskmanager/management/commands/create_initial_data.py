from django.core.management.base import BaseCommand
from faker import Faker
from django.utils import timezone
from taskmanager.models import Category, Priority, Task, SubTask, Note

class Command(BaseCommand):
    help = "Create initial demo data for Hangarin (categories, priorities, tasks, notes, subtasks)."

    def handle(self, *args, **kwargs):
        self.create_categories()
        self.create_priorities()
        self.create_tasks(25)

    def create_categories(self):
        categories = ["Work", "School", "Personal", "Finance", "Projects", "Health", "Errands"]
        for c in categories:
            Category.objects.get_or_create(name=c)

        self.stdout.write(self.style.SUCCESS('Categories created successfully.'))

    def create_priorities(self):
        priorities = ["High", "Medium", "Low", "Critical", "Optional"]
        for p in priorities:
            Priority.objects.get_or_create(name=p)

        self.stdout.write(self.style.SUCCESS('Priorities created successfully.'))

    def create_tasks(self, count):
        fake = Faker()
        categories = list(Category.objects.all())
        priorities = list(Priority.objects.all())

        for _ in range(count):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                priority=fake.random_element(elements=priorities),
                category=fake.random_element(elements=categories),
            )

            # Notes
            for _ in range(fake.random_int(min=0, max=2)):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2)
                )

            # Subtasks
            for _ in range(fake.random_int(min=0, max=3)):
                SubTask.objects.create(
                    parent_task=task,
                    title=fake.sentence(nb_words=4),
                    status=fake.random_element(elements=['Pending', 'In Progress', 'Completed']),
                    category=fake.random_element(categories)
                )

        self.stdout.write(self.style.SUCCESS('Tasks, SubTasks, and Notes created successfully.'))
