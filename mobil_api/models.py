from django.db import models


class Worker(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя",
        blank=False,
        null=False
    )
    # Можно сделать проверку номера телефона. Но не стал сделать т.к. это не обязательно
    phone_num = models.CharField(
        max_length=255,
        verbose_name="Номер телефона",
        unique=True
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return self.name


class POS(models.Model):
    pos_name = models.CharField(
        max_length=255,
        verbose_name="Название",
    )
    worker = models.ForeignKey(
        Worker,
        verbose_name="Работник",
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ("pos_name",)
        verbose_name = "Торговая точка"
        verbose_name_plural = "Торговые точки"

    def __str__(self):
        return self.pos_name


class Visit(models.Model):
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время посещения"
    )
    pos = models.ForeignKey(
        POS,
        verbose_name="Торговая точка",
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    lat = models.FloatField(
        verbose_name="Широта/Latitude",
        blank=False,
        null=False
    )
    long = models.FloatField(
        verbose_name="Долгота/longitude",
        blank=False,
        null=False
    )

    class Meta:
        ordering = ("date",)
        verbose_name = "Посещение"
        verbose_name_plural = "Посещения"

    def __str__(self):
        return f"{self.pos.pos_name} {self.pos.worker.name}"