from django import forms


class NewTweetForm(forms.Form):
    tweet_text = forms.CharField(max_length=500)


class SearchForm(forms.Form):
    search_text = forms.CharField(max_length=500)


class UpdateForm(forms.Form):
    update_text = forms.CharField(max_length=500)
