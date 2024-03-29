# Generated by Django 2.2.3 on 2019-07-30 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('genre', models.IntegerField(choices=[(1, 'Horror'), (2, 'Fantasy'), (3, 'Mystery'), (4, 'Biography'), (5, 'Romance'), (6, 'Self Help'), (7, 'Text Book')])),
                ('language', models.IntegerField(choices=[(1, 'English'), (2, 'Spanish'), (3, 'French'), (4, 'German'), (5, 'Chinese'), (6, 'Japanese')])),
                ('publication_date', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='users.User')),
            ],
        ),
    ]
