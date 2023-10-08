from django.db import models

# Create your models here.
class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=1000, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTf-9vhp7--gDxiejt8MrzvQWG-yuM7ZqN6-51mVKFjtqUQ7ZwNUKjajpygTsqcsbbKmGg&usqp=CAU")

