
# -*- coding=utf-8 -*-
# Name: teddy oweh
# Email: teddy@teddyoweh.com
# Message: Feel Free To Contact Me on Enquires or Question, il Reply :)mport pathlib

from setuptools import setup, find_packages
import pathlib
 
HERE = pathlib.Path(__file__).parent

 
README = (HERE / "README.md").read_text()
 
setup(
    name="Beardb",
    version="0.0.3",
    description="A Local System Based JSON Database system",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/teddyoweh/Beardb",
    author="Teddy Oweh",
    author_email="teddy@teddyoweh.net",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
  
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "Beardb=reader.__main__:main",
        ]
    },
)