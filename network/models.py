from django.db import models


class NetworkNode(models.Model):
    """Модель звена в сети(поставщика)"""

    LEVEL_CHOICES = [
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    ]

    name = models.CharField(max_length=255, verbose_name="Название звена сети")
    contact_email = models.EmailField(unique=True, verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house_number = models.CharField(max_length=20, verbose_name="Номер дома")

    supplier_node = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="clients",
        verbose_name="Поставщик",
    )

    level = models.IntegerField(
        choices=LEVEL_CHOICES,
        verbose_name="Уровень в сети",
    )

    debt = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, verbose_name="Задолженность"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Звено в сети(поставщик)"
        verbose_name_plural = "Звенья в сети(поставщики)"
        ordering = ["-created_at"]  # Сортировка по дате создания (новые выше)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель продукта"""

    name = models.CharField(max_length=255, verbose_name="Название продукта")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")

    # Связь с узлом сети
    network_node = models.ManyToManyField(
        NetworkNode,
        related_name="products",
        verbose_name="Узел сети",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["-release_date"]  # Сортировка по дате создания (новые выше)

    def __str__(self):
        return f"{self.name} ({self.model})"
