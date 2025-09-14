from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file_path = models.CharField(max_length=500)
    time = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class SubService(models.Model):
    service = models.ForeignKey(Service, related_name='subservice', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    duration = models.IntegerField(help_text="Time Duration in hours")

    def __str__(self):    
        return f"{self.title} ({self.service.title})"
    
class Reservation(models.Model):
    service = models.ForeignKey(
        'Service',           # nazwa modelu usług
        on_delete=models.CASCADE,
        related_name='reservations'
    )
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.service.name} - {self.date} {self.time}"
    
    
   


