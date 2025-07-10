from django.db import models





GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)
from django.db import models

# Ваши константы для choices (BODY_TYPE_CHOICES и т.д.)

class Client(models.Model):
    name = models.CharField(max_length=100, )
    phone = models.CharField(max_length=20,)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=100,)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50, )
    mileage = models.PositiveIntegerField()
    volume = models.FloatField()
    body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES, )
    drive_unit = models.CharField(max_length=20, choices=DRIVE_UNIT_CHOICES, )
    gearbox = models.CharField(max_length=20, choices=GEARBOX_CHOICES,)
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES, )
    price = models.DecimalField( max_digits=10,  decimal_places=2,   )
    image = models.ImageField(upload_to='cars/',null=True, blank=True)

    def __str__(self):
        return f"{self.model} ({self.year})"

class Sale(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Продажа #{self.id}"