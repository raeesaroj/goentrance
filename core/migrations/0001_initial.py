# Generated by Django 2.0.7 on 2018-07-07 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct', models.BooleanField(default=False)),
                ('answer', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'Past Questions'), (1, 'Mock Sets')], default=0)),
                ('name', models.CharField(max_length=64)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets', to='core.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='QuickNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('notes', models.TextField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quicknotes', to='core.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='core.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabus', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='core.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='core.Chapter')),
            ],
        ),
        migrations.AddField(
            model_name='syllabus',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='syllabuslist', to='core.Unit'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='core.QuestionSet'),
        ),
        migrations.AddField(
            model_name='options',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='core.Question'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='core.Unit'),
        ),
    ]
