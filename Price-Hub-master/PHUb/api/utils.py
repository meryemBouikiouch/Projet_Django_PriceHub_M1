import pyproj

def convert_coords(x, y):
    transformer = pyproj.Transformer.from_crs("epsg:3857", "epsg:4326", always_xy=True)
    lon, lat = transformer.transform(x, y)
    return lat, lon
