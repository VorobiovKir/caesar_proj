from __future__ import unicode_literals

from django.db import models


class Transcription(models.Model):
    legend = models.CharField(max_length=32)
    text_origin = models.TextField()
    rot = models.PositiveSmallIntegerField(default=0)
    encrypt = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.legend
