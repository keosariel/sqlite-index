from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.rst"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'Indexes and searches data in a simple sqlite database'

long_description = long_description.strip("\n")

# Setting up
setup(
    name="sqlite-index",
    version=VERSION,
    author="Kenneth Gabriel",
    author_email="kennethgabriel78@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'json', 'index', 'sqlite', "search", "python3"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)