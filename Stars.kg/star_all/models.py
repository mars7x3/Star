from django.db import models


class StarCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True, primary_key=True)

    def __str__(self):
        return self.title


class Star(models.Model):
    category = models.ForeignKey(StarCategory, on_delete=models.SET_NULL, null=True, related_name='stars')
    image = models.FileField(upload_to='star-images')
    name = models.CharField(max_length=300)
    description = models.TextField()
    deadline = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name


class StarComment(models.Model):
    star = models.ForeignKey(Star, on_delete=models.CASCADE, related_name='star_comments')
    image = models.FileField(upload_to='comment_images')
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.star.name


class StarWork(models.Model):
    star = models.ForeignKey(Star, on_delete=models.CASCADE, related_name='star_works')
    video = models.FileField(upload_to='star_works')

    def __str__(self):
        return f'{self.id}. {self.star.name}'


class Orders(models.Model):
    star = models.ForeignKey(Star, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    for_who = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    text = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}. {self.star.name}'


class ToastCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True, primary_key=True)

    def __str__(self):
        return self.title


class Toast(models.Model):
    category = models.ForeignKey(ToastCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=300)
    text = models.TextField()

    def __str__(self):
        return self.title

