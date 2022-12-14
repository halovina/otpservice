# Generated by Django 4.1.2 on 2022-10-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Otpservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=35)),
                ('otp_number', models.IntegerField()),
                ('expired_unixtime', models.IntegerField()),
                ('validate', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
