from django import forms


class UserForm(forms.Form):
    username = forms.CharField(
        label='user名',
        max_length=200,
        required=True,
    )

    password = forms.CharField(
        label='パスワード',
        max_length=50,
        required=True,
    )
