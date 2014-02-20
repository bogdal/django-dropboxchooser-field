from django import forms
from django.conf import settings


class DropboxTextInput(forms.TextInput):
    input_type = 'dropbox-chooser'


class DropboxChooserWidget(DropboxTextInput):

    def __init__(self, attrs=None):
        default_attrs = {
            'style': 'display: none',
            'data-app-key': getattr(settings, 'DROPBOX_APP_KEY', None)}

        if attrs is not None:
            default_attrs.update(attrs)

        super(DropboxChooserWidget, self).__init__(default_attrs)

    class Media:
        js = ['https://www.dropbox.com/static/api/2/dropins.js',
              'js/dropboxchooser_field/chooser.js']
