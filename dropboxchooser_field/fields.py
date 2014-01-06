from StringIO import StringIO
from urlparse import urlparse

from django import forms
from django.core.files import File
import requests

from .widgets import DropboxChooserWidget


class DropboxChooserField(forms.FileField):

    widget = DropboxChooserWidget

    def __init__(self, extensions=[], *args, **kwargs):
        super(DropboxChooserField, self).__init__(*args, **kwargs)
        extensions = map(lambda x: x if x.startswith(".") else (".%s" % x),
                         extensions)
        self.widget.attrs.update({'data-extensions': " ".join(extensions)})

    def _download_file(self, url):
        filename = urlparse(url).path.split('/')[-1]
        return File(StringIO(requests.get(url).content), name=filename)

    def clean(self, url, initial=None):
        data = None

        if url:
            data = self._download_file(url)

        return super(DropboxChooserField, self).clean(data, initial)
