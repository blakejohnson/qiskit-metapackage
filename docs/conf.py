# This code is part of Qiskit.
#
# (C) Copyright IBM 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

import datetime
import os
import sys

import sphinx.ext.doctest

sys.path.insert(0, os.path.abspath("."))

import custom_extensions
import versionutils

# -- General configuration ---------------------------------------------------

project = "Qiskit"
copyright = f"2017-{datetime.date.today().year}, Qiskit Development Team"
author = "Qiskit Development Team"

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = "0.43.1"

docs_url_prefix = "documentation"  # i.e., www.qiskit.org/documentation/

rst_prolog = """
.. |version| replace:: {0}
""".format(
    release
)

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "nbsphinx",
    "sphinx_design",
    "matplotlib.sphinxext.plot_directive",
    "qiskit_sphinx_theme",
    "sphinx.ext.doctest",
]

nbsphinx_timeout = 300
nbsphinx_execute = os.getenv("QISKIT_DOCS_BUILD_TUTORIALS", "never")
nbsphinx_widgets_path = ""
html_sourcelink_suffix = ""
exclude_patterns = ["_build", "**.ipynb_checkpoints"]

nbsphinx_thumbnails = {"**": "_static/images/logo.png"}

nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None) %}

.. only:: html
    
    .. role:: raw-html(raw)
        :format: html
    
    .. note::
        This page was generated from `{{ docname }}`__.

    __ https://github.com/Qiskit/qiskit-tutorials/blob/master/{{ docname }}

"""

panels_css_variables = {
    "tabs-color-label-active": "rgb(138, 63, 252)",
    "tabs-color-label-inactive": "rgb(221, 225, 230)",
}
templates_path = ["_templates"]

source_suffix = ".rst"
master_doc = "index"

# Number figures, tables and code-blocks if they have a caption.
numfig = True
# Available keys are 'figure', 'table', 'code-block' and 'section'.  '%s' is    the number.
numfig_format = {"table": "Table %s"}

language = "en"
translations_list = [
    ("en", "English"),
    ("bn_BN", "Bengali"),
    ("fr_FR", "French"),
    ("de_DE", "German"),
    ("ja_JP", "Japanese"),
    ("ko_KR", "Korean"),
    ("pt_UN", "Portuguese"),
    ("es_UN", "Spanish"),
    ("ta_IN", "Tamil"),
]
# For Adding Locale
locale_dirs = ["locale/"]  # path is example but recommended.
gettext_compact = False  # optional.

pygments_style = "colorful"

# Whether module names are included in crossrefs of functions, classes, etc.
add_module_names = False

# A list of prefixes that are ignored for sorting the Python module index
# (e.g., if this is set to ['foo.'], then foo.bar is shown under B, not F).
# This can be handy if you document a project that consists of a single
# package. Works only for the HTML builder currently.
modindex_common_prefix = ["qiskit."]


# -- Configuration for extlinks extension ------------------------------------
# Refer to https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
extlinks = {
    "pull_terra": ("https://github.com/Qiskit/qiskit-terra/pull/%s", "qiskit-terra #%s"),
    "pull_aer": ("https://github.com/Qiskit/qiskit-aer/pull/%s", "qiskit-aer #%s"),
    "pull_ibmq-provider": (
        "https://github.com/Qiskit/qiskit-ibmq-provider/pull/%s",
        "qiskit-ibmq-provider #%s",
    ),
}

# -- Options for HTML output -------------------------------------------------

html_theme = "qiskit_sphinx_theme"
html_theme_options = {
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}
html_favicon = "images/favicon.ico"
html_last_updated_fmt = "%Y/%m/%d"
html_context = {
    "analytics_enabled": os.getenv("QISKIT_ENABLE_ANALYTICS", False)
}  # enable segment analytics for qiskit.org/documentation

# -- Options for Autosummary and Autodoc ------------------------------------
# Note that setting autodoc defaults here may not have as much of an effect as  you may expect; any
# documentation created by autosummary uses a template file (in autosummary in  the templates path),
# which likely overrides the autodoc defaults.
autosummary_generate = True
autosummary_generate_overwrite = False
autoclass_content = "both"

# The pulse library contains some names that differ only in capitalisation, during the changeover
# surrounding SymbolPulse.  Since these resolve to autosummary filenames that also differ only in
# capitalisation, this causes problems when the documentation is built on an OS/filesystem that is
# enforcing case-insensitive semantics.  This setting defines some custom names to prevent the clash
# from happening.
autosummary_filename_map = {
    "qiskit.pulse.library.Constant": "qiskit.pulse.library.Constant_class.rst",
    "qiskit.pulse.library.Sawtooth": "qiskit.pulse.library.Sawtooth_class.rst",
    "qiskit.pulse.library.Triangle": "qiskit.pulse.library.Triangle_class.rst",
    "qiskit.pulse.library.Cos": "qiskit.pulse.library.Cos_class.rst",
    "qiskit.pulse.library.Sin": "qiskit.pulse.library.Sin_class.rst",
    "qiskit.pulse.library.Gaussian": "qiskit.pulse.library.Gaussian_class.rst",
    "qiskit.pulse.library.Drag": "qiskit.pulse.library.Drag_class.rst",
}

# Move type hints from signatures to the parameter descriptions (except in overload cases, where
# that's not possible).
autodoc_typehints = "description"
# Only add type hints from signature to description body if the parameter has documentation.  The
# return type is always added to the description (if in the signature).
autodoc_typehints_description_target = "documented_params"

# Plot directive configuration
# ----------------------------

plot_html_show_formats = False

# ---------------------------------------------------------------------------
# Doctest
# ---------------------------------------------------------------------------

# This option will make doctest ignore whitespace when testing code.
# It's specially important for circuit representation as it gives an
# error otherwise
doctest_default_flags = sphinx.ext.doctest.doctest.NORMALIZE_WHITESPACE

# Leaving this string empty disables testing of doctest blocks from docstrings.
# Doctest blocks are structures like this one:
# >> code
# output
doctest_test_doctest_blocks = ""


# -- Extension configuration -------------------------------------------------


def setup(app):
    custom_extensions.load_terra_docs(app)
    custom_extensions.load_tutorials(app)
    versionutils.setup(app)
    app.connect("build-finished", custom_extensions.clean_docs)
