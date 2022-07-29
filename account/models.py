from djongo import models

# Create your models here.

class AccountModel(models.Model):
    _id = models.ObjectIdField()
    password = models.CharField(max_length=150)
    user_id = models.CharField(max_length=50)
    role = models.BooleanField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    class Meta:
        db_table = 'account'
