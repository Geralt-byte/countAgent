"""AppContext composition root (lightweight DI container)."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from countagent.core.bus import MessageBus


@dataclass
class AppContext:
    """Unified composition root managing component lifecycle."""

    bus: MessageBus = field(default_factory=MessageBus)
    _provider: Any = None
    _tool_registry: Any = None
    _session_manager: Any = None
    _config: Any = None

    @property
    def provider(self) -> Any:
        return self._provider

    @provider.setter
    def provider(self, value: Any) -> None:
        self._provider = value

    @property
    def tool_registry(self) -> Any:
        return self._tool_registry

    @tool_registry.setter
    def tool_registry(self, value: Any) -> None:
        self._tool_registry = value

    @property
    def session_manager(self) -> Any:
        return self._session_manager

    @session_manager.setter
    def session_manager(self, value: Any) -> None:
        self._session_manager = value

    @property
    def config(self) -> Any:
        return self._config

    @config.setter
    def config(self, value: Any) -> None:
        self._config = value
