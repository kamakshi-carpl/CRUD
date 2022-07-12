from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="images/")
    uploadDate = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name