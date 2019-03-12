import uuid

from accounts.models import Account
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class BaseProjectAppClass(models.Model):
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


class BaseClass(BaseProjectAppClass):
    class Meta:
        abstract = True

    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        max_length=30
    )
    descriptions = models.TextField(
        max_length=2000
    )

    def __str__(self):
        return self.name


class Status(BaseClass):
    class Meta:
        verbose_name = _('status')
        verbose_name_plural = _('statuses')

    is_active = models.BooleanField(
        default=True
    )


class Project(BaseClass):
    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')

    project_manager = models.ForeignKey(
        to=Account,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        verbose_name='project manager',
        related_name='managers'
    )

    project_status = models.ForeignKey(
        to=Status,
        on_delete=models.SET('undefined'),
        blank=False,
        null=False,
        verbose_name='project status',
        related_name='projects',
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

    task_project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='project',
        related_name='tasks'
    )

    task_status = models.ForeignKey(
        to=Status,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='task status',
        related_name='tasks',
    )

    task_staff = models.ManyToManyField(
        to=Account,
        blank=False,
        verbose_name='task staff',
    )
    task_result_url = models.URLField(

    )

    task_price = models.FloatField(

    )

    # TODO: Поля - Стоимость, Исполнитель, Комментарии,

    def get_absolute_url(self):
        return reverse('projects:task_detail',
                       args=[
                           self.slug
                       ])


class Message(BaseProjectAppClass):
    message_author = models.ForeignKey(
        to=Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='comment_author',
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='task'

    )

    def get_absolute_url(self):
        return reverse('projects:message_detail',
                       args=[
                           self.slug
                       ])

    def __str__(self):
        return '{} about {}'.format(self.message_author.get_full_name, self.task.name)
