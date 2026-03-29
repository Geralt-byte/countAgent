"""Backward-compatible template rendering — delegates to resources.template_renderer."""

from countagent.resources.template_renderer import render_template

__all__ = ["render_template"]
