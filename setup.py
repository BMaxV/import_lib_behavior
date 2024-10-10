import os
import setuptools

setuptools.setup(
    name = "module import lib problem",
    version = "0.1",
    author = "bmaxv",
    description = ("example"),
    packages= ["module"],
    license = "MIT",
    entry_points={
    "console_scripts": [
        "my_import_tool_showcase = module.main:main",
    ]
    }
)
