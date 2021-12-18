#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the
#      Flask-Plots Project (https://github.com/juniors90/Flask-Plots/).
# Copyright (c) 2021, Ferreira Juan David
# License:
#         MIT
# Full Text:
#           https://github.com/juniors90/Flask-Plots/blob/master/LICENSE

from flask_plots import Plots

import pytest as pt


@pt.fixture(autouse=True)
def plots(app):
    yield Plots(app)
