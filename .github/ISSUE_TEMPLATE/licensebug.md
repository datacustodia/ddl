---
name: License Bug Report
about: Report a bug, inconsistency or ambiguity in the License text
title: "[license] "
labels: licenses, need:view
assignees: ''
---

# License Bug Report

Thanks for taking the time to report an issue in the License
text. The License is a normative legal instrument, so please
be precise and conservative.

**Reminder**: only **core developers** may open pull requests
against the canonical repository. If your report is
accepted, a core developer will prepare and merge the change.

## 1. Type of Issue

<!-- Replace the applicable items with [x]. -->

- [ ] Typo or spelling error
- [ ] Broken cross-reference (e.g. "see Section X" pointing
      to the wrong Section)
- [ ] Inconsistency between Sections
- [ ] Inconsistency between Section and Preamble
- [ ] Inconsistency between Section and a definition
      (Section 1)
- [ ] Inconsistency between `licenses/License.txt` and
      `licenses/LastestLicense.txt`
- [ ] Missing provision
- [ ] Overlapping or contradictory provision
- [ ] Numbering or labelling error (e.g. wrong section letter,
      sub-number)
- [ ] Banner, header or formatting issue
- [ ] Other (please describe)

## 2. Where the Issue Is

- **Source file**: <!-- licenses/License.txt or licenses/LastestLicense.txt -->
- **Section**: <!-- e.g. Section 6(c) -->
- **Sub-item**: <!-- e.g. Section 5(a)(2) -->
- **Approximate line number** (if known): <!-- e.g. line 412 -->

## 3. Current Text (verbatim)

<!-- Paste the current text exactly as it appears in the file,
     including banner characters if relevant. Use a fenced
     block. Do NOT paraphrase. -->

```text
(paste here)
```

## 4. Suggested Wording

<!-- If you have a concrete proposal, paste it verbatim.
     Leave blank if you only want to flag the issue. -->

```text
(paste here)
```

## 5. Why This Is a Problem

<!-- Explain the inconsistency, ambiguity or error.
     Quote any related Sections that are affected. -->

## 6. Suggested Severity

- [ ] Blocking — License is unusable or misleading without
      a fix.
- [ ] Major — affects the meaning of one or more Sections.
- [ ] Minor — affects clarity but not meaning (wording,
      punctuation, banner alignment).
- [ ] Editorial — typo, grammar, formatting only.

## 7. Suggested Handling

- [ ] Fix in the next official release.
- [ ] Fix in a clarifying note only (no text change).
- [ ] Defer for discussion in a core-developer review.

## 8. Impact Analysis

<!-- If you can, list any places (other Sections, docs
     pages, translations, downstream tooling) that depend on
     the affected text. -->

- Affected Sections:
- Affected docs pages:
- Affected translations:

## 9. Provenance of the Source

- Which file did you inspect?
  - [ ] `licenses/License.txt` (official release)
  - [ ] `licenses/LastestLicense.txt`
  - [ ] A copy on another site or mirror
- If you inspected a copy, please quote the URI and the
  date you accessed it.

## 10. Source Compliance

- [ ] I have read [`README.md`](../../README.md) and
      [`CONTRIBUTING.md`](../../CONTRIBUTING.md).
- [ ] I understand that the authoritative License text
      lives in `licenses/License.txt` and that any fix must
      be made on the **latest official release**, not on a
      sub-version (see Section 6(c) of
      `licenses/LastestLicense.txt`).
- [ ] I understand that only **core developers** may open
      pull requests. This issue is a request for review; if
      accepted, a core developer will prepare the change.