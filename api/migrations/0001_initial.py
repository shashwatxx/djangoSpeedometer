# Generated by Django 2.2.4 on 2019-09-01 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReadSpeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TIMESTAMP', models.DateTimeField(auto_now_add=True)),
                ('STUDENT_NAME', models.CharField(max_length=200)),
                ('SUBJECT_NAME', models.CharField(max_length=200)),
            ],
        ),
    ]
