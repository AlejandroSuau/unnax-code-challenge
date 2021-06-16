from django.db import migrations


def pre_populate_currencies(apps, schema_editor):
    """ Pre populate currencies database table """
    Currency = apps.get_model("account", "Currency")
    Currency.objects.create(name="EURO", abbreviation="EUR", symbol="€")
    Currency.objects.create(name="DOLLAR", abbreviation="USD", symbol="$")


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(pre_populate_currencies),
    ]

