from version_endpoint.versions import get_versions


def test_versions():
    output = get_versions(['django-version-endpoint'])
    assert output['django-version-endpoint']
