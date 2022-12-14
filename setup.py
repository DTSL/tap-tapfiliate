#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-tapfiliate",
    version="0.1.2",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_tapfiliate"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-tapfiliate=tap_tapfiliate:main
    """,
    packages=["tap_tapfiliate"],
    package_data = {
        "schemas": ["tap_tapfiliate/schemas/*.json"]
    },
    include_package_data=True,
)
