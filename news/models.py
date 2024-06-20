from django.db import models
from django.utils import timezone



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=self.model.Status.Published)


class Category(models.Model):
    name=models.CharField(max_length=255)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Category"
        verbose_name_plural="Kategoriyalar"



class New(models.Model):

    class Status(models.TextChoices):
        Draft="DR","Draft"
        Published="PB","Published"

    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255)
    body=models.TextField()
    image=models.ImageField(upload_to="news/images")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    publish_time=models.DateTimeField(default=timezone.now)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.Draft)

    objects=models.Manager()  #default
    published=PublishedManager()   #ozgartirilgan


    class Meta:
        ordering=["-publish_time"]
        verbose_name="New"
        verbose_name_plural="Yangiliklar"





    def __str__(self):
        return self.title



class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name












