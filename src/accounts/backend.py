from django.contrib.auth.backends import ModelBackend
from protector.backends import GenericPermissionBackend


class AccountBackend(
    GenericPermissionBackend,
    ModelBackend
):
    pass
