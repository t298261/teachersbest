# Generated by Django 4.0.6 on 2022-12-06 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arg_essay', '0002_supports_user_thesis_user_userquestion_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thesis',
            name='claim',
        ),
        migrations.AddField(
            model_name='thesis',
            name='declarative',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='supports',
            name='support_one',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='supports',
            name='support_three',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='supports',
            name='support_two',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userquestion',
            name='question',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
