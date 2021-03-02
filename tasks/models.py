from django.db import models

# Create your models here.
class Task(models.Model):
    CATEGORIES_CHOICES = (('Important', 'Important'),
                  ('Optional', 'Optional'),
                  ('Daily update', 'Daily update'),
                  ('Weekly update', 'Weekly update'),
                  )
    category = models.CharField(max_length= 200, choices= CATEGORIES_CHOICES)
    title = models.CharField(max_length= 200)
    complete = models.BooleanField(default= False)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title
