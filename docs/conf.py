"""Sphinx configuration for the project documentation site."""

import shutil
import subprocess
import tomllib
from datetime import date
from pathlib import Path

DOCS_DIR = Path(__file__).parent

# -- Project information -----------------------------------------------------
project = "MultiRoofs Tools Documentation"
author = "MultiRoofs"
copyright = f"{date.today().year}, {author}"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.napoleon",        # Google-style docstrings
    "sphinx.ext.intersphinx",
    "myst_nb",                    # Markdown (MyST) pages and notebooks
    "sphinx_design",
    "sphinx_copybutton",
]

exclude_patterns = [
    "_build", "_sources", "_extra",
    "**.ipynb_checkpoints", "Thumbs.db", ".DS_Store",
]


# -- Python API reference (sphinx-autoapi) ------------------------------------
# Tools are listed in docs/python-tools.toml. Repositories are shallow-cloned
# into docs/_sources/ (git only, nothing is pip-installed) and read statically.
def _python_source_dirs() -> list[str]:
    tools = tomllib.loads((DOCS_DIR / "python-tools.toml").read_text())
    dirs = []
    for name, tool in tools.items():
        if "local" in tool:
            pkg = (DOCS_DIR / tool["local"]).resolve()
        else:
            dest = DOCS_DIR / "_sources" / name
            marker = dest / ".docs-ref"
            wanted = f"{tool['repo']}@{tool['ref']}"
            if not marker.exists() or marker.read_text() != wanted:
                shutil.rmtree(dest, ignore_errors=True)
                subprocess.run(
                    ["git", "-c", "advice.detachedHead=false", "clone", "--quiet", "--depth", "1",
                     "--branch", tool["ref"], tool["repo"], str(dest)],
                    check=True,
                )
                marker.write_text(wanted)
            pkg = dest / tool["path"]
        if not (pkg / "__init__.py").exists():
            raise FileNotFoundError(f"python-tools.toml [{name}]: no package at {pkg}")
        dirs.append(str(pkg))
    return dirs


autoapi_dirs = _python_source_dirs()
if autoapi_dirs:
    # Only load sphinx-autoapi when at least one Python tool is listed:
    # it stops the build if autoapi_dirs is empty.
    extensions.append("autoapi.extension")
autoapi_root = "api"                   # pages are generated in docs/api/<package>/
autoapi_add_toctree_entry = False      # each tool's reference page links to them
autoapi_keep_files = False
numfig = True
autoapi_member_order = "bysource"
autoapi_options = [
    "members", "undoc-members", "show-inheritance",
    "show-module-summary", "imported-members",
]
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_use_ivar = True               # avoids duplicate entries for documented attributes

# -- Links to external Sphinx docs ------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

# -- MyST / notebooks --------------------------------------------------------
myst_enable_extensions = ["colon_fence", "deflist", "fieldlist"]
myst_heading_anchors = 3
nb_execution_mode = "off"            # notebooks are committed with outputs

# -- HTML output -------------------------------------------------------------
html_theme = "sphinx_book_theme"
html_title = "MultiRoofs Tools Documentation"
html_logo = "_static/logo_text_horizontal-removebg-preview.png"
html_favicon = "_static/logo-removebg-preview.png"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
# Pasted, pre-built API references: docs/_extra/reference/<tool>/ is copied
# unchanged to <site>/reference/<tool>/.
html_extra_path = ["_extra"]
html_theme_options = {
    # Point these at your docs repository so the GitHub buttons work.
    "repository_url": "https://github.com/MultiRoofs/MultiRoofs_docs",
    "repository_branch": "main",
    "path_to_docs": "docs",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "show_toc_level": 2,
    "home_page_in_toc": True,
}
