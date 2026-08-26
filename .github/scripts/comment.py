"""Comment templates posted by the Spam-Blocker Bot.

The closure comment body is rendered by ``render_closure_comment``.
Keep the wording friendly but firm: the bot is not a person,
and the PR is closed by automation, not by personal
rejection. The comment explicitly points to
``CONTRIBUTING.md`` Section 3 and to the relevant issue
templates so that the contributor knows exactly how to
propose their change through the correct channel.
"""
from __future__ import annotations


# The template is intentionally written in English: the
# canonical License and is the only authoritative language for
# the project (see ``licenses/License.txt`` Section 21(c)).
_CLOSURE_TEMPLATE = """\
@{author} thank you for your interest in DDL-v1.

**This pull request has been closed automatically.**

Per [`CONTRIBUTING.md`]({contributing_url}), Section 3, only
**core developers** may open a pull request against the
canonical repository. The canonical repository publishes a
normative legal instrument; opening a pull request is a
release-management action that must be carried out by a
core developer, not an outside contributor.

If you would like to propose a change, please file an
**issue** instead. A core developer will then sponsor,
prepare, and open the pull request on your behalf if your
proposal is accepted.

What to do next:

  1. Open an issue describing the change you would like to
     see, using the appropriate template:
       - `[doc]` Documentation Bug Report
       - `[license]` License Bug Report
       - `[i18n]` Translation Report
       - `[security]` Security Advisory (private email,
         not a public issue)
  2. Discuss with the core developers until there is rough
     consensus.
  3. Wait for a core developer to open the pull request.

This is not a workaround; it is the rule. See
[`CONTRIBUTING.md`]({contributing_url}), Sections 2 and 3,
for the full workflow.

If you believe this closure is in error (for example,
because you have been added as a core developer since this
check last ran), please contact a core developer through
the issue tracker.

- Spam-Blocker Bot (auto-generated)
"""

# Marker used by workflows to detect a bot-managed comment
# when re-running. The HTML comment syntax is invisible in
# rendered Markdown and survives most reformatting.
COMMENT_MARKER = (
    "<!-- spam-blocker-bot: do not edit this comment; "
    "it is regenerated on every PR -->"
)


def render_closure_comment(*, author: str,
                            contributing_url: str) -> str:
    """Return the Markdown body to post when closing a PR
    opened by a non-core developer."""
    return _CLOSURE_TEMPLATE.format(
        author=author,
        contributing_url=contributing_url,
    )


def default_contributing_url(repository: str = "datacustodia/ddl") -> str:
    """Return the canonical URL of ``CONTRIBUTING.md`` for the
    given ``owner/repo``. The ``master`` branch is assumed;
    forks should not be linking here at all because the file
    is identical across forks."""
    return f"https://github.com/{repository}/blob/master/CONTRIBUTING.md"