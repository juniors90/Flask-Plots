# Flask-Plots

[![Build status](https://github.com/juniors90/Flask-Plots/actions/workflows/CI.yml/badge.svg)](https://github.com/juniors90/Flask-Plots/actions)
[![codecov](https://codecov.io/gh/juniors90/Flask-Plots/branch/main/graph/badge.svg?token=3DSLEQIE8A)](https://codecov.io/gh/juniors90/Flask-Plots)
[![docs](https://readthedocs.org/projects/flask-plots/badge/?version=latest)](https://flask-plots.readthedocs.io/en/latest/?badge=latest)
![docstr-cov](https://img.shields.io/endpoint?url=https://jsonbin.org/juniors90/Flask-Plots/badges/docstr-cov)
[![License](https://img.shields.io/github/license/juniors90/Flask-Plots)](https://github.com/juniors90/Flask-Plots/blob/main/LICENSE)
[![Forks](https://img.shields.io/github/forks/juniors90/Flask-Plots)](https://github.com/juniors90/Flask-Plots/network)
[![Stars](https://img.shields.io/github/stars/juniors90/Flask-Plots)](https://github.com/juniors90/Flask-Plots/stargazers)
[![Issues](https://img.shields.io/github/issues/juniors90/Flask-Plots)](https://github.com/juniors90/Flask-Plots/issues)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![https://github.com/leliel12/diseno_sci_sfw](https://img.shields.io/badge/DiSoftCompCi-FAMAF-ffda00)](https://github.com/leliel12/diseno_sci_sfw)

Flask-Plots is a library for creating and rendering static visualizations using [Matplotlib](https://matplotlib.org/stable/index.html) in Python.


## Requirements

Python 3.8+

## Dependecies for this project.

- [matplotlib(>=3.4.0)](https://matplotlib.org/) for plots management
- [Flask(>=2.0.2)](https://flask.palletsprojects.com/en/2.0.x/) for build the backend.

## intallation

You can install via pip:

```cmd
    $> pip install Flask-Plots
```
   
For development, clone the [official github repository](https://github.com/juniors90/Flask-Plots) instead and use:

```cmd
    $ git clone git@github.com:juniors90/Flask-Plots.git
    $ cd Flask-Plots
    $ python3 -m venv venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements/dev.txt
```

## Quick start

With Flask-Plots you can instance the ``Plots`` object and document your endpoints.


```python
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
        # Make data:
        countries = ["Argentina", "Brasil", "Colombia", "Chile"]
        peoples = [14, 40, 16, 24]
        # Plot:
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
```

## Links

- [Documentation](https://flask-plots.readthedocs.io)
- [Example Application](https://github.com/juniors90/Flask-Plots/tree/main/sample_app)
- [PyPI Releases](https://pypi.org/project/Flask-Plots/)
- [Changelog](https://github.com/juniors90/Flask-Plots/blob/main/CHANGELOG.rst)


## Authors

- Ferreira, Juan David

Please submit bug reports, suggestions for improvements and patches via
the (E-mail: juandavid9a0@gmail.com).

## Official repository and Issues

- https://github.com/juniors90/flask-Plots

## Acknowledgment

Thank you to Juan B. Cabral, and Martin Chalela for his teachings during [Curso doctoral FAMAF: Diseño de software para cómputo científico](https://github.com/leliel12/diseno_sci_sfw),
from which this library is based.

## License

`Flask-Plots` is free software you can redistribute it and/or modify it
under the terms of the MIT License. For more information, you can see the
[LICENSE](https://github.com/juniors90/Flask-Plots/blob/main/LICENSE) file
for details.
