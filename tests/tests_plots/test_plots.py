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


from flask import current_app
from matplotlib.figure import Figure

import pytest as pt


@pt.mark.usefixtures("client")
class TestPlots:
    def test_extension_init(self, app):
        with app.app_context():
            extensions = current_app.extensions
        assert "plots" in extensions
        assert "plots_ui" not in extensions

    def test_get_data(self, plots):
        fig = Figure()
        ax = fig.subplots()  # noqa
        ax.plot([1, 2])
        data = plots.get_data(fig)
        assert data is not None
