from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User


class Item(models.Model):
    video = EmbedVideoField()
    title=models.CharField(max_length=264)
    description=models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    video=models.ForeignKey(Item,on_delete=models.CASCADE,related_name='video_comment')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='commenter')
    comment=models.TextField(max_length=264)
    commented_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='Comments'
        ordering=('-commented_at',)
        
    def __str__(self):
        return self.comment