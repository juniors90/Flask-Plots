Basic Usage
===========

Installation
-------------

.. code-block:: bash
    
    $ pip install flask-plots


Initialization
----------------

To get started, the first step is to import and load the extension

.. code-block:: python
    
    from flask import Flask
    from flask_plots import Plots
    
    app = Flask(__name__)
    plots = Plots(app)

    # do something with app...

with ``create_app()`` factory

.. code-block:: python

    from flask import Flask
    from flask_plots import Plots

    def create_app():
        app = Flask(__name__)
        Plots(app)
        return app

    app = create_app()

    # do something with app...

Tutorial
--------

You can see :doc:`tutorial`.


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
| render_img()              | plots/utils.html           | Render a img HTML tag.   |
+---------------------------+----------------------------+--------------------------+

How to use this macro? It's quite simple, just import them from the
corresponding path and call them like this macro:

.. code-block:: jinja

    {% from 'plots/utils.html' import render_img %}
    {{ render_img(data, alt_img='my-image') }}

Go to the :doc:`macros` page to see the detailed usage for this macros.

  
.. raw:: html

    <form action="https://www.paypal.com/donate" method="post" target="_top">
      <input type="hidden" name="hosted_button_id" value="LFAQ7E7TJ4HSY" />
      <input
        type="image"
        src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif"
        border="0"
        name="submit"
        title="PayPal - The safer, easier way to pay online!"
        alt="Donate with PayPal button"
      />
      <img
        alt=""
        border="0"
        src="https://www.paypal.com/en_AR/i/scr/pixel.gif"
        width="1"
        height="1"
      />
    </form>
