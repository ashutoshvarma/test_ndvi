import rasterio
import numpy as np

def get_ndvi(redfp, nirfp, dest_path):
    band4 = rasterio.open(redfp, driver='JP2OpenJPEG') #red
    band8 = rasterio.open(nirfp, driver='JP2OpenJPEG') #NIR

    red = band4.read()
    nir = band8.read()

    def calc_ndvi(red, nir):
        # convert int band arrays to floats
        RED_a = red.astype(float)
        NIR_a = nir.astype(float)
        # Ignore divide by 0 warning
        np.seterr(divide='ignore', invalid='ignore')
        # calc ndvi
        ndvi = (NIR_a - RED_a)/(NIR_a + RED_a)
        return ndvi

    ndvi = calc_ndvi(red, nir)
    meta=band4.meta
    meta.update(driver='GTiff')
    meta.update(dtype=rasterio.float32)

    with rasterio.open(dest_path, 'w', **meta) as dst:
        dst.write(ndvi.astype(rasterio.float32))

