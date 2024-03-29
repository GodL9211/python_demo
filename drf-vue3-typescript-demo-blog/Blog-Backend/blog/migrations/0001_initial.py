# Generated by Django 2.2.23 on 2021-08-18 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.IntegerField(null=True, verbose_name='creator')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modifier', models.IntegerField(null=True, verbose_name='modifier')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='文章标题')),
                ('cover', models.TextField(max_length=1000, verbose_name='封面')),
                ('excerpt', models.CharField(blank=True, max_length=200, verbose_name='摘要')),
                ('keyword', models.CharField(blank=True, max_length=200, verbose_name='关键词')),
                ('markdown', models.TextField(max_length=100000, verbose_name='正文')),
                ('status', models.CharField(choices=[('Draft', '草稿'), ('Published', '已发布'), ('Deleted', '已删除')], default='Draft', max_length=30, verbose_name='文章状态')),
                ('views', models.PositiveIntegerField(default=0, editable=False, verbose_name='浏览量')),
                ('comments', models.PositiveIntegerField(default=0, editable=False, verbose_name='评论数量')),
                ('likes', models.PositiveIntegerField(default=0, editable=False, verbose_name='点赞量')),
                ('words', models.PositiveIntegerField(default=0, editable=False, verbose_name='字数')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'db_table': 'blog_article',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.IntegerField(null=True, verbose_name='creator')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modifier', models.IntegerField(null=True, verbose_name='modifier')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('email', models.EmailField(max_length=100, verbose_name='邮箱')),
                ('content', models.TextField(max_length=10000, verbose_name='内容')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='手机')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='姓名')),
            ],
            options={
                'db_table': 'blog_message',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.IntegerField(null=True, verbose_name='creator')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modifier', models.IntegerField(null=True, verbose_name='modifier')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='标签名称')),
            ],
            options={
                'db_table': 'blog_tag',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.IntegerField(null=True, verbose_name='creator')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modifier', models.IntegerField(null=True, verbose_name='modifier')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='article_likes', to='blog.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='like_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'blog_like',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.IntegerField(null=True, verbose_name='creator')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modifier', models.IntegerField(null=True, verbose_name='modifier')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('content', models.TextField(max_length=10000, verbose_name='评论')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='article_comments', to='blog.Article', verbose_name='评论文章')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_reply', to='blog.Comment', verbose_name='评论回复')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comment_users', to=settings.AUTH_USER_MODEL, verbose_name='评论者')),
            ],
            options={
                'db_table': 'blog_comment',
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.IntegerField(null=True, verbose_name='creator')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modifier', models.IntegerField(null=True, verbose_name='modifier')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='分类名称')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.Catalog')),
            ],
            options={
                'db_table': 'blog_catalog',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='catalog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cls_articles', to='blog.Catalog', verbose_name='所属分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tag_articles', to='blog.Tag', verbose_name='文章标签'),
        ),
    ]
