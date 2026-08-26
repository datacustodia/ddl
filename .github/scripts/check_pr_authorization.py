#!/usr/bin/env python3
# coding: utf-8
"""
Spam-Blocker Bot for the DDL-v1 project (entry point).

This script is the executable entry point that the GitHub
Actions workflow at ``.github/workflows/spam-blocker.yml``
invokes. It composes the helpers in this package:

  - ``codeowners`` : read ``.github/CODEOWNERS`` and resolve
    the set of core developers.
  - ``payload``    : build the structured JSON payload.
  - ``comment``    : render the closure comment body.

Behaviour:

  - Compares the PR author against the set of core
    developers.
  - If the author IS a core developer: emit a payload with
    ``action = "label-only"`` so the workflow applies the
    ``authorized-pr`` label.
  - If the author is NOT a core developer: emit a payload
    with ``action = "close-and-comment"`` so the workflow
    closes the PR and posts the closure comment.
  - On configuration or runtime errors: emit a payload with
    ``action = "error"`` and exit 0; the payload is still
    consumable by the workflow.

Environment variables:

  - ``PR_AUTHOR``       : GitHub login of the PR author
                          (required).
  - ``PR_NUMBER``       : PR number (optional; surfaced in
                          logs only).
  - ``PR_TITLE``        : PR title (optional; surfaced in
                          logs only).
  - ``REPOSITORY``      : ``"owner/repo"`` (default
                          ``"datacustodia/ddl"``).
  - ``CODEOWNERS_PATH`` : path to ``CODEOWNERS`` (default
                          ``.github/CODEOWNERS`` relative to
                          the package root).
  - ``ACTION``          : ``"check"`` (default) or any of the
                          actions enumerated in ``payload``.

Exit codes:

  - 0 : success; the JSON payload is on stdout.
  - 2 : ``PR_AUTHOR`` is missing.

The workflow consumes ``${{ steps.check.outputs.payload }}``
and drives the GitHub API from there.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# Support both ``python -m scripts.check_pr_authorization``
# (used by GitHub Actions) and direct ``python check_pr_authorization.py``
# (used by local smoke-tests).
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from scripts.codeowners import is_core_developer, parse_core_developers
    from scripts.comment import (
        COMMENT_MARKER,
        default_contributing_url,
        render_closure_comment,
    )
    from scripts.payload import make_authorization_payload
else:
    from .codeowners import is_core_developer, parse_core_developers
    from .comment import (
        COMMENT_MARKER,
        default_contributing_url,
        render_closure_comment,
    )
    from .payload import make_authorization_payload


LABEL_AUTHORIZED = "authorized-pr"
LABEL_BLOCKED = "blocked-non-core-pr"


def _resolve_codeowners_path() -> Path:
    """Return the absolute path to the CODEOWNERS file."""
    env = os.environ.get("CODEOWNERS_PATH")
    if env:
        return Path(env)
    return Path(__file__).resolve().parent.parent / "CODEOWNERS"


def _env(name: str, default: str = "") -> str:
    val = os.environ.get(name)
    if val is None or val == "":
        return default
    return val


def _build_payload_for_core_developer(
    *, author: str, core_devs: list[str]
):
    return make_authorization_payload(
        action="label-only",
        authorized=True,
        author=author,
        core_developers=core_devs,
        is_core_developer=True,
        message=(
            f"@{author} is recognised as a core developer. "
            f"PR authorized for normal review workflow."
        ),
        label=LABEL_AUTHORIZED,
    )


def _build_payload_for_non_core_developer(
    *, author: str, core_devs: list[str], contributing_url: str
):
    comment_body = render_closure_comment(
        author=author,
        contributing_url=contributing_url,
    )
    return make_authorization_payload(
        action="close-and-comment",
        authorized=False,
        author=author,
        core_developers=core_devs,
        is_core_developer=False,
        message=(
            f"@{author} is not a core developer. PR will be "
            f"closed with a pointer to CONTRIBUTING.md."
        ),
        comment=comment_body,
        label=LABEL_BLOCKED,
        comment_marker=COMMENT_MARKER,
    )


def main() -> int:
    author = _env("PR_AUTHOR")
    if not author:
        out = make_authorization_payload(
            action="error",
            authorized=False,
            author="",
            core_developers=[],
            is_core_developer=False,
            message="PR_AUTHOR environment variable is not set.",
        )
        print(out.to_json())
        return 2

    _ = _env("ACTION", "check")  # reserved for future use
    repo = _env("REPOSITORY", "datacustodia/ddl")

    core_devs = parse_core_developers(_resolve_codeowners_path())
    contributing_url = default_contributing_url(repo)

    if is_core_developer(author, core_devs):
        out = _build_payload_for_core_developer(
            author=author, core_devs=core_devs
        )
    else:
        out = _build_payload_for_non_core_developer(
            author=author,
            core_devs=core_devs,
            contributing_url=contributing_url,
        )

    print(out.to_json())
    return 0


if __name__ == "__main__":
    sys.exit(main())