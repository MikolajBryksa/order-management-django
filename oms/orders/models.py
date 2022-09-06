from django.db import models


class Model(models.Model):
    # name = models.CharField(max_length=128)
    # description = models.TextField()

    # class Meta:
    #     verbose_name = "Model"
    #     verbose_name_plural = "Models"

    pass

    def __str__(self):
        return self.name
