from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LetterResponse(_message.Message):
    __slots__ = ("a",)
    A_FIELD_NUMBER: _ClassVar[int]
    a: str
    def __init__(self, a: _Optional[str] = ...) -> None: ...

class LetterRequest(_message.Message):
    __slots__ = ("b",)
    B_FIELD_NUMBER: _ClassVar[int]
    b: str
    def __init__(self, b: _Optional[str] = ...) -> None: ...
