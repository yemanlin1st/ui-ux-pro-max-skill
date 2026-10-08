---
name: ui-ux-pro-max
description: "Design, implement, and audit accessible, responsive, secure and inclusive web/mobile UI with UI UX Pro Max, including enterprise governance for PEFY-GG projects."
---

# UI UX Pro Max — PEFY-GG Codex adapter

Use this skill for UI/UX requirements, research, experience maps, visual systems, screens, accessible components, design reviews and engineering handover. This adapter makes the **checked-out repository** discoverable in Codex. It does not install software on the user's computer or into ChatGPT.

## Sources and precedence

- Local repository engine: `src/ui-ux-pro-max/scripts/search.py` and `src/ui-ux-pro-max/data/`.
- Local legacy skill reference: `.claude/skills/ui-ux-pro-max/SKILL.md`.
- Governance overlay: `PEFY-GG-INTEGRATION.md`.
- New installations in *other projects*: use the **official** `ui-ux-pro-max-cli` package, not the older `uipro-cli` package bundled in this fork.
- If engine data conflict with a legal, safety, accessibility, security, or user requirement, the verified requirement prevails. Record conflicts and remediation.

## Workflow

1. Clarify product goals, personas, tasks, devices, languages, connectivity, regulatory exposure and data sensitivity.
2. For this checked-out repository, run from its root:
   `python3 src/ui-ux-pro-max/scripts/search.py "fintech inclusive dashboard" --design-system -p "PEFY-GG"`
   Adapt the search terms and product name. Only run source scripts in an approved sandbox after inspecting changes.
3. Select information architecture, task flows, design tokens, text styles, forms and states (loading, error, empty, success, offline, degraded).
4. Implement/advise on responsive UI; accessibility (target WCAG 2.2 AA or the more stringent applicable requirement), security/privacy and performance are release constraints rather than cosmetic options.
5. For low-resource products, design inclusive pathways spanning PWA, assisted agents, USSD, SMS, IVR and offline/delayed sync as applicable; do not pretend visual UI alone covers non-visual channels.
6. Validate keyboard navigation, focus, semantic markup, screen readers, zoom/text reflow, touch target sizes, contrast, localization, small screens, poor connectivity, motion reduction and error recovery.
7. Supply evidence: requirements-to-screen mapping, decision record, design tokens, component inventory, screenshots and test results. Do not claim tests passed without execution evidence.

## Critical constraints

- No customer-sensitive uploads to external design tools without a data classification and explicit authorization.
- No copying third-party proprietary assets without confirming licensing.
- No automatic installation, dependency upgrades or production deployment without approval.
- Do not invent measurement, accessibility conformance, security certifications or production-readiness results.
- Favor existing PEFY-GG design tokens, accessible high-contrast variants and the brand's white / sapphire-blue visual language, subject to per-product requirements.
- Preserve provenance of third-party skill releases and require verification before promoting updates.

## Activation note

Repo-scoped skill discovery begins only after this branch is checked out or merged in an environment that recognizes `.agents/skills/`. Personal/global Codex setup and ChatGPT workspace installation are separate operations. See `PEFY-GG-INTEGRATION.md`.
