django-dropboxchooser-field
===========================

.. image:: https://version-image.appspot.com/pypi/?name=django-dropboxchooser-field
    :target: https://pypi.python.org/pypi/django-dropboxchooser-field
    

Dropbox chooser field for django.

.. image:: http://bogdal.pl/dropboxchooser.png
    :target: https://www.dropbox.com/developers/dropins/chooser/js
    

Quickstart
----------

1. Install the package via ``pip``:

.. code-block:: bash

    pip install django-dropboxchooser-field
    
  
2. Add ``dropboxchooser_field`` to ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
      ...
      'dropboxchooser_field',
      ...
    )
  

3. Add your `Drop-in <https://www.dropbox.com/developers/dropins/chooser/js>`_ app key to the ``settings.py`` file:

.. code-block:: python

    DROPBOX_APP_KEY = ''
    
Usage
-----

.. code-block:: python

    from django import forms
    from dropboxchooser_field.fields import DropboxChooserField
    
    class MyForm(forms.Form):
        file_from_dropbox = DropboxChooserField(extensions=['jpg', 'png'])
