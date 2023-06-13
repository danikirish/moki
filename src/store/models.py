from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f"self.name"


class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    # image = models.ImageField(upload_to="products")
    stock = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"self.name"

    def in_stock(self):
        return self.stock > 0

    def get_discount_price(self):
        return self.price - self.price * self.discount / 100

    def deduct_stock(self, quantity=1):
        self.stock -= quantity
        self.save()


class Order(models.Model):
    name = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    # email = models.EmailField(max_length=100)
    # address = models.CharField(max_length=100)
    # postal_code = models.CharField(max_length=100)
    # city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    products = models.ManyToManyField(Product, through="OrderItem")

    def __str__(self):
        return f"self.name"
