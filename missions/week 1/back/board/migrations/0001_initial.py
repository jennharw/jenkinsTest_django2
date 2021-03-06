# Generated by Django 3.1.3 on 2022-01-06 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mall', '0002_auto_20220105_1030'),
        ('product', '0004_auto_20220106_0138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='답변')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('상품질문', 'product'), ('배송관련', 'delivery')], default='productQuestion', max_length=32, verbose_name='질문 카테고리')),
                ('title', models.CharField(max_length=256, verbose_name='질문제목')),
                ('description', models.TextField(verbose_name='상품질문')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='상품')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.shop', verbose_name='쇼핑몰')),
            ],
        ),
    ]
