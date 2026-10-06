# Draw your first footprints

In this tutorial you create a map and draw two buildings.

## 1. Create the map

```ts
import { MapView } from "@your-org/mapview";

const view = new MapView({ container: "#map", center: [4.3571, 52.0116], zoom: 17 });
```

## 2. Add footprints

```ts
view.add([
  { id: "b1", ring: [[4.3570, 52.0115], [4.3573, 52.0115], [4.3573, 52.0117], [4.3570, 52.0117], [4.3570, 52.0115]], height: 12 },
  { id: "b2", ring: [[4.3575, 52.0115], [4.3577, 52.0115], [4.3577, 52.0118], [4.3575, 52.0118], [4.3575, 52.0115]] },
]);
```

Next: [compute a footprint's area](../how-to/footprint-area.md).
