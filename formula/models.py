from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime

# GENERAL FIELD LIMIT
NAME_MAX_LENGTH = 64
DESC_MAX_LENGTH = 512

class SlugMixin(models.Model):
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class StrMixin(models.Model):
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True


class Category(SlugMixin, StrMixin, models.Model):
    class Parent(str):    
        CHOICES = [
            (GENERAL := "GE", "General"),
            (OPERATION := "OP", "Operations"),
            (EVEHICLE := "EV", "Electric Vehicle"),
        ]

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    description = models.CharField(max_length=DESC_MAX_LENGTH)
    forum_has = models.IntegerField(default=0)
    date_added = models.DateTimeField(null=True)
    parent = models.CharField(max_length=NAME_MAX_LENGTH, choices=Parent.CHOICES, default = Parent.GENERAL)


    class Meta:
        verbose_name_plural = 'Categories'

    

class Topic(SlugMixin, StrMixin, models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    description = models.CharField(max_length=DESC_MAX_LENGTH)
    category_has = models.IntegerField(default=0)
    date_added = models.DateTimeField()
    category = models.ForeignKey(Category, related_name='topics', on_delete=models.CASCADE)

    

class Post(StrMixin, models.Model):
    CONTENT_MAX_LENGTH = 8192
    FILES_MAX_LENGTH = 512

    name = models.CharField(max_length=NAME_MAX_LENGTH)
    description = models.CharField(max_length=DESC_MAX_LENGTH)
    content = models.CharField(max_length=CONTENT_MAX_LENGTH)
# comment: use FileField() here?
    file = models.CharField(max_length=FILES_MAX_LENGTH)
# comment end
    viewership = models.IntegerField(default=0)
    topic_has = models.IntegerField(default=0)
    date_added = models.DateTimeField()
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(StrMixin, models.Model):
    student_id = models.IntegerField(unique=True, null=False, default=0)
    first_name = models.CharField(max_length=NAME_MAX_LENGTH)
    last_name = models.CharField(max_length=NAME_MAX_LENGTH)
# comment: upload_to is null
    """picture = models.ImageField()"""
    picture = models.CharField(max_length=NAME_MAX_LENGTH)
# comment end
    bio = models.CharField(max_length=DESC_MAX_LENGTH)
    admin = models.BooleanField(default=False)


class Team(StrMixin, models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    description = models.CharField(max_length=DESC_MAX_LENGTH)


class TeamLead(StrMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    leader = models.BooleanField(default=False)
    topic_access = models.ManyToManyField(Topic, related_name="access")

    class Meta:
        db_table = "Team Lead"


class TeamMember(StrMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        db_table = "Team Member"
