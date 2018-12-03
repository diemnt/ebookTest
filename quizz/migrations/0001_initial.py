# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-30 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('content', models.TextField(verbose_name='Content')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Is correct')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quizz_answer_created_by', to='staff.Staff')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quizz_answer_modified_by', to='staff.Staff')),
            ],
            options={
                'verbose_name': 'Answer',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('content', models.TextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Question',
            },
        ),
        migrations.CreateModel(
            name='QuestionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Decription')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='childrens', to='quizz.QuestionCategory')),
            ],
            options={
                'verbose_name': 'Question Category',
            },
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Decription')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quizz_quizz_created_by', to='staff.Staff')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quizz_quizz_modified_by', to='staff.Staff')),
            ],
            options={
                'verbose_name': 'Quizz',
            },
        ),
        migrations.CreateModel(
            name='QuizzQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.Question')),
                ('quizz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.Quizz')),
            ],
            options={
                'verbose_name': 'Quizz Question',
            },
        ),
        migrations.AddField(
            model_name='quizz',
            name='questions',
            field=models.ManyToManyField(blank=True, through='quizz.QuizzQuestion', to='quizz.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_category_rel', to='quizz.QuestionCategory'),
        ),
        migrations.AddField(
            model_name='question',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quizz_question_created_by', to='staff.Staff'),
        ),
        migrations.AddField(
            model_name='question',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quizz_question_modified_by', to='staff.Staff'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quizz.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='quizzquestion',
            unique_together=set([('quizz', 'question')]),
        ),
    ]
