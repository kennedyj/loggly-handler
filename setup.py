#!/usr/bin/env python

from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="loggly-handler",
    version='0.1.0',
    description="Python logging handler that sends messages to Loggly",
    long_description=readme(),
    keywords="loggly logging handler https",
    author="Josh Kennedy",
    author_email="kennedy.josh@gmail.com",
    url="https://github.com/kennedyj/loggly-handler/",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "requests-futures >= 0.9.4"
    ],
    include_package_data=True,
    platform='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers'
    ]
)
