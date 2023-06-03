# Generated by Django 4.1.9 on 2023-05-30 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashAquaponia', '0005_alter_usermodel_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='dashmodel',
            name='limpezaAgua',
            field=models.CharField(max_length=40, verbose_name='LimpezaAgua'),
        ),
        migrations.AlterField(
            model_name='dashmodel',
            name='peixeMorto',
            field=models.CharField(max_length=40, verbose_name='PeixeMorto'),
        ),
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]