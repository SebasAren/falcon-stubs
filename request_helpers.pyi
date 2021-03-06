# Stubs for falcon.request_helpers (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import io
from typing import Any, Optional

def header_property(wsgi_name: Any): ...

class BoundedStream(io.IOBase):
    stream: Any = ...
    stream_len: Any = ...
    def __init__(self, stream: Any, stream_len: Any) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next: Any = ...
    def readable(self): ...
    def seekable(self): ...
    def writeable(self): ...
    def read(self, size: Optional[Any] = ...): ...
    def readline(self, limit: Optional[Any] = ...): ...
    def readlines(self, hint: Optional[Any] = ...): ...
    def write(self, data: Any) -> None: ...
Body = BoundedStream
