from setuptools import setup, find_packages
from dropboxchooser_field import __version__

setup(
    name='django-dropboxchooser-field',
    version=__version__,
    description='Dropbox chooser field for django',
    long_description=open('README.rst').read(),
    author='Adam Bogdal',
    author_email='adam@bogdal.pl',
    url='https://github.com/bogdal/django-dropboxchooser-field',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'],
    install_requires=[
        'requests',
    ],
)
