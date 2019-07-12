django-version-endpoint
=======================

> Provide an endpoint to query installed python package versions

.. image:: https://travis-ci.org/propylon/django-version-endpoint.svg?branch=master
    :target: https://travis-ci.org/propylon/django-version-endpoint

Usage
-----

Installation
************
1. Install the package::

    pip install django-version-endpoint

2. Install the application by adding it to the INSTALLED_APPS setting::

    INSTALLED_APPS += ('version_endpoint',)

3. Set the package names, you're interested in::

    VERSION_ENDPOINT_PACKAGE_NAMES = (
        'all',
        'interesting',
        'packages'
    )

4. Add the url to your urls.py::

    from django.conf.urls import include

    urlpatterns += url(r'^', include('version_endpoint.urls'))

Endpoints
*********

versions/
^^^^^^^^^
You can call the "versions" endpoint to get the information about the installed
package versions.

Request a content type of "application/json" and a dictionary is returned::

    {
        'versions': {
            'all': '1.1',
            'interesting': '2.2',
            'packages': '3.3'
        },
        'host': 'hostname'
    }

Otherwise a rendered html page is returned.

versions/<package_name>/
^^^^^^^^^^^^^^^^^^^^^^^^
The versions endpoint can get a single package name as well to specifically
return the mentioned package's version.

Overwriting the template
************************
In order to overwrite the html template for your needs, just create a template
called "version_endpoint.html" in your project, that's retrieved before the
default one of the application.
For example with the standard template loader and directory in the project's
folder under a "templates" folder.
You can use the dictionary mentioned above as context for the template.

If you want to override the html response for the single package endpoint, you
can do the same for the "version_endpoint_single.html" template.

Development
-----------

Makefile
********

This project uses a Makefile for various tasks. Some of the available tasks
are listed below.

* `make clean` - Clean build artifacts out of your project
* `make test` - Run Tests
* `make plain-test` - Run Tests without rebuilding the project
* `make sdist` - Build a Python source distribution
* `make docs` - Build the Sphinx documentation
* `make lint` - Get a codestyle report about your code
* `make plain-lint` - Get a codestyle report without rebuilding the project
* `make` - Equivalent to `make test lint docs sdist`
