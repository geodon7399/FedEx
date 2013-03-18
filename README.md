<h1><b>FedEx Day #1</b></h1>

Utilize the matLibPlot library to create visualizations of data in two-dimensional chart form. Commuter time data downloaded from the census was used to demonstrate the library's capability.

<b>Goal of the Project</b>
<hr>
The goal of the project was to successfully utilize the library and create "a" visualization of the data via scatter plot or heat map.

<b>Before Getting Started</b>
<hr>
The matLibPlot library has dependencies. To properly setup, install the following in the order listed (for Win7).

    Python 2.6 or higher - http://python.org/download/releases/
    numpy 1.7.0 - https://pypi.python.org/pypi/numpy
    matLibPlot 1.2.0 - http://matplotlib.org/downloads.html

Arguments

    Feature Class: the name of the Feature Class you wish to export
    Output Location: the folder location where the output file will be generated
    CSV|JSON|GeoJSON: file type you wish to create; Default is GeoJSON
    Delimiter: Optional - if you select CSV, you will need to select a delimiter; the default is "|"

License

GPLv3 or later.
Issues

    Need to work on error trapping a bit more
    This does not handle blob fields, or raster fields
    Need to document python version; not sure how compatible it is with all current versions
    Developed in ArcGIS 10.0

