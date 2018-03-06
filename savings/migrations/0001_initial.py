# Generated by Django 2.0.2 on 2018-02-20 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chama', '0004_auto_20180220_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Savings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chama.Member')),
            ],
            options={
                'verbose_name_plural': 'savings',
            },
        ),
        migrations.CreateModel(
            name='SavingsDeposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chama.Member')),
            ],
            options={
                'verbose_name_plural': 'Savings Purchase',
            },
        ),
        migrations.CreateModel(
            name='SavingsWithdrawal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chama.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('fixed', 'fixed'), ('contract', 'contract'), ('current', 'current'), ('target', 'target')], default='fixed', max_length=100)),
                ('interval', models.CharField(choices=[('year', 'per anum'), ('month', 'per month'), ('week', 'per week'), ('day', 'per day')], default='month', max_length=100)),
                ('min_amount', models.IntegerField()),
                ('max_amount', models.IntegerField()),
                ('compulsory', models.BooleanField(default=True)),
                ('interest_rate', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='savingswithdrawal',
            name='savings_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='savings.Type'),
        ),
        migrations.AddField(
            model_name='savingsdeposit',
            name='savings_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='savings.Type'),
        ),
        migrations.AddField(
            model_name='savings',
            name='savings_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='savings.Type'),
        ),
    ]