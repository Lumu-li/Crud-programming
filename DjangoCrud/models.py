from django.db import models


class stude(models.Model):
    name = models.CharField(max_length=30, blank=False,null=False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.IntegerField(max_length=30, blank=False, null=False)


    def _str_(self):
        return self.name