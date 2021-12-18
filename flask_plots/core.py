#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This docstring was part of Matplotlib. All rights reserved.
# Full Text:
#    https://matplotlib.org/stable/users/project/license.html
#
# This file is part of the
#   Flask-Plots Project https://github.com/juniors90/Flask-Plots/
#
# Copyright (c) 2021, Ferreira Juan David
#       License: MIT
# Full Text:
#       https://github.com/juniors90/Flask-Plots/blob/master/LICENSE
#
# =============================================================================
# DOCS
# =============================================================================

"""Flask-Plots.

Implementation of Matplotlib in Flask.
"""

# =============================================================================
# IMPORTS
# =============================================================================

import base64
import io

from flask import Blueprint, current_app


def raise_helper(message):  # pragma: no cover
    """Handle for raise in jinja templates."""
    raise RuntimeError(message)


class Plots(object):
    """Base extension class for different Plots versions.

    .. versionadded:: 0.0.1
    """

    static_folder = "plots"
    # Generate the figure **without using pyplot**.

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Sample factory function for initialize the extension."""
        app.config.setdefault("PLOTS_CMAP", "Greys")
        app.config.setdefault("STATIC_FOLDER", "plots")
        app.config.setdefault("BAR_HEIGHT", 50)
        if not hasattr(app, "extensions"):  # pragma: no cover
            app.extensions = {}
        app.extensions["plots"] = self
        blueprint = Blueprint(
            "plots",
            __name__,
            static_folder=f"static/{self.static_folder}",
            static_url_path=f"{app.static_url_path}",
            template_folder="templates",
        )
        app.register_blueprint(blueprint)
        app.jinja_env.globals["plots"] = self
        app.jinja_env.globals["raise"] = raise_helper
        app.jinja_env.add_extension("jinja2.ext.do")

    def get_data(self, fig, fmt="png", decode="ascii"):
        """
        Create a data for embed the result in the html output.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        format : str, default: "png"
            A extension type for the images.

        decode : str, default: "ascii"
            A buffer decode.
        """
        buf = io.BytesIO()
        fig.savefig(buf, format=fmt)
        data = base64.b64encode(buf.getbuffer()).decode(decode)
        return data

    # Statistics plots: Plots for statistical analysis.
    def hist(self, fig, x, ax=None, hist_kws=None):
        """
        Plot a histogram using Matplotlib.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        x : (n,) array or sequence of (n,) arrays
            Input values, this takes either a single array or a sequence of
            arrays which are not required to be of the same length.

        ax : matplotlib.Figure.Axis, (optional)
            A matplotlib axis.

        hist_kwargs : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.

        Returns
        -------
        ax : matplotlib.Figure.Axis
            A matplotlib axis.
        """
        ax = fig.gca() if ax is None else ax
        hist_kws = {} if hist_kws is None else hist_kws
        ax.hist(x, **hist_kws)
        return ax

    def errorbar(self, fig, x, y, ax=None, errorbar_kws=None):
        """
        Plot y versus x as lines and/or markers with attached errorbars.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        x, y : float or array-like
            The data positions.

        ax : matplotlib.Figure.Axis, (optional)
            A matplotlib axis.

        errorbar_kws : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.


        Returns
        -------
        ax : matplotlib.Figure.Axis
            A matplotlib axis.
        """
        ax = fig.gca() if ax is None else ax
        errorbar_kws = {} if errorbar_kws is None else errorbar_kws
        ax.errorbar(x, y, **errorbar_kws)
        return ax

    def violinplot(
        self, fig, dataset, positions, ax=None, violinplot_kws=None
    ):
        """
        Make a violin plot using Matlotlib.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        dataset : Array or a sequence of vectors.
            The input data.

        positions : array-like, default: [1, 2, ..., n]
            The positions of the violins. The ticks and limits are
            automatically set to match the positions.

        ax : matplotlib.Figure.Axis, (optional)
            A matplotlib axis.

        violinplot_kws : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.

        Returns
        -------
        ax : matplotlib.Figure.Axis
            A matplotlib axis.
        """
        ax = fig.gca() if ax is None else ax
        violinplot_kws = {} if violinplot_kws is None else violinplot_kws
        vp = ax.violinplot(dataset, positions, **violinplot_kws)
        return vp

    def eventplot(self, fig, positions, ax=None, eventplot_kws=None):
        """
        Plot identical parallel lines at the given positions.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        positions : array-like or list of array-like
            A 1D array-like defines the positions of one sequence of events.
            Multiple groups of events may be passed as a list of array-likes.
            Each group can be styled independently by passing lists of values
            to *lineoffsets*, *linelengths*, *linewidths*, *colors* and
            *linestyles*.
            Note that *positions* can be a 2D array, but in practice different
            event groups usually have different counts so that one will use a
            list of different-length arrays rather than a 2D array.

        ax : matplotlib.Figure.Axis, (optional)
            A matplotlib axis.

        eventplot_kws : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.

        Returns
        -------
        ax : matplotlib.Figure.Axis
            A matplotlib axis.
        """
        ax = fig.gca() if ax is None else ax
        eventplot_kws = {} if eventplot_kws is None else eventplot_kws
        ax.eventplot(positions, **eventplot_kws)
        return ax

    def hist2d(self, fig, x, y, ax=None, hist2d_kws=None):
        """
        Make a 2D histogram plot using Matplotlib.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        x, y : array-like, shape (n, )
            Input values

        ax : matplotlib.Figure.Axis, (optional)
            A matplotlib axis.

        hist2d_kws : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.

        Returns
        -------
        ax : matplotlib.Figure.Axis
            A matplotlib axis.
        """
        ax = fig.gca() if ax is None else ax
        hist2d_kws = {} if hist2d_kws is None else hist2d_kws
        ax.hist2d(x, y, **hist2d_kws)
        return ax

    def hexbin(self, fig, x, y, ax=None, hexbin_kws=None):
        """
        Make a 2D hexagonal binning plot of points *x*, *y* using Matplotlib.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        x, y : array-like
            The data positions. *x* and *y* must be of the same length.

        ax : matplotlib.Figure.Axis, (optional)
            A matplotlib axis.

        hexbin_kws : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.

        Returns
        -------
        ax : matplotlib.Figure.Axis
            A matplotlib axis.
        """
        ax = fig.gca() if ax is None else ax
        hexbin_kws = {} if hexbin_kws is None else hexbin_kws
        ax.hexbin(x, y, **hexbin_kws)
        return ax

    def scatter_hist2d(
        self, fig, x, y, ax=None, hist2d_kws=None, scatter_kws=None
    ):
        """
        Make a 2D histogram plot using Matplotlib.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        x, y : array-like, shape (n, )
            Input values

        ax : matplotlib.Figure.Axis, (optional)
            A matplotlib axis.

        hist2d_kws : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.

        scatter_kws : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot in term scatter method.

        Returns
        -------
        ax : matplotlib.Figure.Axis
            A matplotlib axis.
        """
        ax = fig.gca() if ax is None else ax
        hist2d_kws = {} if hist2d_kws is None else hist2d_kws
        scatter_kws = {} if scatter_kws is None else scatter_kws
        hist2d_kws.setdefault("cmap", current_app.config["PLOTS_CMAP"])
        ax.hist2d(x, y, **hist2d_kws)
        ax.scatter(x, y, **scatter_kws)
        return ax

    def scatter_hexbin(
        self, fig, x, y, ax=None, hexbin_kws=None, scatter_kws=None
    ):
        """
        Make a 2D scatter-hexagonal binning plot of points *x*, *y*.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        x, y : array-like
            The data positions. *x* and *y* must be of the same length.

        ax : matplotlib.Figure.Axis, (optional)
            A matplotlib axis.

        hexbin_kws : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot in term hexbin method.

        scatter_kws : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot in term scatter method.

        Returns
        -------
        ax : matplotlib.Figure.Axis
            A matplotlib axis.
        """
        ax = fig.gca() if ax is None else ax
        hexbin_kws = {} if hexbin_kws is None else hexbin_kws
        scatter_kws = {} if scatter_kws is None else scatter_kws
        hexbin_kws.setdefault("cmap", current_app.config["PLOTS_CMAP"])
        ax.hexbin(x, y, **hexbin_kws)
        ax.scatter(x, y, **scatter_kws)
        return ax

    def bar(self, fig, x, bar_height=None, ax=None, bar_kws=None):
        """
        Make a bar plot using Matplotlib.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        x : float or array-like
            The x coordinates of the bars. See also *align* for the
            alignment of the bars to the coordinates.

        bar_height : float or array-like,
            The height(s) of the bars. You can config this value
            using ``app.config["BAR_HEIGHT"]``.

        ax : matplotlib.Figure.Axis, (optional)
            A matplotlib axis.

        bar_kws : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.

        Returns
        -------
        ax : matplotlib.Figure.Axis
            A matplotlib axis.
        """
        ax = fig.gca() if ax is None else ax
        bar_kws = {} if bar_kws is None else bar_kws
        bar_height = (
            current_app.config["BAR_HEIGHT"]
            if bar_height is None
            else bar_height
        )
        ax.bar(x, bar_height, **bar_kws)
        return ax

    def pie(self, fig, x, ax=None, pie_kws=None):
        """
        Make a pie plot using Matplotlib.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        x : 1D array-like
            The wedge sizes.

        ax : matplotlib.Figure.Axis, (optional)
            A matplotlib axis.

        bar_kws : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.

        Returns
        -------
        ax : matplotlib.Figure.Axis
            A matplotlib axis.
        """
        ax = fig.gca() if ax is None else ax
        pie_kws = {} if pie_kws is None else pie_kws
        ax.pie(x, **pie_kws)
        return ax

    def boxplot(self, fig, x, ax=None, boxplot_kws=None):
        """
        Draw a box and whisker plot using MAtplotlib.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        x : Array or a sequence of vectors.
            The input data.  If a 2D array, a boxplot is drawn for each column
            in *x*.  If a sequence of 1D arrays, a boxplot is drawn for each
            array in *x*.

        ax : matplotlib.Figure.Axis, (optional)
            A matplotlib axis.

        boxplot_kws : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.

        Returns
        -------
        ax : matplotlib.Figure.Axis
            A matplotlib axis.
        """
        ax = fig.gca() if ax is None else ax
        boxplot_kws = {} if boxplot_kws is None else boxplot_kws
        ax.boxplot(x, **boxplot_kws)
        return ax

    def quiver(self, fig, x, y, u, v, ax=None, quiver_kws=None):
        """
        Plot a 2D field of arrows using matplotlib.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        x, y : 1D or 2D array-like, optional
            The x and y coordinates of the arrow locations.
            If not given, they will be generated as a uniform integer meshgrid
            based on the dimensions of *u* and *v*.
            If *x* and *y* are 1D but *u*, *v* are 2D, *x*, *y* are expanded
            to 2D using ``x, y = np.meshgrid(x, y)``. In this case ``len(x)``
            and ``len(y)`` must match the column and row dimensions of
            *u* and *v*.

        u, v : 1D or 2D array-like
            The x and y direction components of the arrow vectors.
            They must have the same number of elements, matching the
            number of arrow locations. *u* and *v* may be masked. Only
            locations unmasked in *u*, *v*, and *C* will be drawn.
        ax : matplotlib.Figure.Axis, (optional)
            A matplotlib axis.

        quiver_kws : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.

        Returns
        -------
        ax : matplotlib.Figure.Axis
            A matplotlib axis.
        """
        ax = fig.gca() if ax is None else ax
        quiver_kws = {} if quiver_kws is None else quiver_kws
        ax.quiver(x, y, u, v, **quiver_kws)
        return ax

    def streamplot(self, fig, x, y, u, v, ax=None, streamplot_kws=None):
        """
        Draw streamlines of a vector flow using matplotlib.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        x, y : 1D/2D arrays
            Evenly spaced strictly increasing arrays to make a grid.
            If 2D, all rows of *x* must be equal and all columns of
            *y* must be equal; i.e., they must be as if generated
            by ``np.meshgrid(x_1d, y_1d)``.

        u, v : 2D arrays
            *x* and *y*-velocities. The number of rows and columns
            must match the length of *y* and *x*, respectively.

        ax : matplotlib.Figure.Axis, (optional)
            A matplotlib axis.

        streamplot_kws : ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.

        """
        ax = fig.gca() if ax is None else ax
        streamplot_kws = {} if streamplot_kws is None else streamplot_kws
        ax.streamplot(x, y, u, v, **streamplot_kws)
        return ax

    def contourf(self, fig, x, y, z, levels, ax=None, contourf_kws=None):
        """
        Plot contour lines using matplotlib.

        Parameters
        ----------
        fig : matplotlib.Figure
            A instance of Figure Object.

        x, y : array-like, optional
            The coordinates of the values in *z*.

            *x* and *y* must both be 2D with the same shape as *z* (e.g.
            created via `numpy.meshgrid`), or they must both be 1-D such
            that ``len(x) == N`` is the number of columns in *z* and
            ``len(y) == M`` is the number of rows in *z*.

            *X* and *Y* must both be ordered monotonically.

            If not given, they are assumed to be integer indices, i.e.
            ``x = range(N)``, ``y = range(M)``.

        levels : int or array-like, optional
            Determines the number and positions of the contour lines / regions.

            If an int *n*, use `~matplotlib.ticker.MaxNLocator`, which tries
            to automatically choose no more than *n+1* "nice" contour levels
            between *vmin* and *vmax*.

            If array-like, draw contour lines at the specified levels.
            The values must be in increasing order.

        ax : matplotlib.Figure.Axis, (optional)
            A matplotlib axis.

        contourf_kws: ``dict`` or ``None`` (optional)
            The parameters to send to the data plot.

        Returns
        -------
        ax : matplotlib.Figure.Axis
            A matplotlib axis.
        """
        ax = fig.gca() if ax is None else ax
        contourf_kws = {} if contourf_kws is None else contourf_kws
        ax.contourf(x, y, z, levels, **contourf_kws)
        return ax
