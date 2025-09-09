from django.db import migrations

def seed_data(apps, schema_editor):
    Client = apps.get_model("mainapp", "Client")
    Category = apps.get_model("mainapp", "Category")
    Product = apps.get_model("mainapp", "Product")
    Order = apps.get_model("mainapp", "Order")
    OrderItem = apps.get_model("mainapp", "OrderItem")

    clients = [
        Client.objects.create(name="Иванов Иван"),
        Client.objects.create(name="Петров Петр"),
        Client.objects.create(name="Сидорова Анна"),
        Client.objects.create(name="Smith John"),
        Client.objects.create(name="Doe JaneDA"),
    ]

    electronics = Category.objects.create(name="Электроника")
    home = Category.objects.create(name="Товары для дома")
    phones = Category.objects.create(name="Смартфоны", parent=electronics)
    tvs = Category.objects.create(name="Телевизоры", parent=electronics)
    kitchen = Category.objects.create(name="Кухонная техника", parent=home)

    products = {
        "iPhone 15": Product.objects.create(name="iPhone 15", category=phones, price=1000, quantity=20),
        "Samsung Galaxy": Product.objects.create(name="Samsung Galaxy", category=phones, price=800, quantity=30),
        "LG OLED TV": Product.objects.create(name="LG OLED TV", category=tvs, price=1500, quantity=10),
        "Sony Bravia": Product.objects.create(name="Sony Bravia", category=tvs, price=1200, quantity=12),
        "Холодильник Bosch": Product.objects.create(name="Холодильник Bosch", category=kitchen, price=600, quantity=15),
        "Микроволновка Samsung": Product.objects.create(name="Микроволновка Samsung", category=kitchen, price=200, quantity=25),
        "Чайник Philips": Product.objects.create(name="Чайник Philips", category=kitchen, price=50, quantity=40),
    }

    order1 = Order.objects.create(client=clients[0])  # Иванов
    order2 = Order.objects.create(client=clients[1])  # Петров
    order3 = Order.objects.create(client=clients[2])  # Сидорова
    order4 = Order.objects.create(client=clients[3])  # Smith
    order5 = Order.objects.create(client=clients[4])  # Jane

    OrderItem.objects.create(order=order1, product=products["iPhone 15"], quantity=2, price=1000)
    OrderItem.objects.create(order=order1, product=products["Чайник Philips"], quantity=3, price=50)

    OrderItem.objects.create(order=order2, product=products["Samsung Galaxy"], quantity=1, price=800)
    OrderItem.objects.create(order=order2, product=products["LG OLED TV"], quantity=1, price=1500)

    OrderItem.objects.create(order=order3, product=products["Sony Bravia"], quantity=2, price=1200)
    OrderItem.objects.create(order=order3, product=products["Холодильник Bosch"], quantity=1, price=600)

    OrderItem.objects.create(order=order4, product=products["iPhone 15"], quantity=1, price=1000)
    OrderItem.objects.create(order=order4, product=products["Samsung Galaxy"], quantity=2, price=800)

    OrderItem.objects.create(order=order5, product=products["Микроволновка Samsung"], quantity=4, price=200)
    OrderItem.objects.create(order=order5, product=products["Чайник Philips"], quantity=5, price=50)


def unseed_data(apps, schema_editor):
    Client = apps.get_model("mainapp", "Client")
    Category = apps.get_model("mainapp", "Category")
    Product = apps.get_model("mainapp", "Product")
    Order = apps.get_model("mainapp", "Order")
    OrderItem = apps.get_model("mainapp", "OrderItem")

    OrderItem.objects.all().delete()
    Order.objects.all().delete()
    Product.objects.all().delete()
    Category.objects.all().delete()
    Client.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0003_seed_products"),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]
