.. _settings:

Settings
--------
version_endpoint is configured by adding the following settings to the Django
settings.

.. py:attribute:: PACKAGE_NAMES

      The packages, that are returned in the list endpoint.

      Default
         :code:`['django-version-endpoint', 'Django']`

      Examples::

         VERSION_ENDPOINT_PACKAGE_NAMES = ['Django', 'djangorestframework']

.. py:attribute:: ALLOWED_PACKAGE_NAMES

      The packages, that might be returned by requesting the single package
      endpoint. Other packages return a forbidden response.

      Default
         :code:`PACKAGE_NAMES`

      Examples::

        ALLOWED_PACKAGE_NAMES = ['Django',]
