
# -*- coding=utf-8 -*-
# Name: teddy oweh
# Email: teddy@teddyoweh.com
# Message: Feel Free To Contact Me on Enquires or Question, il Reply :)mport pathlib

from setuptools import setup, find_packages
import pathlib
 
HERE = pathlib.Path(__file__).parent

 
README = (HERE / "README.md").read_text()
 
setup(
    name="beardb",
    version="0.0.1",
    description="Database system implementing encrypted versions JSON of data. Easy to access, manage and deploy remotely",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/teddyoweh/Beardb",
    author="Teddy Oweh",
    author_email="teddy@teddyoweh.net",
    packages=find_packages('src/beardb/'),
    package_dir={'': 'src/beardb/'},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
  
    include_package_data=True,
    install_requires=['cryptography','requests'],
    entry_points={
        "console_scripts": [
            "Beardb=reader.__main__:main",
        ]
    },
)