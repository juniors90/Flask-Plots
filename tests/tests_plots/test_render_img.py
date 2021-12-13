from flask import render_template_string
from matplotlib.figure import Figure
import pytest as pt


def test_render_img(app, client, plots):
    @app.route("/render-image")
    def render_image():
        # Generate the figure **without using pyplot**.
        fig = Figure()
        ax = fig.subplots()
        ax.plot([-1, 4])
        ax.set_title("Linear Function")
        # Embed the result in the html output.
        data_img = plots.get_data(fig)
        return render_template_string(
            """{% from 'plots/utils.html' import render_img %}
            {{ render_img(data=data, alt_img='some_img') }}
            """,
            data=data_img,
        )

    response = client.get("/render-image")
    data = response.get_data(as_text=True)
    assert '<img src="data:image/png;base64,' in data
    assert 'alt="some_img"/>' in data

    @app.route("/render-image-with-class")
    def render_image_with_class():
        # Generate the figure **without using pyplot**.
        fig = Figure()
        ax = fig.subplots()
        ax.plot([1, 4])
        ax.set_title("Linear Function 2")
        # Embed the result in the html output.
        data_img = plots.get_data(fig)
        return render_template_string(
            """{% from 'plots/utils.html' import render_img %}
            {{ render_img(data=data, alt_img='some_img', class_img='ui') }}
            """,
            data=data_img,
        )

    response = client.get("/render-image-with-class")
    data = response.get_data(as_text=True)
    assert '<img src="data:image/png;base64,' in data
    assert 'alt="some_img" class="ui"/>' in data

    @app.route("/render-image-with-style")
    def render_image_with_style():
        # Generate the figure **without using pyplot**.
        fig = Figure()
        ax = fig.subplots()
        ax.plot([1, -4])
        ax.set_title("Linear Function 3")
        # Embed the result in the html output.
        data_img = plots.get_data(fig)
        return render_template_string(
            """{% from 'plots/utils.html' import render_img %}
            {{ render_img(data=data, alt_img='my_img', style='float:right') }}
            """,
            data=data_img,
        )

    response = client.get("/render-image-with-style")
    data = response.get_data(as_text=True)
    assert '<img src="data:image/png;base64,' in data
    assert 'alt="my_img" style="float:right"/>' in data

    with pt.raises(RuntimeError) as excinfo:

        @app.route("/render-image-with-runtimeerror")
        def render_image_with_runtimeerror():
            # Generate the figure **without using pyplot**.
            fig = Figure()
            ax = fig.subplots()
            ax.plot([1, -4])
            ax.set_title("Linear Function 3")
            # Embed the result in the html output.
            data_img = plots.get_data(fig)  # noqa
            return render_template_string(
                """{% from 'plots/utils.html' import render_img %}
            {{ render_img(data=data, alt_img='my_img', style='float:right') }}
            """  # , data=data_img
            )

        response = client.get("/render-image-with-runtimeerror")
        data = response.get_data(as_text=True)
        assert '<img src="data:image/png;base64,' not in data
        assert 'alt="my_img" style="float:right"/>' not in data
        assert "RuntimeError: You must send the data of the image." in data
        assert "RuntimeError: You must send the data of the image." in str(
            excinfo.value
        )
