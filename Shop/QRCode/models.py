from django.db import models
from decimal import Decimal


class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.items.exists():
            food_items = [
                {"name": "قهوه اسپرسو", "description": "قهوه اسپرسو خالص", "price": Decimal('15.00')},
                {"name": "کاپوچینو", "description": "کاپوچینو با شیر داغ", "price": Decimal('20.00')},
                {"name": "لاته", "description": "لاته با شیر و فوم", "price": Decimal('25.00')},
                {"name": "چای سیاه", "description": "چای سیاه تازه", "price": Decimal('10.00')},
                {"name": "چای سبز", "description": "چای سبز طبیعی", "price": Decimal('12.00')},
                {"name": "نوشابه", "description": "نوشابه گازدار", "price": Decimal('8.00')},
                {"name": "آب معدنی", "description": "آب معدنی خنک", "price": Decimal('5.00')},
                {"name": "ساندویچ مرغ", "description": "ساندویچ مرغ گریل شده", "price": Decimal('30.00')},
                {"name": "ساندویچ ژامبون", "description": "ساندویچ ژامبون و پنیر", "price": Decimal('35.00')},
                {"name": "پیتزا مارگاریتا", "description": "پیتزا با پنیر و گوجه", "price": Decimal('50.00')},
                {"name": "پیتزا پپرونی", "description": "پیتزا با پپرونی و پنیر", "price": Decimal('55.00')},
                {"name": "سالاد سزار", "description": "سالاد سزار با سس مخصوص", "price": Decimal('40.00')},
                {"name": "پاستا Carbonara", "description": "پاستا با سس Carbonara", "price": Decimal('45.00')},
                {"name": "پاستا Bolognese", "description": "پاستا با سس Bolognese", "price": Decimal('48.00')},
                {"name": "کیک شکلاتی", "description": "کیک شکلاتی خوشمزه", "price": Decimal('25.00')},
                {"name": "چیزکیک", "description": "چیزکیک با توت فرنگی", "price": Decimal('30.00')},
                {"name": "مافین", "description": "مافین شکلاتی", "price": Decimal('15.00')},
                {"name": "بستنی وانیلی", "description": "بستنی وانیلی خامه‌ای", "price": Decimal('12.00')},
                {"name": "بستنی شکلاتی", "description": "بستنی شکلاتی خامه‌ای", "price": Decimal('12.00')},
                {"name": "بستنی توت فرنگی", "description": "بستنی توت فرنگی خامه‌ای", "price": Decimal('12.00')},
            ]

            for item in food_items:
                MenuItem.objects.create(
                    menu=self,
                    name=item['name'],
                    description=item['description'],
                    price=item['price']
                )


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
