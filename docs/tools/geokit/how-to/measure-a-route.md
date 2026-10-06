# Measure the length of a route

**Goal:** get the total distance of a route given as a list of coordinates.

```python
from geokit import haversine

route = [(48.8566, 2.3522), (50.8503, 4.3517), (52.3676, 4.9041)]  # Paris, Brussels, Amsterdam

total = sum(haversine(*a, *b) for a, b in zip(route, route[1:]))
print(f"{total:.0f} km")
```

```{tip}
For millions of segments on a GPU machine, use {func}`geokit.accel.batch_haversine` instead.
```

See also {func}`geokit.haversine` in the reference.
