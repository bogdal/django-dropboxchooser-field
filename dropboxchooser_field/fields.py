from StringIO import StringIO
from urlparse import urlparse

from django import forms
from django.core.files import File
import requests

from .widgets import DropboxChooserWidget


class DropboxChooserField(forms.FileField):

    widget = DropboxChooserWidget

    def _download_file(self, url):
        filename = urlparse(url).path.split('/')[-1]
        return File(StringIO(requests.get(url).content), name=filename)

    def clean(self, url, initial=None):
        data = None

        if url:
            data = self._download_file(url)

        return super(DropboxChooserField, self).clean(data, initial)
