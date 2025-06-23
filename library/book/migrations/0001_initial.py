
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'), 
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, blank=True, unique=True)),
                ('description', models.CharField(max_length=256, blank=True)),
                ('count', models.IntegerField(default=10)),
                ('image', models.ImageField(upload_to='book_covers/', blank=True, null=True)),
                ('authors', models.ManyToManyField(to='author.Author', related_name='books')),
            ],
        ),
    ]
