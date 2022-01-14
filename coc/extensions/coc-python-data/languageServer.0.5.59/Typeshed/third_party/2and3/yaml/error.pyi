from typing import Any

class Mark:
    name = ...  # type: Any
    index = ...  # type: Any
    line = ...  # type: Any
    column = ...  # type: Any
    buffer = ...  # type: Any
    pointer = ...  # type: Any
    def __init__(self, name, index, line, column, buffer, pointer) -> None: ...
    def get_snippet(self, indent=..., max_length=...): ...

class YAMLError(Exception): ...

class MarkedYAMLError(YAMLError):
    context = ...  # type: Any
    context_mark = ...  # type: Any
    problem = ...  # type: Any
    problem_mark = ...  # type: Any
    note = ...  # type: Any
    def __init__(self, context=..., context_mark=..., problem=..., problem_mark=..., note=...) -> None: ...
