# -*- coding: utf-8 -*-
"""views module for version_endpoint package.

Copyright 2019 Propylon Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from __future__ import unicode_literals

from django.http import HttpResponseForbidden, JsonResponse
from django.template.response import TemplateResponse

from .settings import ALLOWED_PACKAGE_NAMES, PACKAGE_NAMES
from .utils import get_accepted_content_types
from .versions import get_version, get_versions


def get_response(request, context, template):
    """Return a response based on the request's Accept Header.

    Dependent on the requested content type (and the order):
    * application/json: json response with version dict
    * text/html: html template
    * default representation: html template
    """
    for act in get_accepted_content_types(request):
        if act == 'application/json':
            return JsonResponse(context)
        elif act == 'text/html':
            return TemplateResponse(request, template, context)

    return TemplateResponse(request, template, context)


def versions_view(request):
    """Return the installed versions."""
    version_dict = {
        'versions': get_versions(PACKAGE_NAMES),
        'host': request.get_host()
    }

    return get_response(request, version_dict, 'version_endpoint.html')


def version_view(request, package_name):
    """Return a single installed version."""
    if package_name not in ALLOWED_PACKAGE_NAMES:
        return HttpResponseForbidden('querying package version is not allowed')

    version_dict = {'version': get_version(package_name)}
    return get_response(request, version_dict, 'version_endpoint_single.html')
