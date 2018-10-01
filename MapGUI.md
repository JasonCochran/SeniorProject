# Map Research

### Basically we need to generate maps (vector or raster)

## Plan:
#### Create vector map tiles of Chicago
#### Automatically generate vector maps using PostGIS data (https://openmaptiles.org/docs/generate/custom-vector-from-postgis/)
#### Create a custom vector layer (https://openmaptiles.org/docs/raster/custom-raster/#prepare-map-style)
#### Combine Chicago and custom PostGIS vectors layers
#### Combining layers possibly:  https://openmaptiles.org/docs/raster/custom-raster/
#### Figure out how to update PostGIS data -> regen vector tiles -> regen overall map...
#### Create GUI to control which vector layers are shown  maybe? Or just have different vector maps
#### Generate a lot of vectors for info throughout time?

## Good documentation:
#### Discusses how to use Docker with OSM maps https://www.youtube.com/watch?v=JK-L3EvH3nk
#### Forcing Mapbox JS GL to use custom server https://stackoverflow.com/questions/45888989/how-to-use-openmaptiles-server-for-mapbox-gl-js
#### Adding Mapbox to Flask https://pengoox.pythonanywhere.com/How_to_Add_Maps_to_Flask_Web_App_with_Mapbox/
#### JS Code Examples to create layers https://www.mapbox.com/mapbox-gl-js/example/toggle-layers/
#### Caching JSON https://www.codebyamir.com/blog/a-web-developers-guide-to-browser-caching
#### Library to cache JSON client side https://github.com/jeremydurham/persist-js
