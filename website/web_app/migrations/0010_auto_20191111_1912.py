# Generated by Django 2.2.5 on 2019-11-11 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0009_auto_20191111_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web_app.Recipe'),
        ),
    ]