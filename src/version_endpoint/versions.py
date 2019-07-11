# -*- coding: utf-8 -*-
"""versions module for version_endpoint package.

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
from pkg_resources import get_distribution


def get_version(package_name):
    """Return the version of the requested package."""
    return get_distribution(package_name).version


def get_versions(package_names=None):
    """Return the installed versions of the given package names.

    :param package_names: iterable of package names to get installed version
        for
    :return: {dict} Dictionary with package name as key and version as value
    """
    package_names = package_names or []
    return {
        pkg_name: get_version(pkg_name)
        for pkg_name in package_names
    }
