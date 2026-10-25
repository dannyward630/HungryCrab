# Next supervised discovery release scope

Status: planned, 2026-10-25. Tracker:
[#453](https://github.com/drevendev/HungryCrab/issues/453).
Target: the next release after 0.6.4; the current development line is 0.6.5.dev0.
The release procedure assigns the final version after compatibility review.
Baseline: `master@d9ab36538aabede45d9ad1b661cea5c62d484da3`.

Deliver the outstanding pilot transfers, repair every selected pilot finding,
and make supervised discovery investigate useful behavior beyond the fixed trait
menu. Include three bounded improvements to CLI help, issue-card readability and
architecture evidence. This is a planning deliverable; implementation, merges,
Docker installation and release publication do not start during this task.

## 1. Release contents

| Work | Scope | Acceptance owner |
|---|---|---|
| Pilot follow-through | Finish the outstanding PRs through their target policies; verify retention of already merged changes | Section 2 and the operator's experiment registry |
| Acquisition and attribution | Safe bounded local catch, Windows backend readiness, preservation of prior notices and MIT metadata controls | #445, #446, #450 |
| Evidence and receiving-project facts | Portable source references, manifest-free runtimes and consistent CI evidence | #449, #451, #194 |
| Wider discovery and honest closure | Goal-driven exploration, new behavior/pattern cards, coverage records and a controlled replay | #447, #448 |
| Three bounded improvements | Public CLI help, distinct issue-lesson cards, removal of phantom architecture facts | #354, #130, #452 |

There are **eight pilot issue workstreams and three additional issue workstreams**.
The existing PRs are integration tasks, not eleven additional discoveries. The
larger discovery work is mandatory for this release; it is not a stretch item to
drop after the easier configuration repairs.

Use the current remaining acceptance of each issue. Historical issue text can
describe already-fixed behavior. A partial slice does not close an entire issue,
and a closed issue or green CI does not prove a useful change survived integration.

## 2. Finish the existing PR rollout

Provider state and retained content were checked on 2026-10-25. Reconcile again
before effects because another session can change a branch or merge it.

| Public PR | Observed state | Required work |
|---|---|---|
| [HungryCrab #443](https://github.com/drevendev/HungryCrab/pull/443), CodeQL | OPEN; GitHub reports a merge conflict. Head `b264be88d9759cda820f9539e030d26fb27a6466` had successful CI and CodeQL | Reconcile current master, preserve all source notices/receipts and action pins, review the complete resulting diff, run fresh CI and CodeQL on the resulting head, and merge through target policy |
| [HungryCrab #444](https://github.com/drevendev/HungryCrab/pull/444), unittest recognition | MERGED; merge/default head `d9ab36538aabede45d9ad1b661cea5c62d484da3` retains the matcher | Keep the merged fix; complete its remaining workflow-evidence inconsistency under #194 rather than recreating this PR |
| [BeautifulRepo #157](https://github.com/drevendev/BeautifulRepo/pull/157), lint cache | MERGED; merge/default head `5e623dffd74fe96403d75c29dfc259ae3f9c6b2f` retains the lint-cache inputs | Verify retention at final follow-up, including its independently maintained MIT notice; do not reinstate removed internal control files |

The private rollout is a required companion track in the operator's excluded
local experiment registry. Its identity, PR links, findings and CI details must
not be copied into this public document, tracker, public Actions or artifacts.
Apply that repository's real checks, review and merge-owner policy. Record an
actual unresolved external dependency rather than bypassing it or claiming merge.

For every pilot PR, retain the latest head, target default branch and inspected
default revision, CI results, actual merge SHA/date and whether the intended
change is retained, amended or reverted. Verify ancestry and resulting behavior;
an approved old head does not approve conflict resolution or later edits. Do not
force-push over concurrent work or enable auto-merge as a substitute for review.

## 3. Repair the pilot findings

### A1. Bound local acquisition and prepare Windows execution

Tracking: [#445](https://github.com/drevendev/HungryCrab/issues/445).

- Expose and enforce catch download and disk limits for clone and refresh,
  including independent wiki acquisition, Git expansion, checkout and temporary
  staging. Keep all acquisition writes inside the actual bounded domain.
- Prepare Docker or another verified local Windows backend. Check the machine's
  prerequisites and storage/resource settings before installation during the
  implementation phase; record any restart or operator-only dependency.
- A bind mount, free-space sample, shallow clone or public repository is not a
  hard disk boundary. Demonstrate the selected backend's enforced capacity and
  process-tree cancellation, not just configured numbers.
- Refuse unsupported containment before network acquisition. Limits must not
  fall back silently to an unbounded host directory or to public CI.
- Preserve unrelated caches and workspaces. Failed/cancelled acquisition is not
  reusable; cleanup must be owned, bounded and recoverable.
- Document host headroom and retained-cache growth separately from the
  per-acquisition limit. Full cache collection remains #213, outside this release.

Acceptance: real Windows and Linux synthetic overflow, expansion, refresh,
cancellation and cleanup checks, plus independent wiki/concurrent-connection
controls. Keep a normal small acquisition passing. No donor program runs.

### A2. Preserve existing legal notices

Tracking: [#446](https://github.com/drevendev/HungryCrab/issues/446).

Replace heading-only ownership with a verified managed-file contract. An
ordinary human-maintained `# Third-party notices` file must be refused or
explicitly preserved through a reviewable migration before publication or
rewriting. Preserve notices across fetched-base changes, missing/deleted receipts
and edited managed files. A separate generated notice path must work alongside
an existing contributor-maintained index.

Acceptance: new tests fail under the old guard and cover the full publication
payload and standalone attribution rewrite, including absent provider effects on
refusal and a valid managed-file control. The repaired pilot PR is a workaround,
not acceptance of this CLI fix. A green check over only newly rendered receipts
cannot establish that older notices survived.

### A3. Recognize supported MIT metadata without admitting riders

Tracking: [#450](https://github.com/drevendev/HungryCrab/issues/450).

Support bounded ordinary copyright forms around the fully established MIT body:
present-ranges, absent/reordered years and supported obfuscated contact metadata.
Keep the original notice text. Unsupported metadata must have an actionable
explanation; an API label or filename cannot supply the missing grant.

Acceptance: the reported positive controls and the restrictive-rider negative
matrix from #436/#437 pass together. Paid/commercial-use conditions, field-of-use
restrictions, extra grants and arbitrary copyright-prefixed prose remain refused.
Do not broaden the general licence compatibility engine in this workstream.

### E1. Retain source evidence across machines

Tracking: [#449](https://github.com/drevendev/HungryCrab/issues/449).

Make the public-donor artifact to local-comparison path explicit and supported.
Preserve bounded repository-relative file references and verified provenance so
an unavailable Linux working-tree root does not silently become an empty file
list on Windows. Provide a safe resolver for the supported immutable snapshot
form, or expose unavailable evidence as unknown. Do not trust a coincidentally
existing old directory, materialize executable donor content automatically or
weaken HUMAN to recover a missing reference.

Acceptance: original-root and relocated comparisons retain equivalent supported
file evidence and path-specific grants. Cover Git-object-only evidence, an
unrelated nested licence, genuine absence, stale/aliased roots and incomplete
inventories. No private maw data enters a public donor artifact. Existing Feeder
meal serving and its source identity checks continue to work.

### E2. Recognize the runtime of manifest-free maws

Tracking: [#451](https://github.com/drevendev/HungryCrab/issues/451).

Separate package/dependency ecosystem facts from grounded first-party runtime
compatibility. A stdlib Python repository may have zero dependencies and no
package manifest while remaining eligible for Python comparisons. Do not invent
a pyproject, dependency or test framework to fill the gap.

Acceptance: a first-party stdlib Python fixture reaches relevant comparison
judgement; documentation mentions, excluded fixture/vendor files, another real
runtime and an unknown stack remain negative/unknown controls. Eligibility does
not mean that an additional tool should be adopted.

### E3. Share CI tool classification and source evidence

Tracking: [#194](https://github.com/drevendev/HungryCrab/issues/194).

Use consistent classification for parsed commands, CI traits and workflow
evidence. Finish the unittest inconsistency remaining after #444 and support
the selected bounded package-script/entry-point indirection through inert
metadata. Preserve explicit limits and cycles/unknown handling; do not execute
scripts or implement a general shell interpreter.

Acceptance: donor workflow to traits to candidate to exact workflow-file evidence
is covered, alongside the already-fixed maw-side false recommendation. Keep
echo/import/module-prefix negative controls, supported root-script cases and
appropriate unknown results for unresolved indirection. Verify the original
remaining #194 acceptance before closing it.

## 4. Deliver wider discovery with verifiable coverage

Tracking: [#447](https://github.com/drevendev/HungryCrab/issues/447) and
[#448](https://github.com/drevendev/HungryCrab/issues/448).

### D1. Plan from the receiving project's problems

Record the maw's actual goals, important flows, open gaps, architecture and
dependency/effect constraints. Select relevant exploration facets: behavior and
API/CLI usability; algorithms and data structures; failure recovery, resource
bounds and concurrency; streaming/performance; testing and adversarial vectors;
architecture/extensibility; packaging/operations; documentation and contributor
experience. Evidence may make a facet inapplicable; an unexamined facet stays
unexamined. This is not a requirement to force every facet into every donor.

Use the menu as an index, then inspect bounded source/test/example/history/issue
evidence for the selected hypotheses. State channel and history coverage before
using their absence. A shallow snapshot is not a historical investigation.

### D2. Register useful behavior outside the trait catalogue

Provide a deterministic validated route for an agent-discovered nutrient to
enter a meal with stable maw-relative identity, donor revision/file/range,
receiving behavior, verified gap, adaptation and maintenance costs, and an
acceptance check. Keep model judgement in the skill/agent protocol; the CLI
validates and persists it without LLM calls or a new mandatory parser framework.

Retain licence, origin, hunger, deduplication, receipt and publication guards.
Differentiate permission to inspect, keep an idea, propose a change and implement
a PR. Keep policy-blocked findings visible for an explicit scope decision; do not
silently enable copying code or substitute a non-MIT donor. Preserve existing ids
or provide a migration if a schema change requires one.

### D3. Make coverage and closure match the work

Record acquisition, comparison, exploration, implementation, review/CI,
publication and default-branch acceptance separately. Capture immutable tool,
digest/menu, dirty-maw, policy and ledger identities. Later deduplication must not
erase the original candidate set or denominator.

Keep evidence-backed dispositions distinct from proposed triage, unknown,
unexplored, budget-deferred, policy-blocked and licence-unresolved states. A
category-wide reason does not establish individual semantic review. NO_GAP needs
an examined scope and actual maw evidence, not zero menu cards. Audit whether
unsupported prior dispositions entered learning; do not invent acceptance or
train on uninvestigated rejections.

Bind CI/runner observations to their actual repository, artifact/head, workflow,
job and executed steps. Companion billing failure is not target CI failure;
an app attachment timeout is not failed GitHub publication.

### D4. Prove the expanded path and replay the relevant cohort

Use a small synthetic donor/maw pair with a known non-trait behavior gap, such as
bounded streaming instead of whole-input buffering. The source is read as inert
data. Validate the proposed card and receiving implementation without executing
the donor; use a receiving project that already has the behavior as a no-gap
control. Registration alone proves the contract, not model discovery quality.

Then perform a bounded, recorded supervised replay on the relevant original
public cohort under the broader protocol. Inspect the earlier generic declines
and report supported findings, specific rejections, legal/policy holds and work
left pending. Keep any private replay in its authorized private environment.
Record the actual agent/tool version and review method; fabricate no independent
auditor or completed swarm. No paid/live benchmark run is implied.

Acceptance measures examined hypotheses/facets, verified gaps, useful adaptation,
cost and later maintainer acceptance. There is no minimum PR quota or compulsory
5–15 kept nutrients. A quick structural pass remains available and labelled as
such; it cannot close a deeper user goal.

## 5. Three bounded additional improvements

| Issue | Included work | Acceptance and boundary |
|---|---|---|
| [#354](https://github.com/drevendev/HungryCrab/issues/354) | Explain the currently undocumented public command/options surface | Walk the actual parser and cover missing public help with a regression; describe real defaults/effects. Preserve intentional hidden options, names and behavior. Recount current omissions rather than claiming the historical 73 is current |
| [#130](https://github.com/drevendev/HungryCrab/issues/130) | Give issue-lesson cards distinguishable structured titles and usable evidence | Two distinct clusters/cards and dry-run previews remain distinguishable using safe source/issue facts. Preserve stable ids, commenter-origin ceilings, title-leak sentinels and frozen benchmark labels. Do not reintroduce raw commenter prose to make titles readable |
| [#452](https://github.com/drevendev/HungryCrab/issues/452) | Qualify and correct phantom architecture symbols/imports inside comments and strings | First reproduce through a full synthetic digest; preserve real symbols/edges while excluding inert ones in Python and JS/TS. Check counts and hubs, bounded processing and unsupported-syntax coverage. The issue currently proves the regex stage, not end-to-end mining; this is a bounded precision repair, not a universal parser rewrite |

These tasks complement discovery usability and the reliability of its evidence.
Additional unrelated backlog does not enter automatically. In particular the
remaining GPL summary-label work in #207 and the wider documentation audit #229
remain separate; update only documentation affected by this release's contracts.

## 6. Implementation order

1. Reconcile the current PR inventory, preserve the merged fixes and establish
   the implementation baseline. Resolve #443's conflict and follow the private
   target's real merge procedure. Re-read provider state before each effect.
2. Repair #446 and #450 before new COPY work. Establish E1–E3's reliable evidence
   and receiving-project facts. Prepare #445's Windows backend and bounded catch.
3. Implement #448's coverage/decision records before reporting a broader pass as
   complete. Develop #447's workflow and registration against those contracts.
4. Deliver the three bounded improvements. Reproduce #452 before relying on its
   affected graphs in the replay. Reconcile shared schema/source files rather
   than landing competing representations.
5. Run the expanded controls/replay, review the integrated candidate, confirm
   target merges and retention, and only then cut the release.

## 7. Release acceptance

- Every selected issue's current acceptance is satisfied, with PASS, FAIL,
  BLOCKED or NOT_RUN evidence tied to revision and environment. Do not call the
  whole scope done when a required backend, test or exploration phase is pending.
- Run targeted regressions during implementation and the complete repository CI
  on the integrated candidate: Ruff, format, strict mypy, tests, source/wheel
  packaging, installed-artifact checks, self-digest and hard-quota controls.
  Require the actual Windows/Linux Python 3.11/3.14 jobs; mocks or skipped required
  checks do not replace their execution.
- Recheck source/notice/origin refusals with harmless synthetic markers and safe
  positive controls. No dependency install, setup, test, build or hook runs from
  donor content. New fixture files must have fixture-builder history coverage.
- Review current PR heads after all edits. Require fresh checks for rebased or
  conflict-resolved heads and verify CI on actual merged main/master. Preserve
  source notices and concurrent maintainer changes.
- Retain the expanded coverage report and current experiment PR observations;
  do not rewrite old negative/failed attempts or infer human acceptance from a
  served marker. Confirm intended changes remain on their actual default branch.
- Update the affected skills, CLI help, glossary/contracts and release notes to
  match shipped behavior, including supported acquisition backends, evidence
  capabilities, schema migration and remaining limits.
- Follow [CONTRIBUTING](../../CONTRIBUTING.md): coherent version files and lock,
  release plus next-development commits, rebase merge preserving both commits,
  tag the release commit, successful tag CI, then verified package publication
  when release execution is authorized. Check the installed CLI/plugin artifacts.

## 8. Explicit exclusions

Unattended host enforcement and Scheduled Crab autonomy remain deferred under
[#243](https://github.com/drevendev/HungryCrab/issues/243). This scope does not
inherit that blocker as a requirement to enable autonomy, or claim supervised
tests prove a deployed permission broker. It does not reopen the historical
security batch's completed controls.

Also excluded: paid/live B2 runs or changing frozen benchmark labels, Marketplace
launch, full cache garbage collection, a general parser/interpreter, unrelated
compatibility-matrix expansion, arbitrary new runtime frameworks, public uploads
of private maws, production daemon/account mutations and new recurring jobs.

Planning changes no product code, version, tag, OS feature or installed backend.
The existing [pilot protocol](../experiments/mit-transfer-pilot.md), issue
acceptance and operator's private registry supply the detailed evidence.
