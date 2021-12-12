#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the
#   Flask-Plots Project https://github.com/juniors90/Flask-Plots/
#
# Copyright (c) 2021, Ferreira Juan David
#       License: MIT
# Full Text:
#       https://github.com/juniors90/Flask-Plots/blob/master/LICENSE

# =============================================================================
# DOCS
# =============================================================================

"""Flask-Plots.

Implementation of Matplotlib in Flask.
"""

# =============================================================================
# IMPORTS
# =============================================================================

import io
import base64
from flask import Blueprint
import matplotlib.pyplot as plt


class Plots(object):
    """Base extension class for different Plots versions.

    .. versionadded:: 0.0.1
    """

    def __init__(self, app=None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.cmap = app.config.setdefault("PLOTS_CMAP", "Greys")
        self.static_folder = app.config.setdefault("STATIC_FOLDER", "plots")
        self.bar_height = app.config.setdefault("BAR_HEIGHT", 50)

        if not hasattr(app, "extensions"):
            app.extensions = {}
        blueprint = Blueprint(
            "plots",
            __name__,
            static_folder=f"static/{self.static_folder}",
            static_url_path=f"{app.static_url_path}",
            template_folder="templates",
        )
        app.register_blueprint(blueprint)
        app.jinja_env.globals["semantic"] = self
        app.jinja_env.add_extension("jinja2.ext.do")

    def get_data(self, fig, format="png"):
        img = io.BytesIO()
        fig.savefig(img, format=format)
        img.seek(0)
        data = base64.b64encode(img.getvalue()).decode()
        return data

    # Statistics plots: Plots for statistical analysis.
    def hist(self, x, ax=None, hist_kws=None):
        """Plot a histogram using Matplotlib.

        Parameters
        ----------
        x : (n,) array or sequence of (n,) arrays
            Input values, this takes either a single array or a sequence of
            arrays which are not required to be of the same length.

        ax : matplotlib.pyplot.Axis, (optional)
            A matplotlib axis.

        hist_kwargs: ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.
            Only ``label`` and ``color`` can't be provided.

        Returns
        -------
        ax : matplotlib.pyplot.Axis
            A matplotlib axis.
        """
        ax = plt.gca() if ax is None else ax
        hist_kws = {} if hist_kws is None else hist_kws
        ax.hist(x, **hist_kws)
        return ax

    def errorbar(self, x, y, ax=None, errorbar_kws=None):
        """Plot y versus x as lines and/or markers with attached errorbars.

        Parameters
        ----------
        x, y : float or array-like
            The data positions.

        ax : matplotlib.pyplot.Axis, (optional)
            A matplotlib axis.

        errorbar_kws: ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.
            Only ``label`` and ``color`` can't be provided.

        Returns
        -------
        ax : matplotlib.pyplot.Axis
            A matplotlib axis.
        """
        ax = plt.gca() if ax is None else ax
        errorbar_kws = {} if errorbar_kws is None else errorbar_kws
        ax.errorbar(x, y, **errorbar_kws)
        return ax

    def violinplot(self, dataset, positions, ax=None, violinplot_kws=None):
        """Make a violin plot. using Matlotlib.

        Parameters
        ----------
        dataset : Array or a sequence of vectors.
            The input data.
        
        positions : array-like, default: [1, 2, ..., n]
            The positions of the violins. The ticks and limits are
            automatically set to match the positions.
        
        ax : matplotlib.pyplot.Axis, (optional)
            A matplotlib axis.

        violinplot_kws: ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.
            Only ``label`` and ``color`` can't be provided.

        Returns
        -------
        ax : matplotlib.pyplot.Axis
            A matplotlib axis.
        """
        ax = plt.gca() if ax is None else ax
        violinplot_kws = {} if violinplot_kws is None else violinplot_kws
        vp = ax.violinplot(dataset, positions, **violinplot_kws)
        return vp

    def eventplot(self, positions, ax=None, eventplot_kws=None):
        """Plot identical parallel lines at the given positions.

        Parameters
        ----------
        positions : array-like or list of array-like
            A 1D array-like defines the positions of one sequence of events.
            Multiple groups of events may be passed as a list of array-likes.
            Each group can be styled independently by passing lists of values
            to *lineoffsets*, *linelengths*, *linewidths*, *colors* and
            *linestyles*.
            Note that *positions* can be a 2D array, but in practice different
            event groups usually have different counts so that one will use a
            list of different-length arrays rather than a 2D array.

        ax : matplotlib.pyplot.Axis, (optional)
            A matplotlib axis.

        eventplot_kws: ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.
            Only ``label`` and ``color`` can't be provided.

        Returns
        -------
        ax : matplotlib.pyplot.Axis
            A matplotlib axis.
        """
        ax = plt.gca() if ax is None else ax
        eventplot_kws = {} if eventplot_kws is None else eventplot_kws
        ax.eventplot(positions, **eventplot_kws)
        return ax

    def scatter_hist(self, x, y, ax=None, hist_kws=None, scatter_kws=None):
        ax = plt.gca() if ax is None else ax
        hist_kws = {} if hist_kws is None else hist_kws
        scatter_kws = {} if scatter_kws is None else scatter_kws
        hist_kws.setdefault("cmap", self.cmap)
        ax.hist2d(x, y, **hist_kws)
        ax.scatter(x, y, **scatter_kws)
        return ax

    def scatter_hexbin(self, x, y, ax=None, hexbin_kws=None, scatter_kws=None):
        ax = plt.gca() if ax is None else ax
        hexbin_kws = {} if hexbin_kws is None else hexbin_kws
        scatter_kws = {} if scatter_kws is None else scatter_kws
        hexbin_kws.setdefault("cmap", self.cmap)
        ax.hexbin(x, y, **hexbin_kws)
        ax.scatter(x, y, **scatter_kws)
        return ax

    def bar(self, x, bar_height=None, ax=None, bar_kws=None):
        """Make a bar plot using Matplotlib.

        Parameters
        ----------
        x : float or array-like
            The x coordinates of the bars. See also *align* for the
            alignment of the bars to the coordinates.

        bar_height : float or array-like, 
            The height(s) of the bars. You can config this value
            using ``app.config["BAR_HEIGHT"]``.
        
        ax : matplotlib.pyplot.Axis, (optional)
            A matplotlib axis.
        
        bar_kws: ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.
            Only ``label`` and ``color`` can't be provided.

        Returns
        -------
        ax : matplotlib.pyplot.Axis
            A matplotlib axis.
        """
        ax = plt.gca() if ax is None else ax
        bar_kws = {} if bar_kws is None else bar_kws
        bar_height = self.bar_height if bar_height is None else bar_height
        ax.bar(x, bar_height, **bar_kws)
        return ax

    def pie(self, x, ax=None, pie_kws=None):
        """Make a pie plot using Matplotlib.

        Parameters
        ----------
        x : 1D array-like
            The wedge sizes.
        
        ax : matplotlib.pyplot.Axis, (optional)
            A matplotlib axis.
        
        bar_kws: ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.
            Only ``label`` and ``color`` can't be provided.

        Returns
        -------
        ax : matplotlib.pyplot.Axis
            A matplotlib axis.
        """
        ax = plt.gca() if ax is None else ax
        pie_kws = {} if pie_kws is None else pie_kws
        ax.pie(x, **pie_kws)
        return ax

    def boxplot(self, x, ax=None, boxplot_kws=None):
        """Draw a box and whisker plot using MAtplotlib.

        Parameters
        ----------
        x : Array or a sequence of vectors.
            The input data.  If a 2D array, a boxplot is drawn for each column
            in *x*.  If a sequence of 1D arrays, a boxplot is drawn for each
            array in *x*.
        
        ax : matplotlib.pyplot.Axis, (optional)
            A matplotlib axis.
        
        boxplot_kws: ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.
            Only ``label`` and ``color`` can't be provided.

        Returns
        -------
        ax : matplotlib.pyplot.Axis
            A matplotlib axis.
        """
        ax = plt.gca() if ax is None else ax
        boxplot_kws = {} if boxplot_kws is None else boxplot_kws
        ax.boxplot(x, **boxplot_kws)
        return ax
