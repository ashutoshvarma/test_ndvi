# ndvi
Simple Web App for NDVI Generator in Python

## Run (Local)

- ### Clone
    ```shell
    git clone https://github.com/ashutoshvarma/test_ndvi.git
    cd test_ndvi
    ```

- ### Install `rasterio`
    https://rasterio.readthedocs.io/en/latest/installation.html

- ### Setup Flask
    `pip install flask`

- ### Run
    `FLASK_DEBUG=true flask run`

## Note
All the uploads are save either in-memory (RAM) or temp file(will be deleted automatically)
so you don't need to worry about stray temp files.
Also output NDVI file is saved as `static/NDVI.tiff`. 