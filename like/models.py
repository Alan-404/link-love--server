from djongo import models

# Create your models here.

class LikeModel(models.Model):
    _id = models.ObjectIdField()
    post_id = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    status = models.BooleanField(default=True)
    class Meta:
        db_table = 'like'
