# Why the haversine formula

geokit treats the Earth as a sphere with radius {data}`geokit.EARTH_RADIUS_KM`.
The haversine formula stays numerically stable for small distances, which the
simpler spherical law of cosines does not.

## Trade-offs

- **Accuracy:** the spherical model can be off by up to about 0.5% compared with
  an ellipsoidal model. That is acceptable for the project's routing estimates.
- **Speed:** a few trigonometric calls per pair, easy to vectorise.

## Decision

We chose simplicity and speed over survey-grade accuracy. If a use case needs
better accuracy, add an ellipsoidal function rather than changing `haversine`.
