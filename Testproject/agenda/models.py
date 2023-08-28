from django.db import models

class Narrative(models.Model):
    name = models.CharField('Name', max_length=50)
    intro = models.CharField('Intro', max_length=250)
    full_text = models.TextField('Narrative')
    datentime = models.DateTimeField('Date and time when published')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/agenda/{self.id}'

