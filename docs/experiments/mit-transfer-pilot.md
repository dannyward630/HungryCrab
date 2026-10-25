# MIT-only transfer and PR follow-up pilot

Experiment: `mit-transfer-2026-10-25`. Recorded: 2026-10-25.

**Status: INITIAL STRUCTURAL COMPARISONS COMPLETE; DEEP EXPLORATION INCOMPLETE.** After recording
the rules, the owner explicitly started the experiment on 2026-10-25. The initial
cohort contains ten comparisons per maw (30 pairs; 21 distinct admitted public
MIT donors). Detailed evidence, decisions and PR observations remain in the
excluded local records below. This pilot authorizes no merge, scheduler or
monitoring job; later integration and retention checks remain owner-requested.

The 2026-10-25 retrospective found that generic category dispositions and a
shallow/no-channel acquisition were overinterpreted as complete exploration.
The first pass is evidence of structural comparison and its published changes,
not an exhaustive search for useful behavior. Next-release work is tracked by
[#447](https://github.com/drevendev/HungryCrab/issues/447) and its coverage,
portable-evidence, MIT-metadata and manifest-free-stack follow-ups (#448–#451).

## Question and targets

Can Hungry Crab find useful, reviewable improvements in MIT donors, deliver them
as PRs to the appropriate maw, and retain evidence of whether those improvements
actually reach that maw's default branch?

Plan ten qualified donors for each of three owner-selected maws: HungryCrab,
BeautifulRepo and one private maw. Keep the private maw's identity and all of its
inputs, findings, PR links and evidence in private/local records. The local plan
is `.crab/experiments/mit-transfer-2026-10-25/plan.json`, excluded from Git.

The previous chat shortlist is provisional, not an approved MIT donor list. It
contains non-MIT sources. Rebuild and qualify the list after execution is
authorized; do not count excluded entries as completed comparisons. Ten donors
per maw is a selection target, not a quota of positive findings or PRs.

## Donor eligibility: MIT only

- Accept only a public donor with an established, standard MIT root grant at an
  immutable full commit SHA. Record the licence path, blob identity and verdict.
  A GitHub label, filename, README claim or familiar substring is insufficient.
- For this deliberately narrow pilot, exclude dual/compound grants, MIT-0,
  Apache, BSD, copyleft, custom/restricted, missing, unreadable and uncertain
  grants. Do not substitute clean-room implementation or ideas-only intake to
  admit a non-MIT donor to this cohort.
- Every selected source file, template, configuration or asset must itself be
  covered by MIT. Exclude material with a different nested grant or uncertain
  upstream provenance even when its repository root is MIT. A restrictive rider
  is not ordinary copyright metadata.
- Preserve required copyrights, licence texts and upstream notices in adapted
  material. Verify any matching upstream chain; an MIT intermediary cannot
  erase a different original grant. Discussion/issue prose is not licensed code.
- Recheck `crab sniff` and the pinned digest against the actual maw before a
  transfer. The private maw's own policy/licence must also resolve correctly.
  Unknown/HUMAN, BYPASS or inferred OWN is not a shortcut around cohort admission
  or transfer verification. Do not silently change a maw's policy.

## Execution protocol, once started

1. Record the actual running CLI version/revision and installed plugin revision;
   this pilot starts from released 0.6.4 or a separately verified newer revision.
   Match the maw's actual stack, exclusions, licence and default branch.
2. Qualify the donor and pin both donor and maw revisions. State the concrete
   improvement sought before judging the menu. Check safe acquisition size and
   provide a bounded acquisition environment; standalone catch has no universal
   disk quota. Never execute donor scripts, builds, tests, hooks or installers.
3. Produce fresh, integrity-checked comparison evidence. Do not reuse stale meals
   after a failure or call partial evidence a successful run. Record NO_GAP,
   DUPLICATE, OUT_OF_SCOPE, LICENCE_EXCLUDED and BLOCKED outcomes with reasons.
4. Judge usefulness for this maw. A score, popularity or a runnable donor feature
   does not establish a missing feature here. Avoid changes made solely to
   produce a positive experiment result.
5. Implement a useful selected improvement in the appropriate maw, preserving
   its architecture and required attribution. Verify the change with relevant
   tests and review its diff, publication safety and CI requirements.
6. Open a focused PR directly in that maw. The owner's intended output is a
   working improvement for review; a separate nutrient issue is not required as
   an intermediate deliverable. Do not publish an unimplemented suggestion as a
   completed transfer. Use the existing guarded serving/receipt protocol when
   applicable and respect the target repository's instructions.
7. Immediately record the PR and source evidence in the private/local follow-up
   registry. Opening a PR is not acceptance. Do not merge, enable auto-merge,
   deploy, release or enable autonomous work as part of this pilot without
   separate applicable owner authorization.

## Durable records and later follow-up

Create actual comparison/PR records only when there is evidence. No experiment
PR exists at registration; the earlier implementation/release PRs are not pilot
outcomes. Do not rely on chat memory alone. Keep the trace chain:

`experiment -> maw -> pinned donor -> meal -> nutrient -> implementation PR -> default branch`

For each comparison retain: comparison ID, maw identity and base SHA, donor URL
and full SHA, verified MIT evidence, tool/policy versions, fresh meal location,
candidate decisions and outcome/reason. For each created PR additionally retain:

| Field | Required evidence |
|---|---|
| Identity | Experiment/comparison/nutrient IDs, target repo, PR number and URL. |
| Change | Concrete benefit, changed paths and attribution/receipt reference. |
| Creation | Creation time, base branch/base SHA and initial head SHA. |
| Review | Latest head SHA, actual CI run URLs/results, review findings and revisions. |
| Outcome | OPEN, DRAFT, CLOSED_UNMERGED, MERGED_NONDEFAULT, MERGED_DEFAULT_UNVERIFIED, MERGED_DEFAULT_CONFIRMED, REVERTED or UNKNOWN; last checked time and evidence. |
| Integration | Provider merge state/date/SHA, actual default-branch name and the default-branch SHA inspected. |
| Retention | Whether the intended change remains, was amended or was reverted at the inspected default-branch revision. |

At later owner-requested follow-up, read provider truth again. Verify that the
merge commit is reachable from the actual default branch, whether named master
or main. A merge into another branch remains MERGED_NONDEFAULT until it reaches
the default branch. Inspect the resulting change as well: reachable merge
ancestry alone does not prove that a subsequently reverted improvement remains.
Record uncertainty instead of inferring integration from green CI, a closed PR
or an agent's completion message. Preserve earlier observations when appending
new snapshots. Separate human acceptance from automatic served/publication state.

Report qualified/excluded donors, comparisons and their negative/blocked results,
useful candidates, opened PRs, merged/default-confirmed PRs and retained/reverted
changes. Keep the denominators visible; do not omit unsuccessful meals.

Follow-up is manual when requested. This record creates no timer, recurring
automation or background watcher. No private maw data may be published in this
public repository or its issues, PRs, Actions artifacts or release notes.
