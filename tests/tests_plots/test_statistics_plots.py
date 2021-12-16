#!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# This file is part of the Flask-Plots Project
#    https://github.com/juniors90/Flask-Plots/
# Copyright (c) 2021, Ferreira Juan David
# License:
#    MIT
# Full Text:
#    https://github.com/juniors90/Flask-Plots/blob/master/LICENSE
#
# =====================================================================
# TESTS
# =====================================================================

from matplotlib.testing.decorators import check_figures_equal
import numpy as np


class TestPlots:
    x = np.random.normal(size=100)
    y = np.random.normal(size=100)

    @check_figures_equal(extensions=["png"])
    def test_scatter_hist2d(self, app, plots, fig_test, fig_ref):
        test_ax = fig_test.subplots()
        with app.app_context():
            plots.scatter_hist2d(fig=fig_test, x=self.x, y=self.y, ax=test_ax)

        exp_ax = fig_ref.subplots()
        exp_ax.hist2d(x=self.x, y=self.y, cmap="Greys")
        exp_ax.scatter(self.x, self.y)

    @check_figures_equal(extensions=["png"])
    def test_scatter_hist(self, app, plots, fig_test, fig_ref):
        # make data
        np.random.seed(1)
        z = 4 + np.random.normal(0, 1.5, 200)
        # test plot:
        test_ax = fig_test.subplots()
        with app.app_context():
            plots.hist(
                fig=fig_test,
                x=z,
                ax=test_ax,
                hist_kws={"bins": 8, "linewidth": 0.5, "edgecolor": "white"},
            )
            test_ax.set(
                xlim=(0, 8),
                xticks=np.arange(1, 8),
                ylim=(0, 56),
                yticks=np.linspace(0, 56, 9),
            )
            test_ax.set_title("Histogram Chart")

        # expected plot:
        exp_ax = fig_ref.subplots()
        exp_ax.hist(z, bins=8, linewidth=0.5, edgecolor="white")
        exp_ax.set(
            xlim=(0, 8),
            xticks=np.arange(1, 8),
            ylim=(0, 56),
            yticks=np.linspace(0, 56, 9),
        )
        exp_ax.set_title("Histogram Chart")

    @check_figures_equal(extensions=["png"])
    def test_boxplot(self, app, plots, fig_test, fig_ref):
        # make data
        np.random.seed(10)
        D = np.random.normal((3, 5, 4), (1.25, 1.00, 1.25), (100, 3))

        # test plot:
        test_ax = fig_test.subplots()
        with app.app_context():
            plots.boxplot(
                fig=fig_test,
                x=D,
                ax=test_ax,
                boxplot_kws={
                    "positions": [2, 4, 6],
                    "widths": 1.5,
                    "patch_artist": True,
                    "showmeans": False,
                    "showfliers": False,
                    "medianprops": {"color": "white", "linewidth": 0.5},
                    "boxprops": {
                        "facecolor": "C0",
                        "edgecolor": "white",
                        "linewidth": 0.5,
                    },
                    "whiskerprops": {"color": "C0", "linewidth": 1.5},
                    "capprops": {"color": "C0", "linewidth": 1.5},
                },
            )
        test_ax.set(
            xlim=(0, 8),
            xticks=np.arange(1, 8),
            ylim=(0, 8),
            yticks=np.arange(1, 8),
        )
        test_ax.set_title("Boxplot Chart")

        # expected plot:
        exp_ax = fig_ref.subplots()
        exp_ax.boxplot(
            D,
            positions=[2, 4, 6],
            widths=1.5,
            patch_artist=True,
            showmeans=False,
            showfliers=False,
            medianprops={"color": "white", "linewidth": 0.5},
            boxprops={
                "facecolor": "C0",
                "edgecolor": "white",
                "linewidth": 0.5,
            },
            whiskerprops={"color": "C0", "linewidth": 1.5},
            capprops={"color": "C0", "linewidth": 1.5},
        )
        exp_ax.set(
            xlim=(0, 8),
            xticks=np.arange(1, 8),
            ylim=(0, 8),
            yticks=np.arange(1, 8),
        )
        exp_ax.set_title("Boxplot Chart")

    @check_figures_equal(extensions=["png"])
    def test_errorbar(self, app, plots, fig_test, fig_ref):
        # make data
        np.random.seed(1)
        x = [2, 4, 6]
        y = [3.6, 5, 4.2]
        yerr = [0.9, 1.2, 0.5]
        # test plot:
        test_ax = fig_test.subplots()
        with app.app_context():
            plots.errorbar(
                fig=fig_test,
                x=x,
                y=y,
                ax=test_ax,
                errorbar_kws={
                    "yerr": yerr,
                    "fmt": "o",
                    "linewidth": 2,
                    "capsize": 6,
                },
            )
        test_ax.set(
            xlim=(0, 8),
            xticks=np.arange(1, 8),
            ylim=(0, 8),
            yticks=np.arange(1, 8),
        )
        test_ax.set_title("Errorbar Chart")

        # expected plot:
        exp_ax = fig_ref.subplots()
        exp_ax.errorbar(x, y, yerr, fmt="o", linewidth=2, capsize=6)
        exp_ax.set(
            xlim=(0, 8),
            xticks=np.arange(1, 8),
            ylim=(0, 8),
            yticks=np.arange(1, 8),
        )
        exp_ax.set_title("Errorbar Chart")

    @check_figures_equal(extensions=["png"])
    def test_violinplot(self, app, plots, fig_test, fig_ref):
        # make data
        np.random.seed(10)
        dataset = np.random.normal((3, 5, 4), (0.75, 1.00, 0.75), (200, 3))
        # test plot:
        test_ax = fig_test.subplots()
        with app.app_context():
            vp = plots.violinplot(
                fig=fig_test,
                dataset=dataset,
                positions=[2, 4, 6],
                ax=test_ax,
                violinplot_kws={
                    "widths": 2,
                    "showmeans": False,
                    "showmedians": False,
                    "showextrema": False,
                },
            )
        # styling:
        for body in vp["bodies"]:
            body.set_alpha(0.9)
        test_ax.set(
            xlim=(0, 8),
            xticks=np.arange(1, 8),
            ylim=(0, 8),
            yticks=np.arange(1, 8),
        )
        test_ax.set_title("Violin Chart")
        # expected plot:
        exp_ax = fig_ref.subplots()
        vp = exp_ax.violinplot(
            dataset,
            [2, 4, 6],
            widths=2,
            showmeans=False,
            showmedians=False,
            showextrema=False,
        )
        # styling:
        for body in vp["bodies"]:
            body.set_alpha(0.9)
        exp_ax.set(
            xlim=(0, 8),
            xticks=np.arange(1, 8),
            ylim=(0, 8),
            yticks=np.arange(1, 8),
        )
        exp_ax.set_title("Violin Chart")

    @check_figures_equal(extensions=["png"])
    def test_eventplot(self, app, plots, fig_test, fig_ref):
        # make data:
        np.random.seed(1)
        x = [2, 4, 6]
        D = np.random.gamma(4, size=(3, 50))
        # plot:
        test_ax = fig_test.subplots()
        with app.app_context():
            plots.eventplot(
                fig=fig_test,
                positions=D,
                ax=test_ax,
                eventplot_kws={
                    "orientation": "vertical",
                    "lineoffsets": x,
                    "linewidth": 0.75,
                },
            )
        test_ax.set(
            xlim=(0, 8),
            xticks=np.arange(1, 8),
            ylim=(0, 8),
            yticks=np.arange(1, 8),
        )
        test_ax.set_title("Event Chart")
        # expected plot:
        exp_ax = fig_ref.subplots()
        exp_ax.eventplot(
            D, orientation="vertical", lineoffsets=x, linewidth=0.75
        )
        exp_ax.set(
            xlim=(0, 8),
            xticks=np.arange(1, 8),
            ylim=(0, 8),
            yticks=np.arange(1, 8),
        )
        exp_ax.set_title("Event Chart")

    @check_figures_equal(extensions=["png"])
    def test_pie(self, app, plots, fig_test, fig_ref):
        # test plot:
        test_ax = fig_test.subplots()
        with app.app_context():
            plots.pie(
                fig=fig_test,
                x=[14, 40, 16, 24],
                ax=test_ax,
                pie_kws={
                    "labels": ["Argentina", "Brasil", "Colombia", "Chile"],
                    "radius": 3,
                    "center": (4, 4),
                    "wedgeprops": {"linewidth": 1, "edgecolor": "white"},
                    "frame": True,
                },
            )
        test_ax.set(
            xlim=(0, 8),
            xticks=np.arange(1, 8),
            ylim=(0, 8),
            yticks=np.arange(1, 8),
        )
        test_ax.set_title("Pie Chart")
        # expected plot:
        exp_ax = fig_ref.subplots()
        exp_ax.pie(
            x=[14, 40, 16, 24],
            labels=["Argentina", "Brasil", "Colombia", "Chile"],
            radius=3,
            center=(4, 4),
            wedgeprops={"linewidth": 1, "edgecolor": "white"},
            frame=True,
        )
        exp_ax.set(
            xlim=(0, 8),
            xticks=np.arange(1, 8),
            ylim=(0, 8),
            yticks=np.arange(1, 8),
        )
        exp_ax.set_title("Pie Chart")

    @check_figures_equal(extensions=["png"])
    def test_bar(self, app, plots, fig_test, fig_ref):
        # make data:
        np.random.seed(3)
        x = 0.5 + np.arange(8)
        y = np.random.uniform(2, 7, len(x))
        # test plot
        test_ax = fig_test.subplots()
        with app.app_context():
            plots.bar(
                fig_test,
                x,
                y,
                ax=test_ax,
                bar_kws={"width": 1, "edgecolor": "white", "linewidth": 0.7},
            )
        test_ax.set(
            xlim=(0, 8),
            xticks=np.arange(1, 8),
            ylim=(0, 8),
            yticks=np.arange(1, 8),
        )
        test_ax.set_title("Bar Chart")
        # expected plot:
        exp_ax = fig_ref.subplots()
        exp_ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
        exp_ax.set(
            xlim=(0, 8),
            xticks=np.arange(1, 8),
            ylim=(0, 8),
            yticks=np.arange(1, 8),
        )
        exp_ax.set_title("Bar Chart")

    @check_figures_equal(extensions=["png"])
    def test_scatter_hexbin(self, app, plots, fig_test, fig_ref):
        # make data: correlated + noise
        np.random.seed(1)
        x = np.random.randn(5000)
        y = 1.2 * x + np.random.randn(5000) / 3
        # test plot:
        test_ax = fig_test.subplots()
        with app.app_context():
            plots.scatter_hexbin(
                fig=fig_test,
                x=x,
                y=y,
                ax=test_ax,
                hexbin_kws={"cmap": "inferno", "gridsize": 20},
                scatter_kws={"color": "g"},
            )
        test_ax.set(xlim=(-2, 2), ylim=(-3, 3))
        test_ax.set_title("Scatter Hexbin Chart")
        # expected plot
        exp_ax = fig_ref.subplots()
        exp_ax.hexbin(x, y, cmap="inferno", gridsize=20)
        exp_ax.scatter(x, y, color="g")
        exp_ax.set(xlim=(-2, 2), ylim=(-3, 3))
        exp_ax.set_title("Scatter Hexbin Chart")

    @check_figures_equal(extensions=["png"])
    def test_quiver(self, app, plots, fig_test, fig_ref):
        # make data:
        x = np.linspace(-4, 4, 6)
        y = np.linspace(-4, 4, 6)
        X, Y = np.meshgrid(x, y)
        U = X + Y
        V = Y - X
        # test plot:
        test_ax = fig_test.subplots()
        with app.app_context():
            plots.quiver(
                fig=fig_test,
                X=X,
                Y=Y,
                U=U,
                V=V,
                ax=test_ax,
                quiver_kws={
                    "color": "C0",
                    "angles": "xy",
                    "scale_units": "xy",
                    "scale": 5,
                    "width": 0.015,
                },
            )
        test_ax.set(xlim=(-5, 5), ylim=(-5, 5))
        test_ax.set_title("Quiver Chart")
        # plot
        exp_ax = fig_ref.subplots()
        exp_ax.quiver(
            X,
            Y,
            U,
            V,
            color="C0",
            angles="xy",
            scale_units="xy",
            scale=5,
            width=0.015,
        )
        exp_ax.set(xlim=(-5, 5), ylim=(-5, 5))
        exp_ax.set_title("Quiver Chart")

    @check_figures_equal(extensions=["png"])
    def test_streamplot(self, app, plots, fig_test, fig_ref):
        # make a stream function:
        X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
        Z = (1 - X / 2 + X ** 5 + Y ** 3) * np.exp(-(X ** 2) - Y ** 2)
        # make U and V out of the streamfunction:
        V = np.diff(Z[1:, :], axis=1)
        U = -np.diff(Z[:, 1:], axis=0)
        # test plot:
        test_ax = fig_test.subplots()
        with app.app_context():
            plots.streamplot(fig=fig_test, X=X[1:, 1:], Y=Y[1:, 1:], U=U, V=V)
        test_ax.set_title("Streamplot Chart")
        # expected plot:
        exp_ax = fig_ref.subplots()
        exp_ax.streamplot(X[1:, 1:], Y[1:, 1:], U, V)
        exp_ax.set_title("Streamplot Chart")

    @check_figures_equal(extensions=["png"])
    def test_contourf(self, app, plots, fig_test, fig_ref):
        # make data
        X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
        Z = (1 - X / 2 + X ** 5 + Y ** 3) * np.exp(-(X ** 2) - Y ** 2)
        levels = np.linspace(Z.min(), Z.max(), 7)

        # test plot:
        test_ax = fig_test.subplots()
        with app.app_context():
            plots.contourf(fig=fig_test, X=X, Y=Y, Z=Z, levels=levels)
        test_ax.set_title("Contourf Chart")
        # expected plot:
        exp_ax = fig_ref.subplots()
        exp_ax.contourf(X, Y, Z, levels=levels)
        exp_ax.set_title("Contourf Chart")
