from django.db import models

# Create your models here.
class BaseModel(models.Model):
   created_at = models.DateTimeField(auto_now_add=True, db_index=True)
   updated_at = models.DateTimeField(auto_now=True)
   class Meta:
      abstract = True

class Priority(BaseModel):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
     return self.name
    

STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("In Progress", "In Progress"),
    ("Completed", "Completed"),
]
    
class Task(BaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)    
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title



    

class Note(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return f"Note for {self.task.title}"
    
class SubTask(BaseModel):
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "SubTask"
        verbose_name_plural = "SubTasks"

    def __str__(self):
        return f"{self.title} (Task: {self.parent_task.title})"

    
