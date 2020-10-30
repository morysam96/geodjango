# geodjango
near by shops maragheh city

-first install plugin files requirements
-if gdal package is install in the pc ,first directory gdal change to your directory gdal (settings.py >D:\QGIS 3.4)
-postgresql information (database name geodjango , user shopadmin , password shoppass , port 5432 , host localhost )
-for import maragheh.json to database use of  function load_data 0002_auto_20201030_1243.py


# OSGeo4W
The OSGeo4W installer(https://trac.osgeo.org/osgeo4w/) helps to install the PROJ.4, GDAL, and GEOS libraries required by GeoDjango. First, download
the OSGeo4W installer, and run it. Select Express Web-GIS Install and click next. In the ‘Select Packages’ list,
ensure that GDAL is selected; MapServer and Apache are also enabled by default, but are not required by GeoDjango
and may be unchecked safely. After clicking next, the packages will be automatically downloaded and installed, after
which you may exit the installer.
