from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=True, upload_to='images/')
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    read_time = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(default='', max_length=255, unique=True)
    post = models.TextField(default='')
    published = models.BooleanField(default=False)
    featured_post = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
 
    def __str__(self):
     return f"{self.title}"
