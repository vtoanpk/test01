from django.db import models
import random
import os
from django.urls import reverse
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modiffied = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True

class Product(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("product_detail", args=[str(self.slug)])


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


'''
unique_slug_generator
'''


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # instance.slug = create_slug(instance)
        instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_post_receiver, sender=Product)