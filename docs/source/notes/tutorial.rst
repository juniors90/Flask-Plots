How to embed in a web application server?
=========================================

.. important::
    
    When using Matplotlib_ in a web server not use pyplot. You can directly create
    figures using the ``Figure`` constructor and render with ``Plots.render_data()`` method.

Prerequisites
-------------

- Beginner level understanding of the Flask framework.

- Familiarity with the common plotting commands in Matplotlib_.

Flask backend setup
-------------------

Create a new directory in your base directory and then navigate into it

.. code-block:: bash
    
    $ mkdir backend
    $ cd backend

Next, create a virtual environment.

.. code-block:: bash
    
    $ pip install virtualenv
    $ virtualenv venv


Once we have created our environment, we must tell the terminal that we want
to make use of it and not the global Python environment of the system. Therefore:

We will execute the following command if we are on Linux/Mac:

.. code-block:: bash
    
    $ source env/bin/activate

For Windows users:

.. code-block:: bash
    
    $ env\Scripts\activate.bat

We will know that the environment is active because the prompt
begins with the word "(venv)", as the following image shows:

.. code-block:: bash
    
    (venv) $

To install Flask-Plots we will write the following command in the terminal:

.. code-block:: bash
    
    (venv) $ pip install Flask-Plots

Create a app.py file such tah conatin the followin sript:

.. code-block:: python
    :emphasize-lines: 2, 8

    from flask import Flask, render_template_string
    from flask_plots import Plots
    import matplotlib
    from matplotlib.figure import Figure
    import numpy as np
    
    app = Flask(__name__)
    plots = Plots(app)

    # routes
    @app.route("/")
    def bar():
        # Make data
        countries = ["Argentina", "Brasil", "Colombia", "Chile"]
        peoples = [14, 40, 16, 24]
        fig = Figure()
        ax = fig.subplots()
        ax = plots.bar(fig, countries, peoples)
        ax.set_title("Bar Chart")
        data = plots.get_data(fig)
        return render_template_string(
                """
                {% from 'plots/utils.html' import render_img %}
                {{ render_img(data=data, alt_img='my_img') }}
                """,
                data=data
            )

    if __name__ == "__main__":
        app.run(port=5000, debug=True)

Assuming that the working directory contains this script:

- Linux/Mac system:

.. code-block:: bash
    
    (venv) $ FLASK_APP=app
    (venv) $ flask run

- Windows

.. code-block:: bash
    
    (venv) $ set FLASK_APP=app.py
    (venv) $ flask run    

Then navigate to the url ``http://127.0.0.1:5000/``.
You should see the *bar plot* rendered in ``png`` format.

Arrays and Fields
-----------------

Plotting for arrays of data ``Z(x, y)`` and fields ``U(x, y)``, ``V(x, y)`` using Matplotlib_.

.. code-block:: python
    :emphasize-lines: 9

    @app.route("/contourf")
    def contourf():
        # make data
        X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
        Z = (1 - X / 2 + X ** 5 + Y ** 3) * np.exp(-(X ** 2) - Y ** 2)
        levels = np.linspace(Z.min(), Z.max(), 7)
        fig = Figure()
        ax = fig.subplots()
        ax = plots.contourf(fig=fig_test, X=X, Y=Y, Z=Z, levels=levels)
        ax.set_title("Contourf Chart")
        data = plots.get_data(fig)
        return render_template_string(
                """
                {% from 'plots/utils.html' import render_img %}
                {{ render_img(data=data, alt_img='my_img') }}
                """,
                data=data
            )


.. code-block:: python
    :emphasize-lines: 12-19, 21, 24-25

    @app.route("/quiver")
    def quiver():
        # make data
        x = np.linspace(-4, 4, 6)
        y = np.linspace(-4, 4, 6)
        X, Y = np.meshgrid(x, y)
        U = X + Y
        V = Y - X
        # plots:
        fig = Figure()
        ax = fig.subplots()
        ax = plots.quiver(fig, X, Y, U, V, quiver_kws={
                    'color':'C0',
                    'angles':'xy',
                    'scale_units':'xy',
                    'scale':5,
                    'width':.015
                }
            )
        ax.set_title("Quiver Chart")
        data = plots.get_data(fig)
        return render_template_string(
                """
                {% from 'plots/utils.html' import render_img %}
                {{ render_img(data=data, alt_img='my_img') }}
                """,
                data=data
            )

.. code-block:: python
    :emphasize-lines: 12, 14, 17-18

    @app.route("/streamplot")
    def stremplot():
        # make a stream function:
        X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
        Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)
        # make U and V out of the streamfunction:
        V = np.diff(Z[1:, :], axis=1)
        U = -np.diff(Z[:, 1:], axis=0)
        # plot:
        fig = Figure()
        ax = fig.subplots()
        ax = plots.streamplot(fig, X[1:, 1:], Y[1:, 1:], U, V)
        ax.set_title("Streamplot Chart")
        data = plots.get_data(fig)
        return render_template_string(
                """
                {% from 'plots/utils.html' import render_img %}
                {{ render_img(data=data, alt_img='my_img') }}
                """,
                data=data,
            )

Statistics
----------

.. code-block:: python
    :emphasize-lines: 9-27, 35, 38-39

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
                """
                {% from 'plots/utils.html' import render_img %}
                {{ render_img(data=data, alt_img='my_img') }}
                """,
                data=data,
            )

.. code-block:: python
    :emphasize-lines: 11-21, 27, 30, 31
    
    @app.route("/errorbar")
    def errorbar():
        # make data:
        np.random.seed(1)
        x = [2, 4, 6]
        y = [3.6, 5, 4.2]
        yerr = [0.9, 1.2, 0.5]
        # plot
        fig = Figure()
        ax = fig.subplots()
        ax = plots.errorbar(
                fig,
                x,
                y,
                yerr,
                errorbar_kws={
                    "fmt":'o',
                    "linewidth":2,
                    "capsize":6
                }
            )
        ax.set(xlim=(0, 8),
               xticks=np.arange(1, 8),
               ylim=(0, 8),
               yticks=np.arange(1, 8))
        ax.set_title("Errorbar Chart")
        data = plots.get_data(fig)
        return render_template_string(
                """
                {% from 'plots/utils.html' import render_img %}
                {{ render_img(data=data, alt_img='my_img') }}
                """,
                data=data,
            )

.. code-block:: python
    :emphasize-lines: 9-19, 30, 33-34

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
                """
                {% from 'plots/utils.html' import render_img %}
                {{ render_img(data=data, alt_img='my_img') }}
                """,
                data=data,
            )


.. code-block:: python
    :emphasize-lines: 10-18, 26, 29-30

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
                """
                {% from 'plots/utils.html' import render_img %}
                {{ render_img(data=data, alt_img='my_img') }}
                """,
                data=data,
            )

.. code-block:: python
    :emphasize-lines: 6-11, 14, 17-18

    @app.route("/hist2d")
    def hist2d():
        # plots:
        fig = Figure()
        ax = fig.subplots()
        ax = plots.hist2d(
            fig,
            x=np.random.normal(size=100),
            y=np.random.normal(size=100),
            hist2d_kws={"cmap": "inferno"},
        )
        ax.set_title("Hist2d Plot")
        ax.set_xlabel("Label for X!")
        data = plots.get_data(fig)
        return render_template_string(
            """
            {% from 'plots/utils.html' import render_img %}
            {{ render_img(data=data, alt_img='my_img') }}
            """,
            data=data,
        )

.. code-block:: python
    :emphasize-lines: 10-15, 18, 21, 22

    @app.route("/hexbin")
    def hexbin():
        # make data: correlated + noise
        np.random.seed(1)
        x = np.random.randn(5000)
        y = 1.2 * x + np.random.randn(5000) / 3
        # plots:
        fig = Figure()
        ax = fig.subplots()
        ax = plots.hexbin(
            fig=fig,
            x=x,
            y=y,
            hexbin_kws={"cmap": "inferno", "gridsize": 20},
        )
        ax.set(xlim=(-2, 2), ylim=(-3, 3))
        ax.set_title("Hexbin Chart")
        data = plots.get_data(fig)
        return render_template_string(
            """
            {% from 'plots/utils.html' import render_img %}
            {{ render_img(data=data, alt_img='my_img') }}
            """,
            data=data
        )

.. code-block:: python
    :emphasize-lines: 6-16, 24, 27-28

    @app.route("/pie")
    def pie():
        # plots:
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
                """
                {% from 'plots/utils.html' import render_img %}
                {{ render_img(data=data, alt_img='my_img') }}
                """,
                data=data,
            )


.. _Matplotlib: https://matplotlib.org/devdocs/index.html
