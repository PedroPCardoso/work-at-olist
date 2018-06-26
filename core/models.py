from django.db import models

class CallInitial(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField();
    call_id = models.IntegerField();
    source = models.CharField(max_length=9)
    destination = models.CharField(max_length=9)

class CallEnd(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField();
    call_id = models.IntegerField();