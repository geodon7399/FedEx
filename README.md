<h1><b>FedEx Day #1</b></h1>
Utilize the matLibPlot library to create visualizations of data in two-dimensional chart form.

<b>Background</b>
--------------------------
matplotlib is a Python library that simplifies the creation of plots, histograms, bar charts, and scatterplots to name a few. I stumbled onto this library and thought it would be interesting to investigate its capabilities in producing unique visualizations. I saw the potential value in it as it could suplement GIS analysis and would be beneficial to support decision making and planning.

<b>Goal of the Project</b>
--------------------------
The goal of the project was to successfully utilize the library and create "a" visualization of the data via scatter plot or heat map. I downloaded the TRAVEL TIME TO WORK dataset (BO8303) for Maryland counties from the Census Bureau's Factfinder search tool as a test. Click <a href="http://factfinder2.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=ACS_11_1YR_B08303&prodType=table">here</a> for the dataset. These are counts by county of workers 16 years and over who commute to work. It also has counts broken down into how long it takes to get to work (i.e 653 people commute 10-14 min that are from XYZ county).

<b>Setup and Configuration</b>
--------------------------
I used Eclipse IDE as the development environment to experiment with this project. I also installed the add-on, PyDev which enables you to create Python projects, set the type of project (Python, Jython, or Iron Python), set interpreter, add dependencies to the project and so on.

Python needs to be installed as well as dependecies for the matLibPlot library. To properly setup, install the following in the order listed (for Win7).

* Python 2.6 or higher - http://python.org/download/releases/
* numpy 1.7.0 - https://pypi.python.org/pypi/numpy
* matLibPlot 1.2.0 - http://matplotlib.org/downloads.html

Using the MSI installers are the easiest means of getting quickly setup. You can also download the tarballs and install manually via command line.


