"""Great-circle distance and bearing calculations."""

from __future__ import annotations

import math

#: Mean Earth radius in kilometres (IUGG value).
EARTH_RADIUS_KM: float = 6371.0088


def haversine(lat1: float, lon1: float, lat2: float, lon2: float,
              radius: float = EARTH_RADIUS_KM) -> float:
    """Compute the great-circle distance between two points.

    Args:
        lat1: Latitude of the first point, in degrees.
        lon1: Longitude of the first point, in degrees.
        lat2: Latitude of the second point, in degrees.
        lon2: Longitude of the second point, in degrees.
        radius: Sphere radius. Defaults to the mean Earth radius in km.

    Returns:
        Distance in the same unit as ``radius``.

    Raises:
        ValueError: If a latitude is outside ``[-90, 90]``.

    Example:
        >>> round(haversine(48.8566, 2.3522, 51.5074, -0.1278))
        344
    """
    for lat in (lat1, lat2):
        if not -90 <= lat <= 90:
            raise ValueError(f"latitude out of range: {lat}")
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * radius * math.asin(math.sqrt(a))


def bearing(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Compute the initial bearing from point 1 to point 2.

    Args:
        lat1: Latitude of the start point, in degrees.
        lon1: Longitude of the start point, in degrees.
        lat2: Latitude of the end point, in degrees.
        lon2: Longitude of the end point, in degrees.

    Returns:
        Bearing in degrees, clockwise from north, in ``[0, 360)``.
    """
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dl = math.radians(lon2 - lon1)
    x = math.sin(dl) * math.cos(p2)
    y = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl)
    return (math.degrees(math.atan2(x, y)) + 360) % 360
