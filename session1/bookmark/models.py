from django.db import models

# Create your models here.
# DB에 들어갈 임의의 테이블의 필드값을 지정하는 곳

class Bookmark(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)