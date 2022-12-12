from django.db import models
from star_all.models import Star, StarWork


class Banner(models.Model):
    name = models.CharField(max_length=300)
    text = models.CharField(max_length=500)
    image = models.FileField(upload_to='banners')
    link = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} | {self.text}'


class Popular(models.Model):
    custom_id = models.IntegerField()
    star = models.ForeignKey(Star, on_delete=models.CASCADE, related_name='popular')
    image = models.FileField(upload_to='banners')

    def __str__(self):
        return f'{self.custom_id} | {self.star.name}'

    class Meta:
        ordering = ['custom_id']


class Catalog(models.Model):
    custom_id = models.IntegerField()
    star = models.ForeignKey(Star, on_delete=models.CASCADE, related_name='catalog')

    def __str__(self):
        return f'{self.custom_id} | {self.star.name}'

    class Meta:
        ordering = ['custom_id']


class ExampleHomePage(models.Model):
    custom_id = models.IntegerField()
    star = models.ForeignKey(Star, on_delete=models.CASCADE, related_name='example')
    work = models.ForeignKey(StarWork, on_delete=models.CASCADE, related_name='home_example')

    def __str__(self):
        return f'{self.custom_id} | {self.star.name}'

    class Meta:
        ordering = ['custom_id']


class CommentHomePage(models.Model):
    custom_id = models.IntegerField()
    image = models.FileField(upload_to='home-comment-images')
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.custom_id} | {self.text}'

    class Meta:
        ordering = ['custom_id']


class Reaction(models.Model):
    custom_id = models.IntegerField()
    star = models.ForeignKey(Star, on_delete=models.CASCADE, related_name='reactions')
    video = models.FileField(upload_to='home-comment-works')

    def __str__(self):
        return f'{self.custom_id} | {self.star.name}'

    class Meta:
        ordering = ['custom_id']


