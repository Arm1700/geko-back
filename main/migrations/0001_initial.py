# Generated by Django 5.0.4 on 2024-11-15 15:29

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
                ('local_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_url', models.URLField(blank=True, max_length=255, null=True)),
                ('order', models.PositiveIntegerField(blank=True, default=0, null=True)),
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
                ('hour', models.CharField(max_length=50)),
                ('month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_gallery_photos/')),
                ('order', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('status', models.CharField(choices=[('upcoming', 'Upcoming'), ('happening', 'Happening'), ('completed', 'Completed')], max_length=20)),
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
                ('local_image', models.ImageField(blank=True, null=True, upload_to='lesson_images/')),
                ('image_url', models.URLField(blank=True, default='https://eduma.thimpress.com/wp-content/uploads/2022/07/thumnail-cate-7-170x170.png', max_length=255, null=True)),
                ('order', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_image', models.ImageField(blank=True, null=True, upload_to='review_images/')),
                ('image_url', models.URLField(blank=True, default='https://eduma.thimpress.com/wp-content/uploads/2022/07/thumnail-cate-7-170x170.png', max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_image', models.ImageField(blank=True, null=True, upload_to='team_images/')),
                ('image_url', models.URLField(blank=True, default='https://eduma.thimpress.com/wp-content/uploads/2022/07/thumnail-cate-7-170x170.png', max_length=255, null=True)),
                ('order', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('country', models.CharField(max_length=255)),
                ('whatsapp', models.CharField(max_length=20)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='EventGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='event_gallery_photos/')),
                ('order', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_galleries', to='main.event')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='PopularCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_url', models.URLField(blank=True, max_length=255, null=True)),
                ('duration', models.CharField(max_length=50)),
                ('certification', models.TextField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes')),
                ('students', models.TextField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes')),
                ('studentGroup', models.TextField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes')),
                ('assessments', models.TextField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes')),
                ('order', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='EventTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(default='Default place', max_length=255)),
                ('title', models.CharField(default='Default title', max_length=255)),
                ('description', models.CharField(default='Default description', max_length=255)),
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
                ('text', models.CharField(default='Default text', max_length=255)),
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
                ('title', models.CharField(default='Default title', max_length=255)),
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
                ('lang', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.language')),
                ('popular_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.popularcourse')),
            ],
            options={
                'unique_together': {('popular_course', 'language')},
            },
        ),
        migrations.CreateModel(
            name='TeamTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(default='Default desc')),
                ('name', models.CharField(default='Default name', max_length=255)),
                ('role', models.CharField(default='Default role', max_length=255)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.language')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.team')),
            ],
            options={
                'unique_together': {('team', 'language')},
            },
        ),
    ]
