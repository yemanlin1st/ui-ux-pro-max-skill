# Agent instructions — PEFY-GG integration

This repository contains a third-party UI/UX skill fork plus a proposed PEFY-GG integration. Read `PEFY-GG-INTEGRATION.md` before modifying design workflows.

- For interface creation, review and accessibility work, discover `.agents/skills/ui-ux-pro-max/SKILL.md`.
- The upstream skill and the PEFY-GG overlay are distinct. Preserve MIT attribution and respect the upstream licence. Do not silently overwrite vendor source.
- Always disclose the difference between: checked-in files, local skill discovery, cloud ChatGPT workspace installation and actual deployment to external PEFY-GG repositories.
- Prefer generated design systems and measurable UX evidence, but prioritize accessibility, security, law, product requirements, offline accessibility and human-approved controls.
- Never fetch or upload private end-user data to third-party tooling without explicit authorization; do not expose credentials.
- Do not run install/deploy/update, force-push, merge or global changes on behalf of the user without confirmed scope and authority.
- This fork is older than current upstream; use vetted, exact official `ui-ux-pro-max-cli` releases for new projects, not this fork's bundled legacy `uipro-cli`.
- Publish design recommendations with provenance, revision/date, acceptance criteria, deviations and non-conformance risks.
