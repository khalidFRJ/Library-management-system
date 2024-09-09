from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) :
        return self.name


class Book(models.Model):

    status_book = [
        ('availble' , 'availble'),
        ('rental', 'rental'),
        ('sold', 'sold')

    ]




    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    photo_Book = models.ImageField(upload_to='photos' , null=True , blank=True)
    photo_author = models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField(null=True , blank=True)
    price = models.DecimalField(max_digits=9 , decimal_places=5 , null=True , blank=True)
    relar_price_day = models.DecimalField(max_digits=9 , decimal_places=2 , null=True , blank=True)
    relat_period = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50 , choices= status_book , null= True , blank= True)
    category = models.ForeignKey(Category , on_delete=models.PROTECT , null= True , blank= True)

    def __str__(self) :
        return self.title
    
