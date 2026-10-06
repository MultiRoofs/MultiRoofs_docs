# Why NumPy

Pipeline steps process millions of coordinates. NumPy arrays let geokit and the
pipelines vectorise that work instead of looping in Python.

## Gotchas we have hit

- Integer overflow is silent for fixed-size integer arrays. Cast to `int64` before summing counts.
- {func}`numpy.mean` of an empty array returns `nan` with a warning, not an error.
