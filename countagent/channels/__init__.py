"""Chat channels module with plugin architecture."""

from countagent.channels.base import BaseChannel
from countagent.channels.manager import ChannelManager
from countagent.channels.registry import discover_all, discover_channel_names

__all__ = ["BaseChannel", "ChannelManager", "discover_all", "discover_channel_names"]
