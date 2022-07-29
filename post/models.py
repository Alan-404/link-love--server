from djongo import models



# Create your models here.
class PostModel(models.Model):
    _id = models.ObjectIdField()
    user_id = models.CharField(max_length=50)
    content = models.TextField()
    mode = models.CharField(max_length=15)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    class Meta:
        db_table = 'post'