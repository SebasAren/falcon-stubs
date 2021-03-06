# Stubs for falcon.testing.test_case (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import testtools as unittest
from falcon.testing.client import TestClient
from typing import Any

class TestCase(unittest.TestCase, TestClient):
    api_class: Any = ...
    @property
    def api(self): ...
    @api.setter
    app: Any = ...
    def api(self, value: Any) -> None: ...
    def setUp(self) -> None: ...
    def assertIn(self, a: Any, b: Any) -> None: ...
