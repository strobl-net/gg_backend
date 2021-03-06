# Generated by Django 3.0.3 on 2020-04-21 00:46

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('surveys', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', django.contrib.postgres.fields.jsonb.JSONField()),
                ('answered', models.DateTimeField(default=django.utils.timezone.now)),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='surveys.Survey')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
