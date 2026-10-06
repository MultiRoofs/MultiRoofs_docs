"""GPU-accelerated batch operations.

This module imports ``cupy``, a heavy GPU library. The docs build does not
install it: ``conf.py`` lists it in ``autodoc_mock_imports`` instead.
"""

from __future__ import annotations

import cupy as cp  # heavy dependency, mocked during the docs build


def batch_haversine(lats1, lons1, lats2, lons2, radius: float = 6371.0088):
    """Vectorised :func:`geokit.haversine` on the GPU.

    Args:
        lats1: Array of start latitudes, in degrees.
        lons1: Array of start longitudes, in degrees.
        lats2: Array of end latitudes, in degrees.
        lons2: Array of end longitudes, in degrees.
        radius: Sphere radius.

    Returns:
        A ``cupy.ndarray`` of distances.
    """
    p1, p2 = cp.radians(lats1), cp.radians(lats2)
    dp, dl = p2 - p1, cp.radians(lons2 - lons1)
    a = cp.sin(dp / 2) ** 2 + cp.cos(p1) * cp.cos(p2) * cp.sin(dl / 2) ** 2
    return 2 * radius * cp.arcsin(cp.sqrt(a))
