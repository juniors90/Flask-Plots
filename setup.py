#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the
#   Flask-Plots Project (https://github.com/juniors90/Flask-Plots/).
# Copyright (c) 2021, Ferreira Juan David
# License: MIT
# Full Text: https://github.com/juniors90/Flask-Plots/blob/master/LICENSE

# =====================================================================
# DOCS
# =====================================================================

"""This file is for distribute and install Flask-Plots"""

# ======================================================================
# IMPORTS
# ======================================================================

import os
import pathlib

from setuptools import setup  # noqa

# =============================================================================
# CONSTANTS
# =============================================================================

PATH = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))


REQUIREMENTS = ["Flask>=2.0.2", "matplotlib>=3.5.0"]

with open(PATH / "flask_plots" / "__init__.py") as fp:
    for line in fp.readlines():
        if line.startswith("__version__ = "):
            VERSION = line.split("=", 1)[-1].replace('"', "").strip()
            break


with open("README.md") as fp:
    LONG_DESCRIPTION = fp.read()


source = "https://github.com/juniors90/Flask-Plots"
tracker = "https://github.com/juniors90/Flask-Plots/issues"
donate = "https://www.paypal.com/donate?hosted_button_id=LFAQ7E7TJ4HSY"
funding = "https://paypal.me/juniors90"


# =============================================================================
# FUNCTIONS
# =============================================================================

setup(
    name="Flask-Plots",
    version=VERSION,
    description="Implementation of Matplotlib in Flask",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Ferreira Juan David",
    author_email="juandavid9a0@gmail.com",
    url="https://github.com/juniors90/Flask-Plots",
    packages=["flask_plots"],
    include_package_data=True,
    platforms="any",
    license="The MIT License",
    install_requires=REQUIREMENTS,
    keywords=["Flask", "Matplotlib", "Data Visualisation"],
    project_urls={
        "Source": source,
        "Tracker": tracker,
        "Donate": donate,
        "Funding": funding,
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
