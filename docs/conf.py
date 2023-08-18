# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "SEW SCRIPT"
copyright = "2023, xiatian"
author = "xiatian_xjtu"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_copybutton",
    "sphinxemoji.sphinxemoji",
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "zh_CN"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["image"]
html_logo = "image/logo.svg"

html_theme_options = {
    'logo_only': True,
}

sphinxemoji_style = "twemoji"

# Extensions to theme docs
def setup(app):
    from sphinx.domains.python import PyField
    from sphinx.util.docfields import Field

    app.add_object_type(
        'declaration',
        'declaration',
        objname='declaration',
        indextemplate='pair: %s; declaration',
        doc_field_types=[
            PyField(
                'para',
                label= '参数',
                has_arg=False,
                names=('para',),
                bodyrolename='class'
            ),
            Field(
                'return',
                label = '返回值',
                has_arg=False,
                names=('return',),
            ),
        ]
    )
