from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class AccountCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Подтверждение',
        widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароль и подтверждение не совпадают')
        return password2

    def save(self, commit=True):
        user = super(AccountCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'birthday')


class AccountChangeForm(forms.ModelForm):
    '''
    Форма для обновления данных пользователей. Нужна только для того, чтобы не
    видеть постоянных ошибок "Не заполнено поле password" при обновлении данных
    пользователя.
    '''
    password = ReadOnlyPasswordHashField(
        widget=forms.PasswordInput,
        required=False
    )

    def save(self, commit=True):
        user = super(AccountChangeForm, self).save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('email',)
