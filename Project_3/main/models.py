from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class SubService(models.Model):
    service = models.ForeignKey(Service, related_name='subservice', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    duration = models.IntegerField(help_text="Time Duration in Minutes")

    def __str__(self):    
        return f"{self.title} ({self.service.title})"
    
    
   


