from django.db import models

class RoastBoast(models.Model):
    roast = models.BooleanField(default=True)
    content = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    posttime = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    @property
    def total_votes(self):
        return self.upvotes - self.downvotes
 