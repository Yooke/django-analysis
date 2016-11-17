import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-analysis',
    version='0.2',
    packages=['analysis'],
    include_package_data=True,
    license='BSD License',
    description='A analysis tool for django app.',
    long_description="django-analysis is a django's middleware, can use for analysis the django app.",
    url='https://github.com/Yooke/django-analysis',
    author='Em Lei',
    author_email='live1989@foxmail.com',
)
