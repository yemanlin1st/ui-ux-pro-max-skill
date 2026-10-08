# PEFY-GG / MƐTAPEFYON Ω — UI UX Pro Max integration dossier

**Status:** Proposed integration; repository branch only. **Owner:** Dr Erick Franck PATHINVO / PEFY-GG. **Date:** 2026-10-08. **Change class:** Non-production design-workflow enablement.

## 1. Verified baseline and provenance

- Official upstream: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (MIT licence; preserve copyright/attribution).
- Observed upstream main HEAD: `1a2c459b35f26116fd165b0a0f30597f252749ff` at assessment time, **not** a guarantee that the npm package uses this exact commit.
- Latest release visible at assessment: **v2.15.0**. Confirm latest release/tag and the published npm version before installing.
- This preexisting fork, `yemanlin1st/ui-ux-pro-max-skill`, retains an earlier documentation/CLI lineage (`uipro-cli` version 2.2.0 in `cli/package.json`). **Do not assume parity with the current upstream release.**
- The official current npm package is `ui-ux-pro-max-cli`, which exposes the `uipro` command. The old `uipro-cli` package must not be used as a substitute.
- PEFY-GG adapter in `.agents/skills/ui-ux-pro-max/SKILL.md` is PEFY-GG authored integration metadata, not an upstream-certified release.
- License/security/supply-chain review must be refreshed before promotion, including dependencies, lifecycle scripts and the package lock/integrity.

## 2. Deployment scopes (never conflate them)

| Scope | Prepared here | Activation mechanism | Evidence for completion |
| --- | --- | --- | --- |
| This GitHub fork | Yes: repo-local skill + governance | Check out or merge PR, launch Codex from this repo | Codex discovers `ui-ux-pro-max` and a documented design-system smoke case passes |
| Other GitHub repositories | Instructions only | Per-repo installation and pull request under each owner's approval | Each target repo has files, passing checks and accepted PR |
| Local Codex user / other assistants | Instructions only | Run reviewed official CLI on the user's host with scope-specific flags | Skill directory exists, manifest read by runtime, sample invocation passes |
| ChatGPT workspace | Not installed by this PR | Eligible workspace skill creation/install, admin controls | Skill appears as Installed and successfully runs |
| PEFY-GG fabric / MƐTAPEFYON Ω | Governance and contracts documented | Integrate into existing orchestration/config, independently release | Version pin, runtime adapter, RBAC, audit and product-level acceptance verified |

**Eligibility:** According to OpenAI's Skills in ChatGPT help documentation consulted on 2026-10-08, ChatGPT workspace Skills creation/install is available to eligible Business, Enterprise, Healthcare and Edu workspaces, subject to controls. Do not promise a Plus personal ChatGPT account can install the skill globally. Codex has its own compatible skill mechanism.

## 3. Safe install runbook — on a user-controlled host

Prerequisites: Node.js/npm and Python 3; read the official README and inspect the package. Avoid executing arbitrary downloaded scripts as root.

```bash
# 1. Review package and decide which exact reviewed version to pin.
npm view ui-ux-pro-max-cli version dist.tarball dist.integrity
npm view ui-ux-pro-max-cli@2.15.0 scripts dependencies

# 2. In a disposable project, preview and review the planned file changes.
# The version below is the observed release, not a security approval:
npx --yes ui-ux-pro-max-cli@2.15.0 init --ai codex --dry-run

# 3. Only after approval: install into the intended target repository.
npx --yes ui-ux-pro-max-cli@2.15.0 init --ai codex

# 4. Optional: separately add the universal Agent Skills location for the repo.
npx --yes ui-ux-pro-max-cli@2.15.0 init --ai universal

# 5. Inspect and verify. Expected paths depend on selected runtime/version.
find .agents/skills -maxdepth 3 -type f -name SKILL.md -print
git status --short
```

For a **user-level** installation instead of per-repository installation, use the current official CLI and its `--global` mode only after reviewing the generated paths and permissions; e.g. `uipro init --ai universal --global` once the approved CLI has been installed. Never interpret such a shell installation as a cloud ChatGPT-account installation.

Do not run the old fork's bundled `uipro-cli` as if it were the approved v2.15 CLI. Use separate pull requests and inventory evidence when rolling out to actual PEFY-GG repositories. Avoid blanket commits to unrelated forks.

## 4. Integration architecture

```text
Product intake / needs & pain-points
       ↓
ΩAEIF requirement, decision, quality and evidence gates
       ↓
ΩWEBFORGE / ΩVIF / PEFY brand policies (tokens + design governance)
       ↓
UI UX Pro Max adapter (provenance/version pinned)
       ├─ task flows, IA, responsive layouts, palettes and typography
       ├─ accessible components and design-system recommendations
       ├─ stack patterns and implementation checklists
       └─ findings, rationale and proposed code/design changes
       ↓
ΩCSF R2.0 security/privacy policy + ΩRCIAF regulatory checks
       ↓
Human-reviewed PR + accessibility/testing + delivery acceptance
       ↓
Per-product release and real-world performance measurement
```

Governed as a **capability**, not an autonomous authority. It cannot override ΩAEIF construction gates, the ΩCSF security baseline, ΩRCIAF applicability or the user's approved brand and content obligations. Provider-neutral, modular, offline-first and white-label-compatible where practicable.

## 5. Cross-product application

| Target pattern | Primary UI/UX problems to solve | Mandatory adaptations |
| --- | --- | --- |
| AKWƐGBƐ 360™ / FinTech | High-trust onboarding, transaction feedback, fraud warnings | Regulated flows disabled until licensing gates clear; accessible transaction histories; step-up authentication without deceptive patterns |
| EL-VECTOR 360™ / Standards intelligence | Complex applicability, evidence chains, version drift | Traceability, version and jurisdiction indicators; clear uncertainty and human approval |
| GARKAEL Ω / Cyber | Role-aware operations consoles, alert fatigue | RBAC/ABAC cues, critical-action confirmation, tamper-resistant audit |
| PEFY PROSPECT | Qualification/approval pipeline | Transparent scoring, review states, privacy and outbound-approval controls |
| LYSCONEXA / SIRAYA ONJIA | Multi-modal citizen mobility journeys | Feature-phone/SMS/IVR/agent assisted alternatives, low literacy, local languages, low bandwidth |
| PEFY-AGRO | Rural workflows and traceability | Offline-first forms, icon + plain-language support, fallback channels |
| Orange Liberia OHSE IMS | Field HSE reporting and corrective actions | Compact mobile data capture, evidence provenance, incident safety, low-connectivity UX |

No automatic propagation into project repos: each project requires its own integration contract, test case and human authorization.

## 6. Release gates & practical KPI model

**G0 Source qualification:** license, hash/tag, upstream release, packages/scripts/dependencies, advisories and compatibility recorded.

**G1 Design contract:** approved audience, device/network channels, tasks, design tokens, accessibility targets and customer privacy classification.

**G2 Functional proof:** task flows, form completion, validation/error/empty/offline states, RTL/i18n where relevant, handoff components.

**G3 Independent checks:** keyboard and screen-reader use, semantic structure, text scaling/reflow, contrast, mobile touch targets, motion preference, privacy/security review, manual exploratory tests. Automated tools complement, not replace, actual human testing.

**G4 Product pilot:** metrics baselined and measured from real test participants; accessibility and regulated-domain specialists sign off where appropriate.

**G5 Production:** relevant ΩAEIF release evidence, human approval, rollback, telemetry, incident and vulnerability processes ready.

Measure per product only when supported by data: task success (%), task completion time (s), error/retry rate (%), accessibility defects by severity (#), 320/375/768/1024/1440-pixel responsive scenarios passed (#), offline flow success (%), design token violations (#), p75 interaction latency (ms), localization coverage (%). **No fabricated pass or completion percentages.**

## 7. Operational security baseline

- Principle of least privilege, role isolation and project-scoped access; GitHub PR, not direct main-branch force update.
- Supply-chain review: source provenance, license attribution, npm integrity, dependency/SBOM checks, package lifecycle scripts, independent scanning and exact release pin.
- External Figma/MagicPath/AI generation only for classified/authorized data. Do not expose secrets or sensitive design data to unapproved services.
- Privacy by design, consent/notice where required, no manipulative or inaccessible dark patterns.
- WCAG 2.2 AA as an engineering target unless another applicable requirement is stricter; do not assert compliance without audit evidence.
- Brand: PEFY white/diamond + sapphire-blue family; enforce measured readability and accessible contrast rather than visual branding alone.
- Record owner, approver, source ref, test evidence, target repo, deployment date and rollback per rollout.

## 8. Acceptance checklist

- [ ] Draft PR reviewed and merged in this repo, without breaking existing skill.
- [ ] Repo-local Codex discovers the skill on checked-out branch.
- [ ] Sample design-system command executed successfully and output reviewed.
- [ ] Official current CLI release independently vetted.
- [ ] Local/global Codex deployment completed on authorized host.
- [ ] Target PEFY-GG repositories selected and integrated separately via pull requests.
- [ ] ChatGPT workspace eligibility verified, then installation performed by an authorized user/admin if available.
- [ ] Portfolio integration and KPI evidence established in actual runtime(s).

**Decision:** This PR supplies an auditable, non-invasive integration baseline. It does not represent completed account-wide installation, fleet-wide deployment, or certified production readiness.
