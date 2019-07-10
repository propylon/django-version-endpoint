# -*- coding: utf-8 -*-
"""Utility module for version_endpoint package.

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
import re


def get_accepted_content_types(request):
    """Return accepted content types for the request's response.

    Many thanks to https://stackoverflow.com/questions/
                   7459881/determine-the-requested-content-type
    """
    def qualify(raw_content_type):
        parts = raw_content_type.split(';', 1)
        if len(parts) == 2:
            match = re.match(
                r'(^|;)q=(0(\.\d{,3})?|1(\.0{,3})?)(;|$)',
                parts[1]
            )
            if match:
                return parts[0], float(match.group(2))
        return parts[0], 1

    raw_content_types = request.META.get('HTTP_ACCEPT', '*/*').split(',')
    qualified_content_types = map(qualify, raw_content_types)
    return (
        x[0] for x in sorted(
            qualified_content_types, key=lambda x: x[1], reverse=True
        )
    )
