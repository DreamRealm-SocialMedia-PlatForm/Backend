from django.db import models
import os
from django.contrib.auth import get_user_model


User = get_user_model()

class DreamCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

class Dream(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dream")
    category    = models.ManyToManyField(DreamCategory, related_name="dream")
    title       = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail   = models.ImageField(upload_to='thumbnails', null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} - {self.user.username}"
    def save(self, *args, **kwargs):
        try:
            old_instance = Dream.objects.get(pk=self.pk)
            if old_instance.thumbnail and old_instance.thumbnail != self.thumbnail:
                if os.path.isfile(old_instance.thumbnail.path):
                    os.remove(old_instance.thumbnail.path)
        except :
            pass
        return super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
            if self.thumbnail and os.path.isfile(self.thumbnail.path):
                os.remove(self.thumbnail.path)
            super().delete(*args, **kwargs)


    

class DreamLikes(models.Model):
    dream       = models.ForeignKey(Dream, on_delete=models.CASCADE, related_name="dream_likes")
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dream_likes")
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like: {self.dream.title} - {self.user.username}"

class DreamDislikes(models.Model):
    dream       = models.ForeignKey(Dream, on_delete=models.CASCADE, related_name="dream_dislikes")
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dream_dislikes")
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dislike: {self.dream.title} - {self.user.username}"

class DreamComment(models.Model):
    dream       = models.ForeignKey(Dream, on_delete=models.CASCADE, related_name="dream_comment")
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dream_comment")
    comment     = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dream.title} - {self.user.username}"

class DreamCommentLikes(models.Model):
    dream_comment       = models.ForeignKey(DreamComment, on_delete=models.CASCADE, related_name="dream_comment_likes")
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dream_comment_likes")
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like: {self.dream_comment.comment} - {self.user.username}"

class DreamCommentDislikes(models.Model):
    dream_comment       = models.ForeignKey(DreamComment, on_delete=models.CASCADE, related_name="dream_comment_dislikes")
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dream_comment_dislikes")
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dislike: {self.dream_comment.comment} - {self.user.username}"

