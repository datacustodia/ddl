# Security Policy

## 1. Purpose

This Security Policy describes how security issues affecting
the **Datacustodia Dataset License Version 1 (DDL-v1)**
project should be reported, triaged and resolved. Because
DDL-v1 is a normative legal instrument relied on by
downstream users, integrity of the License text and of the
surrounding tooling is treated as a **release-management
and legal-safety** matter, not merely a software-security
matter.

This Policy applies to:

  - the License text in `licenses/License.txt`,
    `licenses/LastestLicense.txt`, and any other
    `licenses/` artefact;
  - the documentation site under `docs/`, including its
    Sphinx configuration and the GitHub Pages deployment
    workflow at `.github/workflows/docs.yml`;
  - the Issue and Pull Request templates under
    `.github/ISSUE_TEMPLATE/` and `.github/PULL_REQUEST_TEMPLATE.md`;
  - the repository settings, branch-protection rules and
    `CODEOWNERS` configuration; and
  - the integrity header of any machine-readable
    configuration file distributed together with the
    License.

## 2. What Counts as a Security Issue

A **security issue** for this project is any circumstance
that could cause a downstream user to rely on a License
text that is not the authoritative release, or that could
compromise the integrity, authenticity, or availability of
the License or its documentation.

Examples include, without limitation:

  - a proposed or published edit to a Section of
    `licenses/License.txt` or `licenses/LastestLicense.txt`
    that would weaken any of the five mandatory requirements
    (free worldwide use, non-commercial reuse, mandatory
    attribution, prohibition on commercial use, verbatim
    reproduction);
  - a copy of the License text published on a non-canonical
    site that purports to be the official release but is
    not, including any unofficial mirror that fails to
    reproduce the banner headings verbatim;
  - a bypass of branch-protection rules or `CODEOWNERS`
    that allows a non-core contributor to land changes on
    a protected branch;
  - a malicious commit, secret, or token disclosed in the
    repository history, including in `.github/workflows/`
    or in any docs build artefact;
  - a tampering of the integrity header of a
    machine-readable configuration file distributed with
    the License;
  - a vulnerability in the Sphinx build chain, the GitHub
    Pages deployment, or any third-party dependency listed
    in `docs/requirements.txt`;
  - a phishing or impersonation attempt purporting to act
    on behalf of the Licensor, the Datacustodia Dataset
    License organization, or a core developer; and
  - a deliberate misstatement of the License terms in
    third-party material that purports to summarise or
    quote DDL-v1.

## 3. What is NOT a Security Issue

The following do **not** count as security issues under
this Policy and should be filed through the normal channels
described in [`CONTRIBUTING.md`](CONTRIBUTING.md):

  - questions about the meaning of a Section that do not
    involve tampering or unauthorised publication;
  - typographical or formatting issues in the License
    text that do not change the meaning of any Section
    (these are non-bug documentation issues — see
    `[docbug]` issues);
  - bugs or inconsistencies in the License text that do
    not affect legal safety (these are License bug
    reports — see `[licensebug]` issues);
  - translation errors in `licenses/i18n/` that do not
    affect the authoritative English text; and
  - feature requests or enhancement proposals.

## 4. How to Report

Security issues must be reported **privately**, before any
public disclosure. Public issues, pull requests, or social
media posts are not appropriate channels for an initial
security report.

  - **Primary contact:** Evan Yang `<quantbit@126.com>`

Please include in the report:

  1. a clear, factual description of the issue;
  2. the affected file(s), Section(s), or workflow(s);
  3. the suspected impact (legal, technical, or both);
  4. a proposed remediation, if you have one;
  5. whether the issue is already publicly known; and
  6. your name and a contact channel for follow-up, unless
     you wish to remain anonymous.

## 5. Coordinated Disclosure

The Licensor follows a coordinated-disclosure timeline:

  1. **Acknowledgement.** Within seven (7) days of
     receiving a report, the Licensor will acknowledge
     receipt and appoint a handler.
  2. **Investigation.** The handler will investigate,
     consult any necessary experts, and prepare a fix.
     During this period the reporter should keep the
     issue confidential.
  3. **Fix and release.** A fix will be prepared as a
     private branch and merged by a core developer. A
     new official release of DDL-v1 will be published if
     the fix is substantive. The Licensor will credit the
     reporter in the release notes unless the reporter
     requests otherwise.
  4. **Public disclosure.** Once the fix is published, or
     ninety (90) days after the initial report (whichever
     comes first), the Licensor and the reporter may
     publicly disclose the issue.

The Licensor will not pursue legal action against a
researcher who, in good faith, reports a vulnerability in
accordance with this Policy.

## 6. Out-of-Scope Vulnerabilities

The following are out of scope and will not, on their own,
trigger a security response:

  - bugs in third-party software that are already tracked
    upstream;
  - theoretical concerns without a concrete reproduction;
  - issues that require physical access to a core
    developer's account and that are not enabled by a
    vulnerability in the project itself;
  - social-engineering attacks against end users of the
    Licensed Material (these should be reported to the
    relevant downstream parties); and
  - issues affecting only unofficial mirrors or third-party
    sites that purport to host DDL-v1 without authorisation.

## 7. Safe Harbor

The Licensor considers security research conducted under
this Policy to be:

  - authorised under any applicable anti-circumvention law
    to the extent the research requires it;
  - not a breach of any contract, including the License
    itself; and
  - not a violation of any acceptable-use policy that may
    otherwise apply to the project infrastructure.

The Licensor will not assert any copyright, database, or
contract claim against a researcher acting in good faith
under this Policy. This safe harbor does not extend to
research that intentionally harms the integrity of the
License text, discloses the report publicly before the
Licensor has had a reasonable opportunity to act, or
exfiltrates confidential information beyond what is
necessary to demonstrate the issue.

## 8. Recognition

Researchers who report valid security issues under this
Policy are credited in the next official release of
DDL-v1, unless they request anonymity. The Licensor may, at
its sole discretion, also acknowledge the reporter in
`CREDITS.txt`.

## 9. Versioning

This Security Policy is versioned together with the License.
Aligned with the **Datacustodia Dataset License Version 1
(DDL-v1)**. Substantive amendments require the same review
and approval process as the License itself.