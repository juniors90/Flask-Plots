Basic Usage
===========

Installation
-------------

.. code-block:: bash
    
    $ pip install flask-plots



To get started, the first step is to import and load the extension

.. code-block:: python

    from flask import Flask
    from flask_plots import Plots

    def create_app():
        app = Flask(__name__)
        Plots(app)
        return app

    # do something with app...

Sample Application
------------------

If you want to have a look at a small sample application, try `browsing it on
github <https://github.com/juniors90/Flask-Plots/tree/main/sample_app>`_.

.. _macros_list:

Configurations
--------------

+-----------------------------+------------------------+-----------------------------------------------------------------+
| Configuration Variable      | Default Value          | Description                                                     |
+=============================+========================+=================================================================+
| PLOTS_CMAP                  | ``'Greys'``            | If set to ``Greys`` and will be used for cmap value in plots.   |
+-----------------------------+------------------------+-----------------------------------------------------------------+
| STATIC_FOLDER               | ``'plots'``            | Default static folder.                                          |
+-----------------------------+------------------------+-----------------------------------------------------------------+
| BAR_HEIGHT                  | ``50``                 | Default bar height                                              |
+-----------------------------+------------------------+-----------------------------------------------------------------+

Macros
------

+---------------------------+----------------------------+--------------------------+
| Macro                     | Templates Path             | Description              |
+===========================+============================+==========================+
| render_img()              | plots/utils.html           | Render a img tag HTML    |
+---------------------------+----------------------------+--------------------------+

How to use this macro? It's quite simple, just import them from the
corresponding path and call them like any other macro:

.. code-block:: jinja

    {% from 'plots/utils.html' import render_img %}

    {{ render_img(data) }}

Go to the :doc:`macros` page to see the detailed usage for these macros.