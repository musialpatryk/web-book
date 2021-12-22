from django import forms


class RequestListForm(forms.Form):
    author_id = forms.IntegerField(widget=forms.NumberInput(attrs={'hidden': True}))
    accept = forms.NullBooleanField()

    def __init__(self, *args, author=None, **kwargs):
        super(RequestListForm, self).__init__(*args, **kwargs)
        if author:
            self.author = author
            self.fields['author_id'].initial = author.id