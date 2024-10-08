# Generated by Django 5.0.4 on 2024-09-17 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(blank=True, max_length=255, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=20)),
                ('hour', models.CharField(max_length=50)),
                ('image', models.JSONField()),
                ('status', models.CharField(choices=[('upcoming', 'Upcoming'), ('happening', 'Happening'), ('completed', 'Completed')], max_length=20)),
                ('total_slots', models.IntegerField()),
                ('booked_slots', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LessonInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50)),
                ('count', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PopularCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(blank=True, max_length=255, null=True)),
                ('lectures', models.IntegerField()),
                ('quizzes', models.IntegerField()),
                ('duration', models.CharField(max_length=50)),
                ('students', models.IntegerField()),
                ('price', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='EventTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.event')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.language')),
            ],
            options={
                'unique_together': {('event', 'language')},
            },
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.category')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.language')),
            ],
            options={
                'unique_together': {('category', 'language')},
            },
        ),
        migrations.CreateModel(
            name='LessonInfoTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.language')),
                ('lesson_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.lessoninfo')),
            ],
            options={
                'unique_together': {('lesson_info', 'language')},
            },
        ),
        migrations.CreateModel(
            name='PopularCourseTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('skill_level', models.CharField(max_length=50)),
                ('assessments', models.CharField(max_length=50)),
                ('lang', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('certification', models.TextField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.language')),
                ('popular_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.popularcourse')),
            ],
            options={
                'unique_together': {('popular_course', 'language')},
            },
        ),
        migrations.CreateModel(
            name='ReviewTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.language')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.review')),
            ],
            options={
                'unique_together': {('review', 'language')},
            },
        ),
    ]
