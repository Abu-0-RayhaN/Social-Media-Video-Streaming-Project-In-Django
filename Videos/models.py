from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title= models.CharField(max_length=20,default=None)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural= "Catogories"# when we see in admin pannel it shows every model with 's but when can declare by saying this 
        
      
class Uploads(models.Model):
    creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name='upload')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    thambnail= models.ImageField(upload_to='video_thabmnail',blank=False)
    title=models.CharField(max_length=264,blank=True)
    videofile= models.FileField(upload_to='videos/', null=True)
    upload_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering =['-upload_date']
        verbose_name_plural= "Uploads"
    def __str__(self):
        return self.title+'@'+str(self.creator)
    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id :

            return Uploads.objects.filter(category=category_id)
        else:
            return Uploads.objects.all()
class Like(models.Model):
    post=models.ForeignKey(Uploads,on_delete=models.CASCADE,related_name='like_post')
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='liker')
    date_created= models.DateTimeField(auto_now_add=True)
    def __st__(self):
        return str(self.user)+' liked '+str(self.post)

class Comment(models.Model):
    upload = models.ForeignKey(Uploads, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)
        
    def __str__(self):
        return self.comment
