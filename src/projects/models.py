import uuid

from accounts.models import Account
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


#TODO: Установить уникальные поля для исключения повторяющихся значений.
class CreateModificateAbstactClass(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    creation_timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='creation time',
        editable=False
    )

    modifications_timestamp = models.DateTimeField(
        auto_now=True,
        verbose_name='modification time',
        editable=False,
    )


class BaseClass(CreateModificateAbstactClass):
    class Meta:
        abstract = True

    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        max_length=30,
        blank=False,
        null=False
    )
    descriptions = models.TextField(
        max_length=2000
    )

    def __str__(self):
        return self.name


class Priority(BaseClass):
    class Meta:
        verbose_name = _('priority')
        verbose_name_plural = _('priorities')

    value = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Status(BaseClass):
    class Meta:
        verbose_name = _('status')
        verbose_name_plural = _('statuses')


class Url(CreateModificateAbstactClass):
    description = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    url = models.URLField(

    )

    def __str__(self):
        return self.description


class Brand(BaseClass):
    pass


class Project(BaseClass):
    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')

    brand = models.ForeignKey(
        to=Brand,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        verbose_name='brand',
        related_name='projects'
    )

    manager = models.ForeignKey(
        to=Account,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        verbose_name='project manager',
        related_name='projects'
    )

    status = models.ForeignKey(
        to=Status,
        on_delete=models.SET('undefined'),
        blank=False,
        null=False,
        verbose_name='project status',
        related_name='projects',
    )

    url = models.ManyToManyField(
        Url,
        blank=True,

    )

    def get_absolute_url(self):
        return reverse('projects:project_detail',
                       args=[
                           self.slug
                       ])


class Task(BaseClass, MPTTModel):
    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')

    class MPTTMeta:
        order_insertion_by = ['name']

    name = models.CharField(
        max_length=50,
        unique=True
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    personal = models.ForeignKey(
        to=Account,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        verbose_name='performer',
        related_name='tasks'
    )

    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='project',
        related_name='tasks',
    )

    status = models.ForeignKey(
        to=Status,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='status',
        related_name='tasks',
    )

    price = models.FloatField(
        blank=True,
        null=True,
        verbose_name='price',

    )
    url = models.ManyToManyField(
        Url,
        blank=True,

    )

    def get_absolute_url(self):
        return reverse('projects:task_detail',
                       args=[
                           self.slug
                       ])


class Message(CreateModificateAbstactClass):
    author = models.ForeignKey(
        to=Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='message author',
        related_name='messages'
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='messages'

    )
    text = models.TextField(
        max_length=1000
    )

    url = models.ManyToManyField(
        Url,
        blank=True
    )

    def get_absolute_url(self):
        return reverse('projects:task_detail',
                       args=[
                           self.task.slug
                       ])

    def __str__(self):
        return '{} about {}'.format(self.author.get_full_name, self.task.name)
