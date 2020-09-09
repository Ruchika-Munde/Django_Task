from django.db import models
from Userapp.models import User
from Postapp.models import Post

# Create your models here.
class Comment(models.Model):
    commentbox=models.TextField(blank=True, null='')
    cfileupload=models.FileField(upload_to='FileUpload/',null='' ,blank=True)
    commentforpost=models.ForeignKey(Post,on_delete=models.CASCADE)
    commentbyuser=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.commentbox

        