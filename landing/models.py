from django.db import models,migrations


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return "%s %s" % (self.name, self.email)
