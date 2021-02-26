# Generated by Django 2.2.4 on 2019-09-01 21:05

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='readspeed',
            name='AS_PER',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(200)], verbose_name='NO OF HOURS REQUIRED AS PER YOU'),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='AVERAGE_READING',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)], verbose_name='AVG TIME READING PER PAGE (IN MINS)'),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='CHECKING_LEVEL',
            field=models.CharField(choices=[('Strict', 'Strict'), ('Normal', 'Normal'), ('Lenient', 'Lenient')], default='Normal', max_length=200),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='CURRENT_STATUS',
            field=models.IntegerField(choices=[(0, 0), (1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60), (7, 70), (8, 80), (9, 90), (10, 100)], default=0, verbose_name='CURRENT STATUS IN %'),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='DESIRED_NUMBER',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='DESIRED MARKS'),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='DUE_DATE',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='EDUCATION_TYPE',
            field=models.CharField(choices=[('School', 'School'), ('Graduation', 'Graduation'), ('Post Graduation', 'Post Graduation')], default='Graduation', max_length=200),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='INTEREST_LEVEL',
            field=models.CharField(choices=[('Very Interesting', 'Very Interesting'), ('Interesting', 'Interesting'), ('Normal', 'Normal'), ('Boring', 'Boring')], default='Interesting', max_length=200),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='MARKS_IN',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='PREVIOUS MARKS IN SAME OR SIMILAR SUBJECT'),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='NUMBER_OF',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0, verbose_name='NO OF REVISION'),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='PREFERRED_READING',
            field=models.CharField(choices=[('Notes', 'Notes'), ('Book', 'Book'), ('Video', 'Video'), ('Multiple', 'Multiple')], default='Notes', max_length=200, verbose_name='PREFERRED READING TYPE'),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='SEMESTER',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='SUBJECT_SYLLABUS',
            field=models.CharField(choices=[('Very Lengthy (800+ pages)', 'Very Lengthy (800+ pages)'), ('Lengthy (600+ pages)', 'Lengthy (600+ pages)'), ('Medium (400+ pages)', 'Medium (400+ pages)'), ('Short', 'Short')], default='Lengthy (600+ pages)', max_length=200),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='SUPPORTING_KNOWLEDGE',
            field=models.CharField(choices=[('None', 'None'), ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='TOUGHNESS_LEVEL',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], default='Medium', max_length=200),
        ),
        migrations.AddField(
            model_name='readspeed',
            name='TYPE_OF',
            field=models.CharField(choices=[('Theoritical', 'Theoritical'), ('Practical', 'Practical'), ('Numerical', 'Numerical'), ('Other', 'Other')], default='Theoritical', max_length=200, verbose_name='TYPE OF SUBJECT'),
        ),
    ]