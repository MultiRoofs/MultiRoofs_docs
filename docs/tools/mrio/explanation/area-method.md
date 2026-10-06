# How areas are computed

`footprintArea` projects the ring onto a flat plane centred on the building
(equirectangular approximation) and applies the shoelace formula. For a single
building the error is negligible. It is not meant for large areas such as districts.
