# Generated by Django 3.1.3 on 2022-01-05 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='상품명')),
                ('description', models.TextField(verbose_name='상품설명')),
                ('price', models.IntegerField(verbose_name='상품가격')),
                ('stuck', models.IntegerField(verbose_name='재고')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('status', models.CharField(choices=[('sale', 'sale'), ('품절', 'out of stock')], default='sale', max_length=32, verbose_name='상태')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.shop', verbose_name='쇼핑몰')),
            ],
            options={
                'verbose_name': '상품',
                'verbose_name_plural': '상품',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductOptionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionGroup', models.CharField(max_length=256, verbose_name='옵션그룹')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOptionGroupItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionItem', models.CharField(max_length=256, verbose_name='옵션내용')),
                ('addPrice', models.IntegerField(default=0, verbose_name='추가 가격')),
                ('productOptionGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productoptiongroup')),
            ],
        ),
    ]