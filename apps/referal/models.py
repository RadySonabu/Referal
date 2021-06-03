from django.db import models

# Create your models here.


class BaseModel(models.Model):

    is_active = models.BooleanField()
    modified_by = models.CharField(max_length=50)
    modified_date = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    class Meta:
        ordering = ['-modified_date']

    def __str__(self):
        return self.name


class Location(BaseModel):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['-modified_date']

    def __str__(self):
        return self.name


class Provider(BaseModel):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-modified_date']

    def __str__(self):
        return self.name
