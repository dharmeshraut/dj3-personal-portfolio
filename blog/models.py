from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length= 100)
    blog_date = models.DateField(auto_now= True)
    image = models.ImageField(upload_to='portfolio/images/', blank= True)
    description = models.TextField()

    def __str__(self):
        return self.title
