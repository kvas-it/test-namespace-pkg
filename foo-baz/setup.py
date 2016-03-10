# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='foo-baz',
    version='0.0.1',
    description='Test',
    long_description='Test',
    author='Vasily Kuznetsov',
    author_email='vasily@adblockplus.org',
    packages=['foo', 'foo.baz'],
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    keywords='pkg_resources',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
