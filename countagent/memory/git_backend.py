"""Git-backed version control for memory — re-exports from utils."""

from countagent.utils.git_backend import GitStore, CommitInfo, LineAge

__all__ = ["GitStore", "CommitInfo", "LineAge"]
