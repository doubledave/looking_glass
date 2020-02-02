import inspect
import types
from typing import cast


def caller_name() -> str:
    """Return the calling function's name."""
    # Ref: https://stackoverflow.com/a/57712700/
    return cast(types.FrameType, inspect.currentframe()).f_back.f_code.co_name


if __name__ == '__main__':
    def _test_caller_name() -> None:
        assert caller_name() == '_test_caller_name'
    _test_caller_name()