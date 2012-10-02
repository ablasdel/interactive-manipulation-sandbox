from django.db import models
from djangotoolbox.fields import ListField
from .forms import StringListField

class TagsField(ListField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, StringListField, **kwargs)

class Place(models.Model):
    name = models.TextField()
    tags = TagsField()
    image = models.ImageField(upload_to="images")

    pose_x = models.FloatField()
    pose_y = models.FloatField()
    pose_angle = models.FloatField()

    map_x = models.IntegerField()
    map_y = models.IntegerField()
    map_width = models.IntegerField()
    map_height = models.IntegerField()

class Robot(models.Model):
    pass
