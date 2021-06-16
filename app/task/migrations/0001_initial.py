# Generated by Django 3.2 on 2021-06-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celery_task_id', models.UUIDField(db_index=True, unique=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('DONE', 'Done'), ('ERROR', 'Error')], default='PENDING', max_length=15)),
            ],
        ),
    ]
