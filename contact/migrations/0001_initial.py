from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('contact_message', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('replied', models.BooleanField(default=False)),
            ],
        ),
    ]
