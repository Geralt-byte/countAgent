"""
countagent - A lightweight AI agent framework
"""

from countagent._version import __version__

__all__ = ["CountAgent", "RunResult", "__version__"]


def __getattr__(name: str):
    if name == "CountAgent":
        from countagent.app import CountAgent
        return CountAgent
    if name == "RunResult":
        from countagent.app import RunResult
        return RunResult
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
