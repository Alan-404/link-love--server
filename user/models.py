from djongo import models

# Create your models here.
class UserModel(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=100)
    b_date = models.DateField()
    phone = models.CharField(max_length=12)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    class Meta:
        db_table = 'user'