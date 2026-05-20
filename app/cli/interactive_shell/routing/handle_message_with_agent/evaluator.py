"""High-level message routing pipeline for non-command input."""

from __future__ import annotations

from app.cli.interactive_shell.routing.types import RouteDecision, RouteKind, RoutingSession


def _looks_like_cli_agent_action_plan(text: str) -> bool:
    lowered = text.lower()
    return (
        "run synthetic test" in lowered
        or "deploy" in lowered
        or "connected services" in lowered
        or "switch to " in lowered
    )


def handle_message_with_agent(
    text: str,
    session: RoutingSession,
) -> RouteDecision:
    """Resolve non-command input to the CLI agent route."""
    _ = session

    matched_signals = ("cli_agent_action_plan",) if _looks_like_cli_agent_action_plan(text) else ()

    return RouteDecision(
        RouteKind.CLI_AGENT,
        0.88,
        matched_signals,
        None,
    )
