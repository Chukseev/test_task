from django.db import migrations

def seed_products(apps, schema_editor):
    Category = apps.get_model("mainapp", "Category")
    Product = apps.get_model("mainapp", "Product")

    hol = Category.objects.get(name="Холодильники")
    st = Category.objects.get(name="Стиральные машины")
    tv = Category.objects.get(name="Телевизоры")
    nb17 = Category.objects.get(name='17"')
    nb19 = Category.objects.get(name='19"')

    Product.objects.create(name="LG Холодильник двухкамерный", price=19990, quantity=10, category=hol)
    Product.objects.create(name="Samsung Стиральная машина", price=15990, quantity=5, category=st)
    Product.objects.create(name="Sony Телевизор 42\"", price=25990, quantity=3, category=tv)
    Product.objects.create(name="Lenovo Ноутбук 17\"", price=39990, quantity=7, category=nb17)
    Product.objects.create(name="Asus Ноутбук 19\"", price=45990, quantity=4, category=nb19)

def unseed_products(apps, schema_editor):
    Product = apps.get_model("mainapp", "Product")
    Product.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0002_seed_categories"),
    ]
    operations = [
        migrations.RunPython(seed_products, unseed_products),
    ]
