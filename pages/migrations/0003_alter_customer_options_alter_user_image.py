# Generated by Django 4.1.7 on 2023-03-25 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_company_rename_customer_address_customer_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['-EnterDate']},
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='std_prof_Img.png', upload_to='photos/%y/%m/%d'),
        ),
    ]
