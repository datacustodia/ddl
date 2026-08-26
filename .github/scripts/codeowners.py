"""Parser for `.github/CODEOWNERS`.

The DDL-v1 CODEOWNERS file lists `@aiwonderland` as the sole
core developer across every path. Per ``CONTRIBUTING.md``
Section 9, core-developer status is what authorises a
contributor to open pull requests against the canonical
repository.

This module exposes a single function, ``parse_core_developers``,
which reads the CODEOWNERS file and returns the sorted list
of GitHub logins that appear as ``@handle`` references in
non-comment, non-blank lines. Any other path-level syntax
(``@org/team``, email patterns, etc.) is currently ignored,
because the DDL-v1 project does not use it. If that changes,
the parser should be updated together with ``CODEOWNERS``.
"""
from __future__ import annotations

import re
from pathlib import Path

# Match a GitHub handle: starts with ``@``, followed by a
# letter or digit, then up to 38 more letters, digits or
# hyphens. Mirrors GitHub's own validation rules.
_HANDLE_RE = re.compile(r"@([A-Za-z0-9][A-Za-z0-9-]{0,38})")


def parse_core_developers(path: str | Path) -> list[str]:
    """Return the sorted list of GitHub logins that own at
    least one path in ``path``.

    The function is tolerant of:

      - missing files (returns ``[]``);
      - comment lines starting with ``#`` (skipped);
      - blank lines (skipped);
      - path patterns (the ``@handle`` may appear anywhere
        on a non-comment, non-blank line).

    The returned list is lowercased for direct comparison
    with a PR author's login. The caller is responsible for
    deciding whether the comparison should be case-insensitive
    on the GitHub side; in practice GitHub logins are
    case-insensitive, so this module lowercases everything
    by default.
    """
    path = Path(path)
    if not path.exists():
        return []
    handles: set[str] = set()
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        for match in _HANDLE_RE.finditer(line):
            handles.add(match.group(1).lower())
    return sorted(handles)


def is_core_developer(login: str, core_devs: list[str]) -> bool:
    """Return ``True`` iff ``login`` (case-insensitive) is in
    ``core_devs``."""
    if not login:
        return False
    target = login.strip().lower()
    return any(target == h for h in core_devs)