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
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=100, verbose_name="Модель")
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    color = models.CharField(max_length=50, verbose_name="Цвет")
    mileage = models.PositiveIntegerField(verbose_name="Пробег (км)")
    volume = models.FloatField(verbose_name="Объем двигателя (л)")
    body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES, verbose_name="Тип кузова")
    drive_unit = models.CharField(max_length=20, choices=DRIVE_UNIT_CHOICES, verbose_name="Привод")
    gearbox = models.CharField(max_length=20, choices=GEARBOX_CHOICES, verbose_name="Коробка передач")
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES, verbose_name="Тип топлива")
    price = models.DecimalField(
        max_digits=10,  # Исправлено
        decimal_places=2,  # Исправлено
        verbose_name="Цена ($)"
    )
    image = models.ImageField(
        upload_to='cars/',
        verbose_name="Изображение",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.model} ({self.year})"

class Sale(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name="Клиент"
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name="Автомобиль"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата продажи"
    )

    def __str__(self):
        return f"Продажа #{self.id}"