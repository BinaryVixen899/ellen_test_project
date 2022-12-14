import os, setuptools
from setuptools import find_packages, setup

setuptools.setup(
    name="ellen_test_project",
    version="0.0.1",
    author="Ellen Anders",
    author_email="eanders@fake.email",
    description="Please work",
    long_description="It has been a long day",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=["ellen"]
)