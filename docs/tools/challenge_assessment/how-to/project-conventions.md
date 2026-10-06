# Follow the project's NumPy conventions

- Import as `import numpy as np`.
- Create random generators with {func}`numpy.random.default_rng`, not the legacy
  `np.random.seed`. Pass a seed from the pipeline config so runs are reproducible.
- Use `float64` unless memory is a proven problem.

```{note}
The function names above link into the official NumPy docs. The links are
created by `sphinx.ext.intersphinx` and stay correct when NumPy reorganises its site.
```
