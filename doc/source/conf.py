# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))  # Lägger till projektroten till sys.path

project = 'Project1'
copyright = '2025, Jeyson Hussein Mario'
author = 'Jeyson Hussein Mario'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',         # För automatisk dokumentation av Python-funktioner och klasser
    'sphinx.ext.napoleon',        # För att hantera Google-style docstrings
    'sphinx_autodoc_typehints',   # För att inkludera typinformation i dokumentationen
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

