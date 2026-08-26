"""Internal helpers for the DDL-v1 automation scripts.

This package is consumed by the workflows under
`.github/workflows/`. It is **not** part of the public
project surface: contributors should not depend on it,
and breaking changes here do not require a License release.

Modules
-------
- ``codeowners``  : parse ``.github/CODEOWNERS`` and return
                    the set of core developers.
- ``payload``     : build the structured JSON payload that
                    workflows consume via ``outputs``.
- ``comment``     : render the closure comment body for
                    blocked pull requests.
"""
__all__ = ["codeowners", "payload", "comment"]