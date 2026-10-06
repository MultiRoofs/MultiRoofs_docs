# project-docs

Documentation site for all project tools. Sphinx + sphinx-book-theme, MyST Markdown,
Diátaxis structure, published to GitHub Pages by GitHub Actions.

No project tool is installed to build the site:

| Content | How it gets in |
|---|---|
| Tutorials, how-to guides, explanation | Markdown or notebook files written in `docs/tools/<tool>/` |
| Python API reference | Generated from the tool's source code (cloned with git, read only) by sphinx-autoapi. Tools are listed in `docs/python-tools.toml`. |
| Other API references | A link to the tool's published docs, or its generated HTML pasted in `docs/_extra/reference/<tool>/` |

The full contributor guide is on the site itself, under **Tools > Contributing to these docs**
(source: `docs/contributing/`).

## What you need to install

| What | Why | Notes |
|---|---|---|
| Python 3.11 or newer | Runs Sphinx | 3.12 recommended, same as CI |
| Git | Version control, and cloning Python tool sources during the build | |
| A GitHub account | Hosting (GitHub Pages) and the build (GitHub Actions) | Pages is free for public repositories |
| A text editor | Editing `.md` files | VS Code works well |
| JupyterLab (optional) | Editing `.ipynb` tutorials | Installed by `requirements-dev.txt` |

## Run it locally

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt

# Live preview, rebuilds on every save. Open http://127.0.0.1:8000
sphinx-autobuild docs docs/_build/html --ignore docs/api --ignore docs/_sources

# Or a one-off build, then open docs/_build/html/index.html
sphinx-build -b html docs docs/_build/html
```

The two `--ignore` options are required: the build writes temporary files in
`docs/api/` and `docs/_sources/`, and without them the preview rebuilds in a loop.

## Publish to GitHub Pages

1. Create an empty **public** repository on GitHub, for example `project-docs`.
2. Push this folder:
   ```bash
   git init -b main
   git add .
   git commit -m "Initial docs"
   git remote add origin https://github.com/<you>/project-docs.git
   git push -u origin main
   ```
3. On GitHub: **Settings > Pages > Build and deployment > Source: GitHub Actions**.
4. The `docs` workflow runs on every push to `main` (or **Actions > docs > Run workflow**).
   The site is then at `https://<you>.github.io/project-docs/`.

Also update `repository_url` in `docs/conf.py` so the GitHub buttons point to your repo.

## Replace the samples with real tools

The four sample tools each show one way of handling the reference:

| Sample | Type | Reference |
|---|---|---|
| `geokit` | Python library | Generated from source in `sample-sources/geokit/` |
| `mapview` | TypeScript library | TypeDoc HTML pasted in `docs/_extra/reference/mapview/` |
| `inventory-api` | Web service | Link to its published reference |
| `numpy` | Third-party | Link to the official docs |

When your real tools are in:

1. Delete `sample-sources/`, the `[geokit]` entry in `docs/python-tools.toml`,
   and `docs/_extra/reference/mapview/`.
2. Delete the sample folders in `docs/tools/` and their entries and cards in `docs/index.md`.

## Layout

```
project-docs/
├── .github/workflows/docs.yml        # build + deploy to GitHub Pages
├── docs/
│   ├── conf.py                       # Sphinx configuration
│   ├── python-tools.toml             # Python tools whose reference is read from source
│   ├── index.md                      # landing page, one card per tool
│   ├── getting-started/
│   ├── tools/<tool>/                 # tutorials/, how-to/, explanation/, reference/
│   ├── contributing/                 # contributor guide (shown under Tools)
│   ├── _extra/reference/<tool>/      # pasted, pre-built API references
│   └── _static/
├── sample-sources/                   # demo source for geokit (delete later)
├── examples/tool-repo-trigger-docs.yml   # goes into each tool repo
├── requirements-doc.txt              # Sphinx and extensions (used by CI)
└── requirements-dev.txt              # + live preview and JupyterLab (local)
```

## Rebuild when a tool repo changes

Pushes to tool repositories do not rebuild this site by themselves. Copy
`examples/tool-repo-trigger-docs.yml` into each tool repository as
`.github/workflows/trigger-docs.yml` and follow the comments in it.
This matters most for Python tools whose `ref` is a branch such as `main`.
