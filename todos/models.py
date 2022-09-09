from django.db import models

# Create your models here.
class task(models.Model):
    item = models.CharField(max_length=400)
    status = models.BooleanField(default= False)
    completed_at = models.DateTimeField(auto_now=True)
    created_at =models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.item + '|' + str(self.status)
    