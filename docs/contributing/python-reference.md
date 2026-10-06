# Add the API reference of a Python tool

The API reference of Python tools is generated from the docstrings in the source
code by [sphinx-autoapi](https://sphinx-autoapi.readthedocs.io/).
**The tool is never installed.** During the build, its repository is cloned with
`git` and the files are read as text. This means:

- No dependencies of your tool are needed, including GPU or compiled libraries.
- Code that only works at runtime is not seen (for example functions created
  dynamically). Normal functions, classes, methods, constants and type hints work.


## Step 1. Register the tool in `docs/python-tools.toml`

Add one entry for your tool:

```toml
[my_tool]
repo = "https://github.com/your-org/my-tool"
ref  = "v1.4.0"
path = "src/my_tool"
```

| Key | Meaning |
|---|---|
| `[my_tool]` | The **Python package name** (what users `import`). Use underscores if the package does. |
| `repo` | Address of the GitHub repository. It must be public. |
| `ref` | Tag or branch to document. Use a release tag (`v1.4.0`) for stable docs, or `main` to always show the latest code. A commit hash is not supported. |
| `path` | Folder of the package inside the repository: the folder that contains `__init__.py`. Usually `src/my_tool` or `my_tool`. |

To try the reference with code that is not pushed yet, use a local folder instead
of `repo`, `ref` and `path` (the path is relative to `docs/`):

```toml
[my_tool]
local = "../../my-tool/src/my_tool"
```

Switch back to `repo` before you open a pull request: the build on GitHub cannot
see your computer.

## Step 2. Link the generated pages from your reference page

The pages are generated in `docs/api/<package>/`. Point to them from
`docs/tools/<your-tool>/reference/index.md`:

````markdown
# API reference

Generated from the my-tool source code.

```{toctree}
:maxdepth: 2

/api/my_tool/index
```
````

The leading `/` matters: it means "from the root of `docs/`".

## Step 3. Build and check

```bash
sphinx-build -b html docs docs/_build/html
```

Then open your tool's reference page. The first build clones the repository into
`docs/_sources/my_tool/`. Both `docs/_sources/` and `docs/api/` are rebuilt
automatically and are not committed.

## Write docstrings the reference can use

Use **Google style**, the convention for all in-house tools:

```python
def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Compute the great-circle distance between two points.

    Args:
        lat1: Latitude of the first point, in degrees.
        lon1: Longitude of the first point, in degrees.
        lat2: Latitude of the second point, in degrees.
        lon2: Longitude of the second point, in degrees.

    Returns:
        Distance in kilometres.

    Raises:
        ValueError: If a latitude is outside [-90, 90].
    """
```

What appears in the reference:

- Every public module, class, function, method and constant. Names starting with
  `_` are hidden.
- Type hints from the function signature.
- Objects listed in `__all__` of a package are shown at package level too.

## Troubleshooting

| Problem | Fix |
|---|---|
| Build stops with `no package at ...` | `path` does not point to the folder containing `__init__.py`. |
| Build stops with a `git clone` error | Check `repo` and that `ref` exists as a tag or branch. The repository must be public. |
| Reference shows an old version | Delete `docs/_sources/<package>/` and build again. This happens locally when `ref` is a branch. On GitHub every build starts clean. |
| A page is empty | The module has no public members, or they all start with `_`. |
