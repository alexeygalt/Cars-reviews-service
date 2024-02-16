from django.db import models

from reviews.validators import validate_four_digit_year


class Country(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Страна")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Car(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Производитель")
    start_year = models.IntegerField(verbose_name="Год начала выпуска", validators=[validate_four_digit_year])
    end_year = models.IntegerField(verbose_name="Год окончания выпуска", validators=[validate_four_digit_year])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


class Comment(models.Model):
    author_email = models.EmailField(verbose_name="Email автора")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата/Время создания")
    comment = models.TextField(verbose_name="Комментарий")

    def __str__(self):
        return f"Комментарций от  {self.author_email} на  {self.car.name}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        indexes = [models.Index(fields=["created_at"])]
        ordering = ["-created_at"]
