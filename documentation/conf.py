# Template for the configuration file for the Sphinx documentation generator.

# Change these to the correct values for your project.

root_doc = "index"
project = "Tooling Demo Nanobind"
copyright = "2024-2026 Rogier van Dalen"
version = "0.0.2"
release = "0.0.2"

# Add any Sphinx extension module names here, as strings.
# They also need to be added in ./BUILD.bazel to sphinx_build_binary(deps=...).

extensions = ["sphinx.ext.imgmath", "sphinx.ext.todo"]

pygments_style = "sphinx"
html_theme = "nature"
templates_path = ["_templates"]


source_suffix = ".rst"
