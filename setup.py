"""Add support for SoftLayer uploads
"""

from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md')) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="monsoon-upload-softlayer",
    version="0.1.1",
    description="Monsoon plug-in for Softlayer uploads.",
    long_description=LONG_DESCRIPTION,
    url="https://github.ibm.com/apset/monsoon",
    author="Luiz Aoqui",
    author_email="laoqui@ca.ibm.com",
    license="IBM",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Database",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: Utilities"
    ],
    packages=find_packages(),
    install_requires=[
        "monsoon-cli>=0.1.4",
        "softlayer-object-storage==0.5.4"
    ],
    entry_points={
        "monsoon.uploads": [
            "softlayer=softlayer:ObjectStorageUpload"
        ]
    }
)
