# -*- coding: utf-8 -*-
import os
import pathlib
import sys

from flask import Flask, render_template_string
import matplotlib
from matplotlib.figure import Figure
import numpy as np

matplotlib.use("Agg")

# this path is pointing to sample_app/
CURRENT_PATH = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))
FLASK_PLOTS_PATH = CURRENT_PATH.parent

sys.path.insert(0, str(FLASK_PLOTS_PATH))

from flask_plots import Plots  # noqa

app = Flask(__name__)

plots = Plots(app)


@app.route("/")
def index():
    fig = Figure()
    ax = fig.subplots()
    ax = plots.scatter_hist2d(
        fig,
        x=np.random.normal(size=100),
        y=np.random.normal(size=100),
        hist_kws={"cmap": "inferno"},
        scatter_kws={"color": "g"},
    )
    ax.set_title("Scatter Hist")
    ax.set_xlabel("Labbel for X!")
    data = plots.get_data(fig)
    return render_template_string(
        """
        <img src='data:image/png;base64,{{ data }}'>
        """,
        data=data,
    )


@app.route("/hist")
def hist():
    # make data
    np.random.seed(1)
    x = 4 + np.random.normal(0, 1.5, 200)
    # Plots
    fig = Figure()
    ax = fig.subplots()
    ax = plots.hist(
        fig,
        x,
        ax,
        hist_kws={"bins": 8, "linewidth": 0.5, "edgecolor": "white"},
    )
    ax.set(
        xlim=(0, 8),
        xticks=np.arange(1, 8),
        ylim=(0, 56),
        yticks=np.linspace(0, 56, 9),
    )
    ax.set_title("Histogram Chart")
    data = plots.get_data(fig)
    return render_template_string(
        "<img src='data:image/png;base64,{{ data }}'>", data=data
    )


@app.route("/boxplot")
def boxplot():
    # make data:
    np.random.seed(10)
    D = np.random.normal((3, 5, 4), (1.25, 1.00, 1.25), (100, 3))
    # plot
    fig = Figure()
    ax = fig.subplots()
    ax = plots.boxplot(
        fig,
        D,
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
    ax.set(
        xlim=(0, 8),
        xticks=np.arange(1, 8),
        ylim=(0, 8),
        yticks=np.arange(1, 8),
    )
    ax.set_title("Boxplot Chart")
    data = plots.get_data(fig)
    return render_template_string(
        "<img src='data:image/png;base64,{{ data }}'>", data=data
    )


@app.route("/errorbar")
def errorbar():
    # make data
    np.random.seed(1)
    x = [2, 4, 6]
    y = [3.6, 5, 4.2]
    yerr = [0.9, 1.2, 0.5]
    # Plot
    fig = Figure()
    ax = fig.subplots()
    ax = plots.errorbar(
        fig,
        x=x,
        y=y,
        errorbar_kws={"yerr": yerr, "fmt": "o", "linewidth": 2, "capsize": 6},
    )
    ax.set(
        xlim=(0, 8),
        xticks=np.arange(1, 8),
        ylim=(0, 8),
        yticks=np.arange(1, 8),
    )
    ax.set_title("Errorbar Chart")
    data = plots.get_data(fig)
    return render_template_string(
        "<img src='data:image/png;base64,{{ data }}'>", data=data
    )


@app.route("/violinplot")
def violinplot():
    # make data
    np.random.seed(10)
    dataset = np.random.normal((3, 5, 4), (0.75, 1.00, 0.75), (200, 3))
    # plot:
    fig = Figure()
    ax = fig.subplots()
    vp = plots.violinplot(
        fig,
        dataset=dataset,
        positions=[2, 4, 6],
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
    ax.set(
        xlim=(0, 8),
        xticks=np.arange(1, 8),
        ylim=(0, 8),
        yticks=np.arange(1, 8),
    )
    ax.set_title("Violin Chart")
    data = plots.get_data(fig)
    return render_template_string(
        "<img src='data:image/png;base64,{{ data }}'>", data=data
    )


@app.route("/eventplot")
def eventplot():
    # make data:
    np.random.seed(1)
    x = [2, 4, 6]
    D = np.random.gamma(4, size=(3, 50))
    # plot:
    fig = Figure()
    ax = fig.subplots()
    ax = plots.eventplot(
        fig,
        D,
        eventplot_kws={
            "orientation": "vertical",
            "lineoffsets": x,
            "linewidth": 0.75,
        },
    )
    ax.set(
        xlim=(0, 8),
        xticks=np.arange(1, 8),
        ylim=(0, 8),
        yticks=np.arange(1, 8),
    )
    ax.set_title("Event Chart")
    data = plots.get_data(fig)
    return render_template_string(
        "<img src='data:image/png;base64,{{ data }}'>", data=data
    )


@app.route("/two-axes")
def two_axes():
    fig = Figure()
    fig.set_size_inches(10, 5)
    axs = fig.subplots(1, 2)
    ax = plots.scatter_hist2d(
        fig,
        x=np.random.normal(size=100),
        y=np.random.normal(size=100),
        ax=axs[1],
        hist_kws={"cmap": "inferno"},
        scatter_kws={"color": "g"},
    )
    ax.set_title("Scatter Hist")
    data = plots.get_data(fig)
    return render_template_string(
        "<img src='data:image/png;base64,{{ data }}'>", data=data
    )


@app.route("/bar")
def bar():
    fig = Figure()
    ax = fig.subplots()
    countries = ["Argentina", "Brasil", "Colombia", "Chile"]
    peoples = [14, 40, 16, 24]
    ax = plots.bar(fig, countries, peoples)
    ax.set_title("Bar Chart")
    data = plots.get_data(fig)
    return render_template_string(
        "<img src='data:image/png;base64,{{ data }}'>", data=data
    )


@app.route("/pie")
def pie():
    fig = Figure()
    ax = fig.subplots()
    ax = plots.pie(
        fig,
        x=[14, 40, 16, 24],
        pie_kws={
            "labels": ["Argentina", "Brasil", "Colombia", "Chile"],
            "radius": 3,
            "center": (4, 4),
            "wedgeprops": {"linewidth": 1, "edgecolor": "white"},
            "frame": True,
        },
    )
    ax.set(
        xlim=(0, 8),
        xticks=np.arange(1, 8),
        ylim=(0, 8),
        yticks=np.arange(1, 8),
    )
    ax.set_title("Pie Chart")
    data = plots.get_data(fig)
    return render_template_string(
        "<img src='data:image/png;base64,{{ data }}'>", data=data
    )


@app.route("/hello")
def hello():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    ax.set_title("Linear Function")
    # Return data from temporary buffer.
    data = plots.get_data(fig)
    return f"<img src='data:image/png;base64,{data}'/>"


@app.route("/hello2")
def hello2():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([-1, 4])
    ax.set_title("Linear Function 2")
    # Embed the result in the html output.
    data = plots.get_data(fig)
    return render_template_string(
        """{% from 'plots/utils.html' import render_img %}
        <img src='data:image/png;base64,{{data}}' alt='some_img1'/>
        {{ render_img(data=data, alt_img='some_img2') }}
        """,
        data=data,
    )


if __name__ == "__main__":
    app.run(debug=True)
