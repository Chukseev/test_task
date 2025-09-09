from django.db import migrations

def seed_categories(apps, schema_editor):
    Category = apps.get_model("mainapp", "Category")

    bt = Category.objects.create(name="Бытовая техника")
    comp = Category.objects.create(name="Компьютеры")

    st = Category.objects.create(name="Стиральные машины", parent=bt)
    hol = Category.objects.create(name="Холодильники", parent=bt)
    tv = Category.objects.create(name="Телевизоры", parent=bt)

    Category.objects.create(name="однокамерные", parent=hol)
    Category.objects.create(name="двухкамерные", parent=hol)

    nb = Category.objects.create(name="Ноутбуки", parent=comp)
    Category.objects.create(name="Моноблоки", parent=comp)

    Category.objects.create(name='17"', parent=nb)
    Category.objects.create(name='19"', parent=nb)


def unseed_categories(apps, schema_editor):
    Category = apps.get_model("mainapp", "Category")
    Category.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_categories, unseed_categories),
    ]
