# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PAGOC MOOC - Guide Utilisateur'
copyright = '2025, PAGOC MOOC'
author = 'PAGOC MOOC'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [ 
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",   # permet Google/NumPy style docstrings
    "sphinx.ext.viewcode"   # ajoute un bouton "Voir le code"
    ]

templates_path = ['_templates']
exclude_patterns = []

language = 'Fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static', 'images']

# Configuration du thème personnalisé
html_css_files = [
    'custom.css',
]

# Options du thème Read the Docs
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
