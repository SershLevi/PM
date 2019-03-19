import uuid

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from pm.settings import actual as settings


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
        max_length=50,
        blank=False,
        null=False,
        unique=True,
    )

    slug = models.SlugField(
        editable=False,
        unique=True
    )

    descriptions = models.TextField(
        max_length=2000,
    )

    def __str__(self):
        return self.name

    def save(self, **kwargs): #TODO: Улучшить проверку
        name = self.name
        name.strip()
        while ('  ' in name):
            name = name.replace('  ', ' ')
            print(name)
        self.name = name
        slug = self.name

        slug.strip().replace(' ', '-').lower()
        self.slug = slugify(slug)
        super(BaseClass, self).save()


class Status(BaseClass):
    class Meta:
        verbose_name = _('status')
        verbose_name_plural = _('statuses')

    def get_absolute_url(self):
        return reverse('projects:status_detail')


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

    def get_absolute_url(self):
        return reverse('projects:brand_detail',
                       args=[
                           self.slug
                       ])


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

    person = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        verbose_name='project manager',
        related_name='projects'
    )

    status = models.ForeignKey(
        to=Status,
        on_delete=models.CASCADE,
        blank=False,
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

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    person = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
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

    done_timestamp = models.DateTimeField(
        verbose_name='done time',
        editable=True,

    )
    to_pay_timestamp = models.DateTimeField(
        verbose_name='to pay time',
        editable=True,

    )

    priority = models.PositiveSmallIntegerField()

    def get_absolute_url(self):
        return reverse('projects:task_detail',
                       args=[
                           self.slug
                       ])


class Comment(CreateModificateAbstactClass):
    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        # ordering = ('-creation_timestamp')

    person = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='Comment author',
        related_name='comments'
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments'

    )
    text = models.TextField(
        max_length=1000
    )

    url = models.ManyToManyField(
        Url,
        blank=True
    )

    def __str__(self):
        return ' Comment by {} on {}'.format(self.person.get_full_name, self.task.name)
