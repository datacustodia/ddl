---
name: Documentation Bug Report
about: Report a bug, typo, broken link or rendering issue in the documentation
title: "[doc] "
labels: doc, need:view
assignees: ''
---

# Documentation Bug Report

Thanks for taking the time to report a documentation issue.
Please fill in the sections below so a core developer can
reproduce and fix the problem.

## 1. Type of Issue

<!-- Replace the applicable items with [x]. -->

- [ ] Typo or spelling error
- [ ] Broken or incorrect link
- [ ] Incorrect or outdated content
- [ ] Wrong wording or translation mismatch
- [ ] Code block that does not render correctly
- [ ] Sphinx build error or warning
- [ ] Missing content
- [ ] Other (please describe)

## 2. Where the Issue Is

- **Page or file**: <!-- e.g. docs/faq.md, README.md, .github/ISSUE_TEMPLATE/docbug.md -->
- **Section or anchor**: <!-- e.g. "## Compliance Checklist" or "Section 5(a)(2)" -->
- **Approximate line number** (if known): <!-- e.g. line 42 -->

## 3. Current Behavior

<!-- Paste the current (wrong) text or describe the current behavior. -->

```text
(paste here)
```

## 4. Expected Behavior

<!-- Describe what you expected to see, or paste the corrected text. -->

```text
(paste here)
```

## 5. Build and Environment

- Source of the docs you are viewing:
  - [ ] GitHub Pages build
  - [ ] Local `sphinx-build -b html docs build/html`
  - [ ] Other: <!-- describe -->
- Sphinx version (`sphinx-build --version`):
- Python version (`python --version`):
- Browser and version (for rendering issues):

## 6. Reproduction Steps

<!-- List the steps a core developer can follow to see the issue. -->

1.
2.
3.

## 7. Additional Context

<!-- Screenshots, links to rendered pages, related issues, etc. -->

## 8. Source Compliance

- [ ] I have read [`README.md`](../../README.md) and
      [`CONTRIBUTING.md`](../../CONTRIBUTING.md).
- [ ] I understand that only **core developers** may open
      pull requests. This issue is a request for a fix; if
      accepted, a core developer will prepare the change.