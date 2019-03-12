from django.contrib import admin
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from protector.admin import PermissionOwnerInline, PermissionObjectInline, GenericGroupAdminMixin, RestrictedAdminMixin

from accounts.models import (
    Account,
    AccountGroup
)

from accounts.forms import AccountChangeForm, AccountCreationForm


class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    model = Account
    change_password_form = AdminPasswordChangeForm

    list_display = [
        'email',
        'is_superuser',
        'is_staff',
        'is_active',
        'first_name',
        'last_name',
        'birthday',
        'last_login',
        'creation_date',
        'modification_date',
    ]

    list_filter = (
        'is_superuser',
        'is_staff',
        'is_active',
    )

    fieldsets = (
        ('Personal info', {
            'fields': (
                'first_name',
                'last_name',
                'birthday',
            )}),

        ('Statuses',
         {'fields': (
             'is_superuser',
             'is_staff',
             'is_active',
         )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_staff',
                'is_active',
            )}
         ),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('last_name',)
    filter_horizontal = ()

    inlines = (
        PermissionOwnerInline,
    )


class GroupAccountAdmin(GenericGroupAdminMixin, RestrictedAdminMixin):
    list_display = ("__str__", "display_accounts")
    save_on_top = True

    inlines = (
        PermissionObjectInline,
    )

    def display_accounts(self, obj):
        links = []
        for accounts in obj.user_set.all():
            ct = ContentType.objects.get_for_model(accounts)
            rule_name = f"admin:{ct.app_label}_{ct.model}_change"
            url = reverse(rule_name, args=(accounts.id,))
            account_name = (f"{accounts.first_name} {accounts.last_name}".strip())
            links.append(f"""<a href="{url}" target="_blank">{account_name}</a>""")
        return mark_safe("<br />".join(links))

    display_accounts.allow_tags = True
    display_accounts.short_description = _("accounts")


admin.site.register(Account, AccountAdmin)
admin.site.register(AccountGroup, GroupAccountAdmin)
