# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'homeenergymodel.dev'
copyright = '2025, Steven Firth'
author = 'Steven Firth'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode'
    ]



import sys
p = r'C:\Users\cvskf\OneDrive - Loughborough University\_Git\stevenkfirth\homeenergymodel\docs\HEM_v0.36_FHS_v0.27'
if not p in sys.path: sys.path.append(p)
p = r'C:\Users\cvskf\OneDrive - Loughborough University\_Git\stevenkfirth\homeenergymodel\docs\HEM_v0.36_FHS_v0.27\src'
if not p in sys.path: sys.path.append(p)

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store',
                    '_ignore/'
                    ]

html_extra_path = [
    'CNAME'   # This is needed to that the GitHub action copies this file to the gh-pages branch. This is used to link with the custom domain name (DNS).
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    #'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    #'analytics_anonymize_ip': False,
    #'logo_only': False,
    #'prev_next_buttons_location': 'bottom',
    #'style_external_links': False,
    #'vcs_pageview_mode': '',
    #'style_nav_header_background': 'white',
    #'flyout_display': 'hidden',
    #'version_selector': True,
    #'language_selector': True,
    ## Toc options
    #'collapse_navigation': True,
    #'sticky_navigation': True,
    'navigation_depth': 10,
    #'includehidden': True,
    #'titles_only': False
}


html_static_path = ['_static']
