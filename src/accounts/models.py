from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _

from protector.managers import PermissionedManager
from protector.models import UserGenericPermsMixin, AbstractGenericGroup, Restricted
from protector.querysets import GenericGroupQuerySet, RestrictedQuerySet


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class RestrictedGroupQuerySet(GenericGroupQuerySet, RestrictedQuerySet):
    pass


RestrictedGroupManager = models.Manager.from_queryset(RestrictedGroupQuerySet)


class AccountGroup(AbstractGenericGroup, Restricted):
    name = models.CharField(max_length=100)
    objects = RestrictedGroupManager()
    by_perm = PermissionedManager()

    class Meta:
        verbose_name = 'Account Group'


class Account(
    UserGenericPermsMixin,
    AbstractBaseUser,
    # PermissionsMixin,
):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        _('email address'),
        unique=True,
        max_length=255,
        db_index=True
    )
    password = models.CharField(
        _('password'),
        max_length=255
    )

    first_name = models.CharField(
        _('first name'),
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        _('last name'),
        max_length=30,
        blank=True
    )
    birthday = models.DateField(
        _('birthday'),
        null=True
    )

    creation_date = models.DateTimeField(
        _('creation date'),
        auto_now_add=True
    )
    modification_date = models.DateTimeField(
        _('modification date'),
        auto_now_add=True
    )
    last_login = models.DateTimeField(
        _('last login'),
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        _('active status'),
        default=True  # TODO: default false until email verification
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=True  # TODO: default false
    )

    # avatar = models.ImageField(
    #     upload_to='/',  # TODO: fix it
    #     null=True,
    #     blank=True
    # )

    objects = AccountManager()

    class Meta:
        verbose_name = _('accounts')
        verbose_name_plural = _('accounts')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email
