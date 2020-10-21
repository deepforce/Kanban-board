# Generated by Django 3.1.2 on 2020-10-21 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_candidate_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='status',
            field=models.CharField(choices=[('Applied', 'Applied'), ('Phone Screen', 'Phone Screen'), ('On site', 'On site'), ('Offered', 'Offered'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Applied', max_length=30),
        ),
    ]