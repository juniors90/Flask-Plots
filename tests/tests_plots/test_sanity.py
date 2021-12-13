#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the
#   Flask-Plots Project
#                      https://github.com/juniors90/Flask-Plots/
# Copyright (c) 2021, Ferreira Juan David
# License: MIT
# Full Text:
#    https://github.com/juniors90/Flask-Plots/blob/master/LICENSE

# =====================================================================
# TESTS
# =====================================================================


def test_can_initialize_app_and_extesion_with_factory_func():
    from flask import Flask
    from flask_plots import Plots

    app = Flask(__name__)
    plots = Plots()
    plots.init_app(app)
