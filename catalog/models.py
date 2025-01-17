from django.db import models

from users.models import User

NULLABLE = {"blank": "True", "null": "True"}


class Product(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта",
        help_text="Введите название продукта",
    )

    desk = models.CharField(
        max_length=100,
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
    )

    image = models.ImageField(
        upload_to="media/photo",
        blank=True,
        null=True,
        verbose_name="Изображение(превью)",
        help_text="Загрузите изображение продукта",
    )

    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите Категорию продукта",
        null=True,
        blank=True,
        related_name="products",
    )

    price = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Цена за покупку",
        help_text="Введите Цену за покупку продукта",
    )

    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания(записи в БД)",
        help_text="Введите Дату создания продукта",
    )

    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения(записи в БД)",
        help_text="Введите Дату последнего изменения продукта",
    )

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        verbose_name='Пользователь',
        help_text='Укажите владельца продукта', **NULLABLE
    )

    published = models.BooleanField(default=False, verbose_name='опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "title"]
        permissions = [
            ("can_canceled_public", "может отменять публикацию продукта"),
            ("can_edit_desk", "может менять описание любого продукта"),
            ("can_edit_category", "может менять категорию любого продукта")
        ]


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите название категории",
    )

    desk = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание категории"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="заголовок")
    slug = models.CharField(max_length=150, verbose_name='URL', **NULLABLE)
    content = models.TextField(verbose_name="содержимое", **NULLABLE)
    preview = models.ImageField(upload_to="media/photo", **NULLABLE)
    created_at = models.DateField(auto_created=True, verbose_name="дата создания")
    published = models.BooleanField(default=True, verbose_name='опубликован')
    views = models.IntegerField(default=0, verbose_name='количество просмотров')
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,verbose_name='Пользователь',
                             help_text='Укажите владельца продукта', **NULLABLE
            )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        permissions = [
            ("can_edit", "может редактировать блог")
        ]


class Version(models.Model):
    product = models.ForeignKey(
        Product, related_name="Версия", verbose_name="Продукт",
        on_delete=models.CASCADE, **NULLABLE)

    version_num = models.IntegerField(
        verbose_name="Номер версии", **NULLABLE)

    version_title = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта")

    current_version = models.BooleanField(default=True, verbose_name="Признак текущей версии")

    def __str__(self):
        return f"{self.product} {self.version_num} {self.version_title}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["version_num", "product"]
