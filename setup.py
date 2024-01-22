# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="ring-seq-py",
    version="0.0.9",
    description="Extends Python list, tuple and str with ring (circular) methods",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://scala-tessella.github.io/ring-seq-py/",
    author="Mario Càllisto",
    author_email="mario.callisto@gmail.com",
    license="APL2",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    # packages=["ring_seq"],
    package_dir={
        '': 'src',
    },
    packages=find_packages(where='src'),
    include_package_data=True,
    install_requires=[]
)
