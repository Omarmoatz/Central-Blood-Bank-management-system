# Generated by Django 5.1.8 on 2025-04-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0002_alter_donor_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='city',
            field=models.CharField(choices=[('Cairo', 'Cairo'), ('Mansoura', 'Mansoura'), ('Tanta', 'Tanta'), ('Alexandria', 'Alexandria'), ('Zagazig', 'Zagazig'), ('Benha', 'Benha'), ('Damietta', 'Damietta'), ('Ismailia', 'Ismailia'), ('Suez', 'Suez'), ('Port Said', 'Port Said')], max_length=50),
        ),
    ]
