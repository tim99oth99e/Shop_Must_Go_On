from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class City(models.Model):
    city_name = models.CharField(max_length=200)

    def __str__(self):
        return self.city_name


class Shop(models.Model):
    shop_name = models.CharField(verbose_name="Nom du commerce", max_length=200)
    shop_website_link = models.URLField(verbose_name="Lien du site web", max_length=300, blank=True, null=True)
    shop_image = models.ImageField(verbose_name="Image", default='shop_images/default_shop_image.jpg', upload_to='shop_images')
    shop_category = models.ForeignKey(Category, verbose_name="Catégorie", on_delete=models.CASCADE, null=True)  # change to null instead of cascade ?
    phone_number = PhoneNumberField(verbose_name="Numéro de téléphone", null=True, blank=True)
    email = models.EmailField(verbose_name="Adresse mail", null=True, blank=True)
    address = models.CharField(verbose_name="Adresse", max_length=200, null=True)  # ça doit être rempli : prouve que le magasin existe
    shop_city = models.ForeignKey(City, verbose_name="Ville", on_delete=models.CASCADE, null=True)  # change to null instead of cascade ?
    how_to_order = models.TextField(verbose_name="Comment commander chez vous ?", null=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.shop_name

    def get_absolute_url(self):
        return reverse('main_app-home')