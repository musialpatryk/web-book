from django import forms
from role_requests.models import RoleRequest


class RoleRequestForm(forms.Form):

    placeholders = {
        'message': 'Powód dla którego chcesz zostać moderatorem'
    }
    message = forms.CharField(max_length=255)

    # role = forms.IntegerField(default = RoleRequest.ROLE_REQUEST_ADMIN)

    def __init__(self, *args, book=None, **kwargs):
        super(RoleRequestForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control mb-2',
            })

            if field in self.placeholders:
                self.fields[field].widget.attrs.update({
                    'placeholder': self.placeholders[field],
                })