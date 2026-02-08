"""Domain exception hierarchy for countagent."""


class CountAgentError(Exception):
    """Base exception for all countagent errors."""


class ProviderError(CountAgentError):
    """LLM provider related errors."""


class ToolExecutionError(CountAgentError):
    """Tool execution failures."""


class SessionError(CountAgentError):
    """Session management errors."""


class ChannelError(CountAgentError):
    """Chat channel communication errors."""


class ConfigurationError(CountAgentError):
    """Configuration loading or validation errors."""


class SecurityViolationError(CountAgentError):
    """Security policy violation errors."""
