from django import forms


class AuthorRequestForm(forms.Form):
    placeholders = {
        'name': 'Imie i nazwisko',
        'description': 'Opis',
        'birthDate': 'Data urodzenia',
        'slug': 'Pseudonim',
        'rating': 'Ocena'
    }

    name = forms.CharField(
        max_length=200,
    )
    genre = forms.ChoiceField(
        choices=(),
    )
    description = forms.CharField(
        widget=forms.Textarea()
    )
    birthDate = forms.DateField(
        input_formats='%Y-%m-%d',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    slug = forms.CharField(
        max_length=100,
    )
    rating = forms.IntegerField(
        max_value=5,
    )
    image = forms.ImageField()

    def __init__(self, *args, genre=None, **kwargs):
        super(AuthorRequestForm, self).__init__(*args, **kwargs)
        if genre:
            self.fields['genre'].choices = genre

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control mb-2',
            })

            if field in self.placeholders:
                self.fields[field].widget.attrs.update({
                    'placeholder': self.placeholders[field],
                })
