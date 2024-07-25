from django.db import models

NULLABLE = {"blank": True, "null": True}
DECIMAL = {"max_digits": 10, "decimal_places": 2}


class NetworkNode(models.Model):
    """Модель для составляющей сети"""

    LEVEL_CHOICES = [(0, "Завод"), (1, "Розничная сеть"), (2, "Индивидуальный предприниматель")]

    name = models.CharField(max_length=150, verbose_name="Название")
    level = models.PositiveIntegerField(choices=LEVEL_CHOICES, verbose_name="Уровень звена")
    supplier = models.ForeignKey("self", related_name="customer", on_delete=models.SET_NULL, **NULLABLE)
    debt = models.DecimalField(**DECIMAL, default=0, verbose_name="Задолженность перед поставщиком")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f"{self.name} - {self.supplier} - {self.debt}"

    class Meta:
        verbose_name = "звено сети"
        verbose_name_plural = "звенья сети"


class Contact(models.Model):
    """Модель для контактов"""

    email = models.EmailField(max_length=100, verbose_name="Электронная почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.IntegerField(verbose_name="Номер дома")

    network_node = models.OneToOneField(
        NetworkNode, related_name="contact", on_delete=models.CASCADE, verbose_name="Звено сети"
    )

    def __str__(self):
        return f"{self.email} - {self.country}, {self.city}, {self.street}, {self.house_number}"

    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"


class Product(models.Model):
    """Модель для продукта"""

    title = models.CharField(max_length=100, verbose_name="Название")
    model = models.CharField(max_length=100, verbose_name="Модель")
    on_market = models.DateField(verbose_name="Дата выхода на рынок")

    network_node = models.ForeignKey(
        NetworkNode, related_name="products", on_delete=models.CASCADE, verbose_name="Звено сети"
    )

    def __str__(self):
        return f"{self.title} ({self.model}) - {self.on_market}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
