"""Unified Jinja2 template renderer for agent prompts.

Agent prompts live in ``resources/templates/`` (pass names like ``agent/identity.md``).
"""

from functools import lru_cache
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader

TEMPLATES_ROOT = Path(__file__).resolve().parent / "templates"


@lru_cache
def _environment() -> Environment:
    return Environment(
        loader=FileSystemLoader(str(TEMPLATES_ROOT)),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )


class TemplateRenderer:
    """Stateless wrapper around the Jinja2 environment for agent templates."""

    def __init__(self, templates_root: Path | None = None) -> None:
        self._root = templates_root or TEMPLATES_ROOT
        self._env: Environment | None = None

    @property
    def env(self) -> Environment:
        if self._env is None or self._root != TEMPLATES_ROOT:
            self._env = Environment(
                loader=FileSystemLoader(str(self._root)),
                autoescape=False,
                trim_blocks=True,
                lstrip_blocks=True,
            )
        return self._env

    def render(self, name: str, *, strip: bool = False, **kwargs: Any) -> str:
        """Render *name* (e.g. ``agent/identity.md``) under ``templates/``."""
        text = self.env.get_template(name).render(**kwargs)
        return text.rstrip() if strip else text


def render_template(name: str, *, strip: bool = False, **kwargs: Any) -> str:
    """Module-level convenience: render ``name`` under ``resources/templates/``."""
    text = _environment().get_template(name).render(**kwargs)
    return text.rstrip() if strip else text
