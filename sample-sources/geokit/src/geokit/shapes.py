"""Planar shapes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class Point:
    """A point in the plane.

    Attributes:
        x: Horizontal coordinate.
        y: Vertical coordinate.
    """

    x: float
    y: float

    def distance_to(self, other: Point) -> float:
        """Return the Euclidean distance to ``other``.

        Args:
            other: The other point.

        Returns:
            The straight-line distance.
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Polygon:
    """A simple (non self-intersecting) polygon.

    Args:
        vertices: Corner points in order. At least three are required.

    Raises:
        ValueError: If fewer than three vertices are given.
    """

    def __init__(self, vertices: Sequence[Point]) -> None:
        if len(vertices) < 3:
            raise ValueError("a polygon needs at least 3 vertices")
        self.vertices: list[Point] = list(vertices)

    def area(self) -> float:
        """Return the area using the shoelace formula."""
        v = self.vertices
        s = sum(v[i].x * v[(i + 1) % len(v)].y - v[(i + 1) % len(v)].x * v[i].y
                for i in range(len(v)))
        return abs(s) / 2

    def perimeter(self) -> float:
        """Return the total length of all edges."""
        v = self.vertices
        return sum(v[i].distance_to(v[(i + 1) % len(v)]) for i in range(len(v)))
