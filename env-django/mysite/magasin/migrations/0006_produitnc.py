# Generated by Django 4.1.7 on 2023-03-14 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0005_produit_categorie_produit_fournisseur_produit_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduitNC',
            fields=[
                ('produit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='magasin.produit')),
                ('Duree_garantie', models.CharField(max_length=100)),
            ],
            bases=('magasin.produit',),
        ),
    ]
