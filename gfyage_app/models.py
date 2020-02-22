from django.db import models

# Create your models here.
class Audio(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=20) #标题
    Date = models.DateField()   # 发表日期
    Creator = models.CharField(max_length=20) # 原创
    SongName = models.CharField(max_length=10)  # 歌曲名
    Lyricist = models.CharField(max_length=10,blank=True) # 作词者
    Compose = models.CharField(max_length=10,blank=True) # 作曲者
    Singer = models.CharField(max_length=10) # 演唱者
    Type = models.CharField(max_length=10) # 歌曲类型
    CopyRight = models.CharField(max_length=20) # 版权所属
    Location = models.CharField(max_length=10) # 演唱地点
    SingDate = models.CharField(max_length=20) # 演唱时间
    Accompany = models.CharField(max_length=20) # 伴奏
    CoverImage = models.ImageField(upload_to='audio', verbose_name='图片', null=True) # 封面图片
    Lyrics = models.TextField() # 歌词
    SingerIntro = models.TextField() # 演唱者介绍
    SongIntro = models.TextField() # 歌曲介绍
    Tag = models.CharField(max_length=20) # 页面最后的一个标签
    MusciPath = models.FileField(blank=True, upload_to='audio')


