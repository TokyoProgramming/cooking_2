from django.db import models

FIELD_CHOICES = (
    ('ARTICLE', 'ARTICLE'),
    ('PHILOSOPHY', 'PHILOSOPHY'),
    ('FASHION', 'FASHION'),
    ('LIFESTYLE', 'LIFESTYLE'),
    ('NATURE', 'NATURE'),
    ('TRAVEL', 'TRAVEL'),

)


class featuredPost(models.Model):
    featured_field = models.CharField(choices=FIELD_CHOICES, max_length=20, default=None)
    featured_tittle = models.CharField(max_length=100)
    featured_text = models.TextField(max_length=300)
    featured_image = models.ImageField(upload_to='featuredImage')

    def __str__(self):
        return self.featured_tittle


class Post(models.Model):

    blog_field = models.CharField(choices=FIELD_CHOICES, max_length=20, default=None)
    blog_tittle = models.CharField(max_length=20)
    blog_text = models.TextField(max_length=500)
    published_date = models.DateTimeField(auto_now=True)
    blog_image = models.ImageField(upload_to='blogImage')

    def __str__(self):
        return self.blog_field
