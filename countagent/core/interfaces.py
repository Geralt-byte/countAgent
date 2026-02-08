"""Domain boundary abstract base classes."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class AbstractLLMProvider(ABC):
    """Contract for LLM provider implementations."""

    @abstractmethod
    async def chat(self, messages, tools=None, model=None, max_tokens=4096,
                   temperature=0.7, reasoning_effort=None, tool_choice=None):
        ...

    @abstractmethod
    async def chat_stream(self, messages, tools=None, model=None, max_tokens=4096,
                          temperature=0.7, reasoning_effort=None, tool_choice=None,
                          on_content_delta=None):
        ...

    @abstractmethod
    def get_default_model(self) -> str:
        ...


class AbstractChannel(ABC):
    """Contract for chat platform channel implementations."""

    @abstractmethod
    async def start(self) -> None:
        ...

    @abstractmethod
    async def stop(self) -> None:
        ...

    @abstractmethod
    async def send_message(self, chat_id: str, text: str, **kwargs: Any) -> None:
        ...


class AbstractTool(ABC):
    """Contract for agent tool implementations."""

    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def description(self) -> str:
        ...

    @abstractmethod
    def get_schema(self) -> dict[str, Any]:
        ...

    @abstractmethod
    async def execute(self, **kwargs: Any) -> str:
        ...


class AbstractMemoryStore(ABC):
    """Contract for memory store implementations."""

    @abstractmethod
    async def save(self, key: str, value: str) -> None:
        ...

    @abstractmethod
    async def load(self, key: str) -> str | None:
        ...
