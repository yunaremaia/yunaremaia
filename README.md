# Yunare Maia 🇧🇷

Open-source developer from Mossoró, Rio Grande do Norte - Brazil. I build
**driftcheck** — a CLI that catches version drift between docs and toolchain
files before your contributors hit a build failure. I also contribute to agent
runtimes and AI infrastructure: provider error classification, retry UX, tool
schemas, test-suite migrations and the CI hygiene that keeps big repos
mergeable. Steady, reproducible, reviewed — one focused PR at a time.

[![driftcheck](https://img.shields.io/badge/driftcheck-v0.1.33-2ea44f?logo=python&logoColor=white)](https://github.com/yunaremaia/driftcheck)
[![Apache Maka](https://img.shields.io/badge/contributor-apache%2Fmaka-BD0000?logo=apache&logoColor=white)](https://github.com/apache/maka)
[![Modular Mojo](https://img.shields.io/badge/contributor-modular%2Fmodular-black?logo=mojo&logoColor=white)](https://github.com/modular/modular)
[![fmtlib/fmt](https://img.shields.io/badge/contributor-fmtlib%2Ffmt-006FC7?logo=cplusplus&logoColor=white)](https://github.com/fmtlib/fmt)
[![VoiceStudio](https://img.shields.io/badge/contributor-VoiceStudio-1E90FF?logo=tauri&logoColor=white)](https://github.com/debpalash/VoiceStudio)
[![Merged PRs (30d)](https://img.shields.io/badge/merged_prs_30d-51-2ea44f)](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Amerged&type=pullrequests)
[![Open to collaboration](https://img.shields.io/badge/open_to-collaboration-0969da)](mailto:yunare@gmail.com)

<div align="center">

![GitHub stats](./stats.svg)
![Contribution streak](./streak.svg)

</div>

## Now

- **Open PRs:** [open pull requests](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Aopen&type=pullrequests) across
  agent runtimes, open-data tooling, and upstream reproducibility — including
  Rust/Go version sync, NER test config, and stdlib test-suite migrations.
  Currently in flight:
  - [`medusajs/medusa#16715`](https://github.com/medusajs/medusa/pull/16715) — fix: translate country and currency names using Intl.DisplayNames — *13 comments* (awaiting review)
  - [`debug-js/debug#1055`](https://github.com/debug-js/debug/pull/1055) — fix: preserve existing namespaces on enable() call — *5 comments* (awaiting review)
  - [`chainloop-dev/chainloop#3406`](https://github.com/chainloop-dev/chainloop/pull/3406) — fix(annotations): allow hyphens in annotation names — *5 comments* (awaiting review)
  - [`kelviq/tare#4`](https://github.com/kelviq/tare/pull/4) — feat: add Cursor log parsing support to tare (awaiting review)
  - [`affaan-m/ECC#2928`](https://github.com/affaan-m/ECC/pull/2928) — fix(docs): make naming conventions language-agnostic (fixes #2830) (awaiting review)
  - [`cratestack/cratestack#929`](https://github.com/cratestack/cratestack/pull/929) — feat(editor): highlight "part", "part of", and "import" as keyword lit (awaiting review)
  - [`rapina-rs/rapina#795`](https://github.com/rapina-rs/rapina/pull/795) — docs(cli): add rapina seed command reference (awaiting review)
  - [`bilawalsidhu/gods-eye-view#119`](https://github.com/bilawalsidhu/gods-eye-view/pull/119) — fix(deps): resolve 9 high-severity npm audit findings in dev/QA toolin (awaiting review)
- **Recently merged:** [browse the live search](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Amerged&type=pullrequests)
  or see the highlights below.

## Featured contributions

- 🔍 **[yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck)** — my own project.
  Detects version drift between docs and toolchain files (README vs Dockerfile,
  build.gradle, pom.xml, versions.tf, .circleci/config.yml, .gitlab-ci.yml,
  GitHub Actions versions, Kubernetes manifests, and more). 40 detectors, 317 tests.
- 🏛️ **[apache/maka](https://github.com/apache/maka)** (ASF agent runtime) — six
  merged PRs including [permission-mode refactor](https://github.com/apache/maka/pull/3603),
  [usage-limit billing paths](https://github.com/apache/maka/pull/3660),
  [humanized retry delays](https://github.com/apache/maka/pull/3611),
  [DeepSeek V4 Flash metadata](https://github.com/apache/maka/pull/3732), and a
  [desktop flake fix](https://github.com/apache/maka/pull/3737).
- ⚡ **[modular/modular](https://github.com/modular/modular)** — stdlib test-suite
  modernization in Mojo: [test_string_span_bounds_abort migration](https://github.com/modular/modular/pull/6957).
- 🔐 **[decionis/agent-safe-pipeline](https://github.com/decionis/agent-safe-pipeline)** —
  cryptographic-agility docs, TLS verification posture, and Unicode edge-case
  conformance vectors ([#56](https://github.com/decionis/agent-safe-pipeline/pull/56),
  [#55](https://github.com/decionis/agent-safe-pipeline/pull/55),
  [#23](https://github.com/decionis/agent-safe-pipeline/pull/23)).
- 📊 **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** —
  vector-store persistence fixes, reproducible CI dependency pinning, and a
  private-IP opt-in for trusted internal APIs
  ([#914](https://github.com/semantica-agi/semantica/pull/914),
  [#945](https://github.com/semantica-agi/semantica/pull/945),
  [#959](https://github.com/semantica-agi/semantica/pull/959)).

## What I work on

- 🔍 **Drift detection** — version drift between docs and toolchain files
  (Dockerfile, build.gradle, pom.xml, versions.tf, CircleCI, GitLab CI,
  GitHub Actions, and more)
- 🤖 **Agent runtimes & LLM tooling** — provider billing/error taxonomies,
  retry UX, MCP tool schemas, capability systems (TypeScript, Python, Rust)
- 🔬 **Test infrastructure & CI hygiene** — flake elimination, conformance
  vectors, reproducible pipelines (Rust, Python, Mojo, C++)
- 🔤 **Encoding & Unicode correctness** — UTF-8 sanitization, Windows code-page
  edge cases, `std::error_code` formatter robustness (C++)
- 📊 **Open data** — schema-validated vendor/startup program datasets

## Recent merged work

<!-- yunare-dynamic:start -->
| When | Where | What |
|------|-------|------|
| 2026-09-07 | [codeforstartups/dynavec](https://github.com/codeforstartups/dynavec) | [docs: add embedding dimension selection guide](https://github.com/codeforstartups/dynavec/pull/148) |
| 2026-09-06 | [oras-project/oras](https://github.com/oras-project/oras) | [fix(ci): resolve licenserc go.mod path relative to config directory](https://github.com/oras-project/oras/pull/2155) |
| 2026-09-06 | [rancher/dashboard](https://github.com/rancher/dashboard) | [fix: support IPv6 CIDR in isValidCIDR validator](https://github.com/rancher/dashboard/pull/19043) |
| 2026-09-06 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [feat(detector): add lockfile drift detection (v0.1.24)](https://github.com/yunaremaia/driftcheck/pull/17) *(+16 more)* |
| 2026-09-06 | [Sekelenao/Flinkboot](https://github.com/Sekelenao/Flinkboot) | [fix(properties): enforce @NotNull on LocalWebUiProperties.enabled](https://github.com/Sekelenao/Flinkboot/pull/110) *(+1 more)* |
| 2026-09-06 | [yunaremaia/skills](https://github.com/yunaremaia/skills) | [docs: fix one-skill install command and name prerequisites for delegating skills](https://github.com/yunaremaia/skills/pull/2) |
| 2026-09-06 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | [chore(ci): migrate GitHub Actions off deprecated Node 20 runtime](https://github.com/THU-MAIC/OpenMAIC/pull/1343) |
| 2026-09-04 | [mavonx/hydra](https://github.com/mavonx/hydra) | [fix: reorder argument validation flow](https://github.com/mavonx/hydra/pull/19) |
| 2026-09-01 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | [fix(packaging): normalize line endings (fixes #144)](https://github.com/tt-a1i/archify/pull/202) *(+2 more)* |
| 2026-08-30 | [yunaremaia/tare](https://github.com/yunaremaia/tare) | [chore: add .gitattributes to normalize line endings](https://github.com/yunaremaia/tare/pull/1) |
| 2026-08-28 | [apache/maka](https://github.com/apache/maka) | [fix(core): add DeepSeek V4 Flash Vision to model metadata](https://github.com/apache/maka/pull/3605) *(+5 more)* |
| 2026-08-27 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | [refactor(ner): remove dead _extract_with_spacy method and unused self.nlp](https://github.com/semantica-agi/semantica/pull/1220) *(+3 more)* |
<!-- yunare-dynamic:end -->

## Stack

`TypeScript` `Python` `Rust` `Mojo` `C++` `Bash` · Node · git-first workflows ·
schema-driven pipelines · distributed test runners · drift detection

## Support

If my open-source work saves you time, you can support it here:

- **Solana / cbBTC:** `Eeztv1nCYUt1fwGWpzKC948gaWfjejYCAuLtUMgzDWbW`
- Or collaborate: pick an [open issue](https://github.com/search?q=author%3Ayunaremaia+is%3Aissue+is%3Aopen&type=issues) I maintain, or ping me below.

---

## Reach me

- GitHub issues and PRs are the fastest channel
- Email: [yunare@gmail.com](mailto:yunare@gmail.com)

---

*Profile refreshed daily by an automation I maintain — tables and stat cards
pulled live from the GitHub API on each run.*
