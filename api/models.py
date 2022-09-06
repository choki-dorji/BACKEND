from django.db import models
import uuid

# Create your models here.
class ProjectDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name = models.TextField()
    project_category = models.TextField()
    project_cost = models.IntegerField()
    project_duration = models.IntegerField()
    Owner = models.TextField()
    person_in_charge = models.TextField()
    Date_from = models.TextField()
    Date_to = models.TextField()
    status = models.IntegerField()
    previlage = models.IntegerField()
    
    def __str__(self):
        return self.project_name

