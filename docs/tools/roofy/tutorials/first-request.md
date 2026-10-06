# Make your first request

List the first five items:

::::{tab-set}
:::{tab-item} curl
```bash
curl "https://inventory.example.com/v1/items?limit=5"
```
:::
:::{tab-item} Python
```python
import json
import urllib.request

with urllib.request.urlopen("https://inventory.example.com/v1/items?limit=5") as r:
    print(json.load(r))
```
:::
::::
