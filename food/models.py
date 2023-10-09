from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)    #default=1 is just for the previous items so they can be assigned to user number 1
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=1000, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTf-9vhp7--gDxiejt8MrzvQWG-yuM7ZqN6-51mVKFjtqUQ7ZwNUKjajpygTsqcsbbKmGg&usqp=CAU")

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
