import version_endpoint
from version_endpoint.apps import VersionEndpointConfig


def test_app_initialization():
    assert VersionEndpointConfig('version_endpoint', version_endpoint)
