from django.db import models

class Result(models.Model):
    result_title = models.CharField(max_length=300)
    def __str__(self):
        return self.result_title
