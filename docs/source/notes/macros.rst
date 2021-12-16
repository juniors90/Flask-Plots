Use Macros
==========

These macros will help you to generate Plots-markup codes quickly and easily.

render_img()
------------

Render a image.

Example
~~~~~~~~

.. code-block:: python

    from flask import Flask, render_template
    from flask_plots import Plots
    from matplotlib.figure import Figure
    
    app = Flask(__name__)
    plots = Plots(app)
    
    @app.route("/")
    def hello():
        fig = Figure()
        ax = fig.subplots()
        # Data
        countries = ["Argentina", "Brasil", "Colombia", "Chile"]
        peoples = [14, 40, 16, 24]
        # Plotting
        ax = plots.bar(fig, countries, peoples)
        ax.set_title("Bar Chart")
        data = plots.get_data(fig)
        return render_template('index.html', data=data, alt="my-chart")

    if __name__ == "__main__":
        app.run(port=5000, debug=True)

in your ``index.html``:

.. code-block:: jinja

    {% from 'plots/utils.html' import render_img %}

    {{ render_img(data=data, alt_img='my_img', alt=alt) }}

API
~~~~

.. py:function:: render_img(data,\
                    alt_img,\
                    class_img=None,\
                    width=None,\
                    height=None,\
                    crossorigin=None,\
                    ismap=None,\
                    longdesc=None,\
                    referrerpolicy=None,\
                    sizes=None,\
                    srcset=None,\
                    usemap=None,\
                    style=None)
                    
    :param data: Data for contruct the path to the image.
    :param alt_img: Specifies an alternate text for an image.
    :param class_img: Add class style to image with CSS.
    :param width: Specifies the width of an image.
    :param height: Specifies the height (in pixeles) of an image.
    :param crossorigin: Allow images from third-party sites that allow
                        cross-origin access to be used with canvas.
    :param ismap: Specifies an image as a server-side image map.
    :param longdesc: Specifies a URL to a detailed description of an image.
    :param referrerpolicy: Specifies which referrer information to
                           use when fetching an image.
    :param sizes: Specifies image sizes for different page layouts.
    :param srcset: Specifies a list of image files to use in different situations.
    :param usemap: Specifies an image as a client-side image map.
    :param style: Add style to image with CSS.

See `tag img <https://www.w3schools.com/tags/tag_img.asp>`_.