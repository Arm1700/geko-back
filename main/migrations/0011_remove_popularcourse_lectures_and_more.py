# Generated by Django 5.0.4 on 2024-11-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_team_teamtranslation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popularcourse',
            name='lectures',
        ),
        migrations.RemoveField(
            model_name='popularcourse',
            name='quizzes',
        ),
        migrations.RemoveField(
            model_name='popularcoursetranslation',
            name='assessments',
        ),
        migrations.RemoveField(
            model_name='popularcoursetranslation',
            name='certification',
        ),
        migrations.RemoveField(
            model_name='popularcoursetranslation',
            name='skill_level',
        ),
        migrations.AddField(
            model_name='popularcourse',
            name='assessments',
            field=models.TextField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes'),
        ),
        migrations.AddField(
            model_name='popularcourse',
            name='certification',
            field=models.TextField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes'),
        ),
        migrations.AddField(
            model_name='popularcourse',
            name='studentGroup',
            field=models.TextField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes'),
        ),
        migrations.AlterField(
            model_name='popularcourse',
            name='students',
            field=models.TextField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes'),
        ),
    ]
