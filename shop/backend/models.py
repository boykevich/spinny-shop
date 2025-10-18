from django.db import models
from django.urls.base import reverse

class ForkType(models.TextChoices):
    COIL = "coil"
    AIR = "air"

class BrakeType(models.TextChoices):
    RIM = "rim"
    VBRAKE = "vbrake"
    HYDRAULIC = "hydraulic"
    MECHANICAL = "mechanical"

class FrameType(models.TextChoices):
    ALU = "aluminum"
    STEEL = "steel"
    CARBON = "carbon"

class BoolType(models.IntegerChoices):
    YES = 1, "yes"
    NO = 0, "no"

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

class Bicycle(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    color = models.CharField(max_length=100)
    price = models.IntegerField()

    description = models.TextField()
    speeds = models.IntegerField()
    wheel_size = models.FloatField()
    year = models.IntegerField()
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT
    )
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), BoolType.choices)))
    is_available = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), BoolType.choices)))

    fork_type = models.CharField(max_length=10, choices=ForkType.choices)
    frame_size = models.IntegerField()
    frame_type = models.CharField(max_length=10, choices=FrameType.choices)
    brake_type = models.CharField(max_length=25, choices=BrakeType.choices)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bicycle Id: {self.pk}. {self.name} - {self.price}"

    class Meta:
        verbose_name = "Bicycle"
        verbose_name_plural = "Bicycles"

    def get_absolute_url(self):
        return reverse('backend:post', kwargs={'post_slug': self.slug})


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return f"Client Id: {self.pk}. {self.name}"

class Status(models.TextChoices):
    COMPLETED = "completed"
    PAYMENT_AWAIT = "payment await"
    IN_PROCESS = "in process"

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    bicycle = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices)

    def __str__(self):
        return f"Order Id: {self.pk}. {self.client} - {self.bicycle}"

class OrderedItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    bicycle_id = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
    total_price = models.IntegerField()

    def __str__(self):
        return f"Order Item Id: {self.pk}. {self.bicycle_id}"