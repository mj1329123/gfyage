from django.db import models


# Create your models here.
class Audio(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField('标题', max_length=20)  # 标题
    Date = models.DateField('时间')   # 发表日期
    Creator = models.CharField('原创', max_length=20)  # 原创
    SongName = models.CharField('歌曲名', max_length=10)  # 歌曲名
    Lyricist = models.CharField('作词者', max_length=10, blank=True)  # 作词者
    Compose = models.CharField('作曲者', max_length=10, blank=True)  # 作曲者
    Singer = models.CharField('演唱者', max_length=10)  # 演唱者
    Type = models.CharField('歌曲类型', max_length=10)  # 歌曲类型
    CopyRight = models.CharField('版权所属', max_length=20)  # 版权所属
    Location = models.CharField('演唱地点', max_length=10)  # 演唱地点
    SingDate = models.CharField('演唱时间', max_length=20)  # 演唱时间
    Accompany = models.CharField('伴奏', max_length=20)  # 伴奏
    CoverImage = models.ImageField(upload_to='audio', verbose_name='图片', null=True)  # 封面图片
    Lyrics = models.TextField('歌词')  # 歌词
    SingerIntro = models.TextField('演唱者介绍')  # 演唱者介绍
    SongIntro = models.TextField('歌曲介绍')  # 歌曲介绍
    Tag = models.CharField('标签', max_length=20)  # 页面最后的一个标签
    MusciPath = models.FileField('上传音频', blank=True, upload_to='audio')

    class Meta:
        verbose_name = '音频'
        verbose_name_plural = verbose_name


