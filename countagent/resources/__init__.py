"""Built-in resources: templates, skills, and web assets."""

from countagent.resources.skills_loader import SkillsLoader, BUILTIN_SKILLS_DIR
from countagent.resources.template_renderer import TemplateRenderer

__all__ = ["SkillsLoader", "BUILTIN_SKILLS_DIR", "TemplateRenderer"]
