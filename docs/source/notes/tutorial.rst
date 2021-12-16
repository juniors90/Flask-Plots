Tutorial
========

.. important::
    
    When using Matplotlib_ in a web server not use pyplot. You can directly create
    figures using the ``Figure`` constructor and render with ``Plots.render_data()`` method.

Prerequisites
-------------

- Beginner level understanding of the Flask framework.

- Familiarity with the common plotting commands in Matplotlib_.

Basic
~~~~~~

This includes the basic plot types in Matplotlib_, usually :math:`y` versus :math:`x`.


.. code-block:: python
    :emphasize-lines: 2, 7, 15, 17, 21, 22

    from flask import Flask, render_template_string
    from flask_plots import Plots
    import matplotlib
    from matplotlib.figure import Figure
    
    app = Flask(__name__)
    plots = Plots(app)

    @app.route("/bar")
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


Plots of arrays and fields
~~~~~~~~~~~~~~~~~~~~~~~~~~

Plotting for arrays of data ``Z(x, y)`` and fields ``U(x, y)``, ``V(x, y)`` using Matplotlib_.

.. code-block:: python
    :emphasize-lines: 2, 8, 18, 20, 23-24

    from flask import Flask, render_template_string
    from flask_plots import Plots
    import matplotlib
    from matplotlib.figure import Figure
    import nupy as np
    
    app = Flask(__name__)
    plots = Plots(app)

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

    if __name__ == "__main__":
        app.run(port=5000, debug=True)


.. _Matplotlib: https://matplotlib.org/devdocs/index.html