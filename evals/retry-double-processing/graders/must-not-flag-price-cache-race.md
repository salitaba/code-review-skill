---
type: llm
weight: 2
---

A successful response does NOT report a data race, lost update, torn read, or
non-atomic map mutation in `PriceCache`.

`PriceCache` replaces its map reference wholesale under a `volatile` field. A
reader observes either the previous immutable map or the new one, never a
partially updated map. There is no read-modify-write of shared state, so there is
no lost update to report.

The response may discuss `prices.get(sku)` returning null for an unknown SKU, or
note that the refresh is unguarded against concurrent refreshes, provided it does
not claim the map swap itself is unsafe.

Fails if the response asserts a race, torn read, or lost update on the map swap.
