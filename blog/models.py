from django.db import models
import json

class Blog(models.Model):
    
    title = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateField(
        'Created:', auto_now_add=True, blank=True, null=True)
    date_modified = models.DateField(
        'Modified:', auto_now=True, blank=True, null=True)
    content = models.TextField(
        'Content', blank=True, null=True, default='The story of today..')

    def get_creation_date():
        return True

    def __str__(self):
        return json.dumps({'id': str(self.id),  'title': self.title, 'date_created': str(self.date_created)})