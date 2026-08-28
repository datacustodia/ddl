# Contributing to DDL-v1

Thank you for your interest in contributing to the Datacustodia
Dataset License, Version 1 (DDL-v1) project. This document
explains how to file issues, submit changes, and contribute
translations.

The DDL-v1 project is governed by the Datacustodia Dataset
License organization. A small group of **core developers**
maintains the canonical repositories, reviews contributions,
and is the only party authorized to merge changes or release
new official versions of the License.

---

## 1. Code of Conduct

By participating in this project, you agree to abide by the
[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Please read it
before opening an issue or submitting a change.

---

## 2. Filing an Issue

Anyone may file an issue against the project. Issues are the
**primary** channel for reporting problems, requesting
clarifications, suggesting improvements, or proposing new
features.

### 2.1 When to file an issue

File an issue if you want to:

  - report an error, ambiguity, or inconsistency in the
    License text or in the documentation;
  - request a clarification of any Section of the License;
  - propose a wording improvement that does not change the
    meaning of any Section;
  - report a problem with the documentation site
    (`docs/`), the build, or the Sphinx configuration;
  - request a new translation into a language not yet
    covered; or
  - propose a new annex, example or non-normative note.

### 2.2 When **not** to file an issue

Do not file an issue to:

  - request a commercial license (see
    [`README.md`](README.md) and `docs/commercial.md`);
  - ask general legal questions unrelated to the wording of
    DDL-v1;
  - discuss matters that belong in a private communication
    with the Licensor; or
  - publish material that you intend to be a stand-alone
    dataset release under DDL-v1 (use a separate repository).

### 2.3 Issue template

When opening an issue, please use the appropriate template
and include:

  1. a short, descriptive title;
  2. the **type** of issue (`bug`, `doc`, `i18n`, `licenses`);
  3. the **Section** or page the issue refers to (e.g.
     `Section 6(c)`, `README.md`, `docs/faq.md`);
  4. a clear **description** of the problem or request;
  5. **proposed wording** if you have one (as a fenced
     block, not a screenshot); and
  6. any **context** that may help a reviewer understand the
     issue (links, references, screenshots, environment
     details).

Issues that do not follow this template may be closed by a
core developer with a request to resubmit.

---

## 3. Pull Requests

Pull requests are subject to a **stricter** workflow than
issues. Only **core developers** may open pull requests
against the canonical repository.

### 3.1 Who may open a pull request

  - **Core developers**: may open pull requests directly
    against the canonical repository, including pull
    requests based on contributions from non-core
    contributors.
  - **Everyone else** (occasional contributors, drive-by
    contributors, vendors, downstream users): may **not**
    open a pull request against the canonical repository.
    External contributors must use the issue tracker
    (Section 2) to propose a change. If a core developer
    accepts the proposal, the core developer will prepare
    and open the pull request themselves.

This rule exists because:

  - the License is a normative document; any change to its
    wording is a release-management decision that must be
    made by the Licensor;
  - the canonical repository is **not** an open-source
    software project; it is the publishing channel for a
    legal instrument; and
  - allowing arbitrary pull requests would risk
    unauthorized edits to a document that downstream users
    rely on for legal certainty.

### 3.2 The workflow

The standard contribution workflow is:

  1. **Discussion (issue)**. Open an issue describing the
     proposed change. Discuss with core developers until
     there is rough consensus.
  2. **Drafting**. A core developer drafts the change on a
     private branch or in a working area. The core developer
     may ask the original proposer to review the draft.
  3. **Pull request**. A core developer opens a pull
     request that references the issue. The pull request
     description must explain the rationale, list the
     Sections affected, and confirm that the change has been
     verified against `licenses/License.txt`.
  4. **Review**. At least one core developer other than the
     author must review and approve the pull request.
     Section 6 (Verbatim Reproduction) of the License and
     any change to defined terms require review by **two**
     core developers.
  5. **Merge**. Only a core developer may merge. The merge
     commit must reference the originating issue.
  6. **Release**. A new official release is published by
     the Licensor in accordance with Section 6(c) of the
     License.

### 3.3 What a pull request must contain

A pull request description must include:

  - a link to the originating issue;
  - a one-paragraph rationale;
  - the **scope** of the change (which Sections, which
    pages, which files);
  - a **diff** summary;
  - a statement of whether the change is
    **substantive** (affects the meaning of the License) or
    **non-substantive** (typo, formatting, comment); and
  - for translation pull requests, the language tag and the
    official release version that the translation is
    derived from.

### 3.4 Substantive vs. non-substantive changes

  - **Non-substantive** changes (typo, punctuation, banner
    alignment, comment fix) may be merged by a single core
    developer after self-review.
  - **Substantive** changes (any change to a defined term,
    any change to a Section heading, any change to a
    prohibition or a permission) require **two** core
    developer approvals and must be reflected in a new
    official release before they take effect.

### 3.5 What cannot be merged

A pull request will be rejected if it:

  - is opened by a non-core contributor;
  - changes the meaning of any Section without prior
    discussion in an issue;
  - introduces a new obligation on the Licensor without
    the Licensor's written consent;
  - removes or weakens any of the five mandatory
    requirements (free worldwide use, non-commercial
    reuse, mandatory attribution, prohibition on
    commercial use, verbatim reproduction); or
  - includes material that the contributor does not have
    the right to license under DDL-v1.

---

## 4. Translating the License

Translations of the License are welcome. All translations are
**informative**: only the English text in
[`licenses/License.txt`](licenses/License.txt) is the
authoritative version. See Section 21(c) of the License and
Section 6(c) of `licenses/LastestLicense.txt`.

### 4.1 Source text

A translation must be derived from the **latest official
release** of `licenses/License.txt`. Do **not** translate
from a sub-version (such as `1.1`) or from any working
build.

### 4.2 File layout

Translations live under `licenses/i18n/`:

```
licenses/i18n/<language-tag>/License.v1.txt
```

The `<language-tag>` should follow BCP 47 / ISO 639-1, for
example:

  - `de_DE` for German in Germany
  - `fr_FR` for French in France
  - `ja_JP` for Japanese in Japan
  - `zh_CN` for Simplified Chinese
  - `zh_TW` for Traditional Chinese

### 4.3 Translation requirements

A translation must:

  1. preserve the **structure** of the License (Preamble,
     Sections 1 through 21, Annexes A and B, closing
     banner);
  2. leave capitalized defined terms such as `Licensor`,
     `Licensed Material`, `Licensed Rights`, `Adapted
     Material`, `Attribution`, `Commercial Use`,
     `Non-Commercial Purpose`, `Publicly Released Usage
     Scenario`, `Sui Generis Database Rights` and `You`
     untranslated, or transliterate them consistently across
     the document;
  3. be marked at the top of the file as a non-authoritative
     translation of DDL-v1, with a clear pointer to the
     authoritative English text;
  4. preserve the integrity of the verbatim-reproduction
     obligation: a translation must not be substituted for
     the English text in any redistribution; and
  5. preserve all numbered items, list markers, and banner
     characters (`====`, `+====+`, `| ... |`) so that
     Section references remain consistent across languages.

### 4.4 Translation workflow

Because the License is a legal instrument, translations
follow the same rules as substantive changes:

  1. Open an issue describing the language, the proposed
     translator(s), and any known risks (legal terminology
     that has no clean equivalent, region-specific legal
     concepts, etc.).
  2. A core developer reviews the proposal and assigns a
     reviewer core developer.
  3. The translator drafts the translation and submits it
     to the issue as a patch or as a gist.
  4. The reviewer core developer verifies the translation
     against the source text and confirms that all
     requirements in Section 4.3 are met.
  5. A core developer opens the pull request that adds the
     translation to `licenses/i18n/<language-tag>/` and
     adds an entry to the translation table in
     [`README.md`](README.md).
  6. After merge, the translation is published alongside
     the next official release of DDL-v1.

### 4.5 Translations are not legal advice

A translation is provided as a courtesy. It is **not**
legal advice and may not reflect the latest amendments. For
any legally consequential question, refer to the
authoritative English text in `licenses/License.txt` and
consult a qualified lawyer in the relevant jurisdiction.

---

## 5. Becoming a Core Developer

Core developers are appointed by the Licensor. The current
list is maintained in `CONTRIBUTORS`. Criteria include:

  - sustained, high-quality contributions over time;
  - demonstrated judgement on legal, normative and
    documentation questions;
  - familiarity with the License text and its intent; and
  - endorsement by at least one existing core developer.

---

## 6. Reporting Security Issues

Security issues affecting the documentation site, the build,
or the integrity of the License text should be reported
**privately** to the Licensor. Do not file a public issue
until the Licensor has acknowledged the report and a fix
has been prepared.

Email: `<ddl-org@tutamail.com>`

---

## 7. Licensing of Contributions

By submitting a contribution (whether as an issue, a patch,
or a translation), you agree that:

  - the contribution may be incorporated into DDL-v1 and
    released under the License;
  - the contribution is your own work, or you have the
    necessary rights to submit it;
  - you grant the Licensor a perpetual, worldwide,
    royalty-free right to use, modify and relicense the
    contribution for the purposes of DDL-v1; and
  - you understand that the Licensor is not obligated to
    accept, merge, or release any contribution.

---

## 8. Recognition

Contributors are listed in `CONTRIBUTORS` and (where
appropriate) in `CREDITS.txt`. Core developers are listed
in both.

Thank you for helping make DDL-v1 clearer, more accurate,
and more accessible.


---

## 9. Physical / Engineering Enforcement

The rules in Section 3 are not merely procedural. The
canonical repository is configured so that **non-core
contributors physically cannot open a pull request** against
the protected branches. This is enforced at the
infrastructure level, not just in policy.

### 9.1 How it is enforced

The repository uses GitHub branch-protection and code-owner
rules configured in `.github/CODEOWNERS` and the repository
settings. Specifically:

  - **`.github/CODEOWNERS`** lists the core developer(s) as
    the required reviewers for every file in the canonical
    repository (including `licenses/License.txt`,
    `licenses/LastestLicense.txt`, `README.md`,
    `CONTRIBUTING.md`, `docs/`, `.github/` and the
    translations under `licenses/i18n/`).

  - **Branch protection** on the default branch `master` 
  requires:

      - at least one (or, for substantive changes, two)
        approving reviews from the listed code owners
        before a pull request can be merged;

      - all status checks (the docs build, link checks, etc.)
        to pass before a pull request can be merged;

      - linear history (no direct pushes; all changes must
        come through a pull request); and

      - dismissal of stale approving reviews when new
        commits are pushed.

  - **Restriction of who can push** to the protected branch:
    the protected branch is limited to the core-developer
    team. Other contributors, even with `write` access to
    the repository, cannot push directly to the protected
    branch.

  - **Required status checks** include the documentation
    build (`.github/workflows/docs.yml`), which must pass
    before any merge.

### 9.2 What this means for non-core contributors

In practice this means:

  - A non-core contributor **cannot** open a pull request
    that reaches the protected branch. Even if they fork the
    repository and open a pull request from their fork, the
    branch-protection rules will require an approval from a
    code owner, and the code owners are core developers.

  - A non-core contributor **cannot** push directly to the
    canonical repository's protected branch. Such a push
    will be rejected by GitHub.

  - A non-core contributor **cannot** bypass code review by
    creating their own branch off an old commit, opening a
    pull request, and self-approving it. Branch protection
    prevents self-approval by non-code-owners.

### 9.3 Why the physical enforcement matters

Without physical enforcement, a single human mistake — a
core developer clicking "Merge" too quickly, a misconfigured
webhook, a compromised account — could push an unauthorized
change into the License text. Because DDL-v1 is a legal
instrument, even a transient incorrect state could mislead
downstream users.

Physical enforcement makes the rules **fail-closed**: if
any link in the chain is missing, the change does not
land. The chain is:

  1. A core developer opens the pull request.
  2. CODEOWNERS requires an approving review from another
     core developer.
  3. Branch protection requires the approving review and
     passing status checks.
  4. The merge is performed by a core developer with merge
     rights on the protected branch.

Every step is automated and cannot be skipped by a
non-core contributor.

### 9.4 Branch and fork policy

  - Direct pushes to the protected branch are **disabled**
    for everyone, including core developers. Core developers
    must also use pull requests.
  - Force pushes are **disabled** on the protected branch.
  - Branch deletion is **disabled** on the protected
    branch.
  - Forks may be created by anyone, but pull requests from
    forks are subject to the same review rules.

### 9.5 What to do if the rules block legitimate work

If you are a non-core contributor and the rules appear to
block legitimate work, that is by design. Do not attempt to
circumvent the rules. Instead:

  1. Open an issue describing what you want to do.
  2. Wait for a core developer to pick it up.
  3. Cooperate with the core developer to draft the change.

This is not a workaround for the rules; it is the rules.

### 9.6 Repository administrators

The Licensor is the only repository administrator.
Repository administrators retain the technical ability to
override branch-protection rules in an emergency, ~~but any
override is treated as a release-management event and is
recorded in `CHANGELOG.md` (or the equivalent revision
history)~~ TODO along with its rationale.