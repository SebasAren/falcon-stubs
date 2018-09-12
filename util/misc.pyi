# Stubs for falcon.util.misc (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class DeprecatedWarning(UserWarning): ...

def deprecated(instructions: Any): ...
def http_now(): ...
def dt_to_http(dt: Any): ...
def http_date_to_dt(http_date: Any, obs_date: bool = ...): ...
def to_query_str(params: Any, comma_delimited_lists: bool = ..., prefix: bool = ...): ...
def get_bound_method(obj: Any, method_name: Any): ...
def get_argnames(func: Any): ...
def get_http_status(status_code: Any, default_reason: str = ...): ...