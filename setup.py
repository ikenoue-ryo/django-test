import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'rb') as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-torina-tutorial1',
    version='0.1',
    packages=find_packages(exclude=('myproject',)),
    include_package_data=True,
    license='MIT License',
    description='Django Simple App',
    long_description=README.decode(),
    url='https://github.com/naritotakizawa/django-torina-tutorial1',
    author='Narito Takizawa',
    author_email='toritoritorina@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)