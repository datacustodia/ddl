"""Structured JSON payload for automation workflows.

Every helper script in this package prints a single JSON
object on stdout. Workflows read the object via
``${{ steps.<id>.outputs.payload }}`` and act on the fields.
Keeping the shape stable makes it easy to add new workflows
without re-parsing the script output.

Standard fields:

  - ``action``          : ``"close-and-comment"``,
                          ``"label-only"`` or ``"error"``.
  - ``authorized``      : ``True`` iff the action should
                          proceed.
  - ``author``          : GitHub login of the PR author.
  - ``core_developers`` : sorted list of core developers.
  - ``is_core_developer``: ``author in core_developers``.
  - ``message``         : human-readable explanation that
                          workflows may echo into the run log.
  - ``comment``         : optional Markdown body for
                          posting on the PR (when action is
                          ``"close-and-comment"``).
  - ``label``           : optional label to apply.
  - ``comment_marker``  : optional HTML comment marker used
                          by workflows to detect a bot-managed
                          comment when re-running.

The class ``Payload`` is a thin wrapper around ``dict`` that
guards against accidental field-name typos via ``__getattr__``.
"""
from __future__ import annotations

from typing import Any, Iterable


class Payload(dict):
    """A ``dict`` subclass with attribute-style access and a
    stable ``to_json()`` serialiser."""

    __slots__ = ()

    def __getattr__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError:
            raise AttributeError(
                f"Payload has no field {name!r}"
            ) from None

    def to_json(self) -> str:
        """Return the JSON string with ``ensure_ascii=False``
        so non-ASCII content (e.g. Simplified Chinese, Japanese)
        is preserved in workflow logs."""
        import json
        return json.dumps(self, ensure_ascii=False)


def make_authorization_payload(
    *,
    action: str,
    authorized: bool,
    author: str,
    core_developers: Iterable[str],
    is_core_developer: bool,
    message: str,
    label: str | None = None,
    comment: str | None = None,
    comment_marker: str | None = None,
    extra: dict | None = None,
) -> Payload:
    """Build the standard payload used by every workflow in this
    package. Field semantics are described in the module
    docstring."""
    out: Payload = Payload()
    out["action"] = action
    out["authorized"] = authorized
    out["author"] = author
    out["core_developers"] = list(core_developers)
    out["is_core_developer"] = is_core_developer
    out["message"] = message
    if label is not None:
        out["label"] = label
    if comment is not None:
        out["comment"] = comment
    if comment_marker is not None:
        out["comment_marker"] = comment_marker
    if extra:
        for k, v in extra.items():
            if k in out:
                raise ValueError(
                    f"extra field {k!r} collides with reserved field"
                )
            out[k] = v
    return out