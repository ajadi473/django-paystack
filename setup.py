import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-paystack",
    version="1.1.0",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",  # example license
    description="A reusable app for making online payments with paystack",
    long_description=README,
    url="https://www.ghorz.com/apps/paystack",
    author="Anthony C. Emmanuel", # Derived
    author_email="mymi14s@hotmail.com",
    install_requires=[
        "requests",
        "future",
        "Paperboy",
        "python-dateutil",
        # "requests-async",
        "requests-async @ https://github.com/encode/requests-async/archive/master.zip",
    ],
    # dependency_links=[
        # "http://github.com/SergeySatskiy/cdm-pythonparser/archive/v2.0.1.tar.gz"
    # ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: X.Y",  # replace "X.Y" as appropriate
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",  # example license
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        # Replace these appropriately if you are stuck on Python 2.
        "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 2",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
