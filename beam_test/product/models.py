from django.db import models


class ProductImage(models.Model):
    image = models.ImageField('Изображение', upload_to='Products_images/')

    def __str__(self):
        return self.image.url if self.image else 'No Image'


class Product(models.Model):
    title = models.CharField(verbose_name='Название товара', max_length=150)
    description = models.TextField('Описание', max_length=500)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    image = models.OneToOneField(ProductImage, related_name='products', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(verbose_name='Категория товара', max_length=100)
    products = models.ManyToManyField(Product, related_name='categories')

    def __str__(self):
        return self.title


class Order(models.Model):
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return f'Order of {self.product.title}'
