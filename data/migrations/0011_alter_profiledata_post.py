# Generated by Django 4.2.17 on 2024-12-11 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_alter_post_user_alter_profiledata_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledata',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='data.post'),
            preserve_default=False,
        ),
    ]