# Yunare Maia 🇧🇷

Open-source developer from Mossoró, Rio Grande do Norte - Brazil. I build
**driftcheck** — a CLI that catches version drift between docs and toolchain
files before your contributors hit a build failure. I also contribute to agent
runtimes and AI infrastructure: provider error classification, retry UX, tool
schemas, test-suite migrations and the CI hygiene that keeps big repos
mergeable. Steady, reproducible, reviewed — one focused PR at a time.

[![driftcheck](https://img.shields.io/badge/driftcheck-v0.1.14-2ea44f?logo=python&logoColor=white)](https://github.com/yunaremaia/driftcheck)
[![Apache Maka](https://img.shields.io/badge/contributor-apache%2Fmaka-BD0000?logo=apache&logoColor=white)](https://github.com/apache/maka)
[![Modular Mojo](https://img.shields.io/badge/contributor-modular%2Fmodular-black?logo=mojo&logoColor=white)](https://github.com/modular/modular)
[![fmtlib/fmt](https://img.shields.io/badge/contributor-fmtlib%2Ffmt-006FC7?logo=cplusplus&logoColor=white)](https://github.com/fmtlib/fmt)
[![VoiceStudio](https://img.shields.io/badge/contributor-VoiceStudio-1E90FF?logo=tauri&logoColor=white)](https://github.com/debpalash/VoiceStudio)
[![Merged PRs (30d)](https://img.shields.io/badge/merged_prs_30d-24-2ea44f)](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Amerged&type=pullrequests)
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
  - `fmtlib/fmt#4918` — sanitize non-UTF-8 bytes from `std::error_code::message()` (fixes #4436)
  - `debpalash/VoiceStudio#1801` — guard null `seg.start/end` in `.toFixed()` (fixes #1798)
  - `THU-MAIC/OpenMAIC#1343` — CI: bump `upload-artifact` + `cache` to Node 24 versions (awaiting re-review)
  - `medusajs/medusa#16715` — translate country/currency names using `Intl.DisplayNames` (awaiting review)
  - `rancher/dashboard#19043` — support IPv6 CIDR in `isValidCIDR` validator (awaiting review)
- **Recently merged:** [browse the live search](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Amerged&type=pullrequests)
  or see the highlights below.

## Featured contributions

- 🔍 **[yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck)** — my own project.
  Detects version drift between docs and toolchain files (README vs Dockerfile,
  build.gradle, pom.xml, versions.tf, .circleci/config.yml, .gitlab-ci.yml,
  GitHub Actions versions, and more). 80+ tests, 15 drift types.
- 🏛️ **[apache/maka](https://github.com/apache/maka)** (ASF agent runtime) - five
  merged PRs in one week: [permission-mode refactor](https://github.com/apache/maka/pull/3603),
  [usage-limit billing paths](https://github.com/apache/maka/pull/3660),
  [humanized retry delays](https://github.com/apache/maka/pull/3611),
  [DeepSeek V4 Flash metadata](https://github.com/apache/maka/pull/3732), and a
  [desktop flake fix](https://github.com/apache/maka/pull/3737).
- ⚡ **[modular/modular](https://github.com/modular/modular)** - stdlib test-suite
  modernization in Mojo: [test_string_span_bounds_abort migration](https://github.com/modular/modular/pull/6957).
- 🔐 **[decionis/agent-safe-pipeline](https://github.com/decionis/agent-safe-pipeline)** -
  cryptographic-agility docs, TLS verification posture, and Unicode edge-case
  conformance vectors ([#56](https://github.com/decionis/agent-safe-pipeline/pull/56),
  [#55](https://github.com/decionis/agent-safe-pipeline/pull/55),
  [#23](https://github.com/decionis/agent-safe-pipeline/pull/23)).
- 📊 **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** -
  vector-store persistence fixes, reproducible CI dependency pinning, and a
  private-IP opt-in for trusted internal APIs
  ([#914](https://github.com/semantica-agi/semantica/pull/914),
  [#945](https://github.com/semantica-agi/semantica/pull/945),
  [#959](https://github.com/semantica-agi/semantica/pull/959)).

## What I work on

- 🔍 **Drift detection** — version drift between docs and toolchain files
  (Dockerfile, build.gradle, pom.xml, versions.tf, CircleCI, GitLab CI,
  GitHub Actions, and more)
- 🤖 **Agent runtimes & LLM tooling** - provider billing/error taxonomies,
  retry UX, MCP tool schemas, capability systems (TypeScript, Python, Rust)
- 🔬 **Test infrastructure & CI hygiene** - flake elimination, conformance
  vectors, reproducible pipelines (Rust, Python, Mojo, C++)
- 🔤 **Encoding & Unicode correctness** - UTF-8 sanitization, Windows code-page
  edge cases, `std::error_code` formatter robustness (C++)
- 📊 **Open data** - schema-validated vendor/startup program datasets

## Recent merged work

<!-- yunare-dynamic:start -->
| When | Where | What |
|------|-------|------|
| 2026-09-04 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [feat(detector): add GitHub Actions version drift detection (v0.1.14)](https://github.com/yunaremaia/driftcheck/pull/7) |
| 2026-09-04 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [feat(detector): add GitLab CI drift detection (v0.1.13)](https://github.com/yunaremaia/driftcheck/pull/6) |
| 2026-09-04 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [feat(detector): add CircleCI drift detection (v0.1.12)](https://github.com/yunaremaia/driftcheck/pull/5) |
| 2026-09-04 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [feat(detector): add Terraform drift detection (v0.1.11)](https://github.com/yunaremaia/driftcheck/pull/4) |
| 2026-09-04 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [feat(detector): add Maven pom.xml drift detection (v0.1.10)](https://github.com/yunaremaia/driftcheck/pull/3) |
| 2026-09-04 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [feat(detector): add Docker and Java/Gradle drift detection (v0.1.9)](https://github.com/yunaremaia/driftcheck/pull/2) |
| 2026-08-30 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | [fix(dataflow): drop degenerate points so vertical edges keep a real final segment](https://github.com/tt-a1i/archify/pull/203) |
| 2026-08-28 | [apache/maka](https://github.com/apache/maka) | [fix(core): add DeepSeek V4 Flash Vision to model metadata](https://github.com/apache/maka/pull/3605) *(+5 more)* |
| 2026-08-27 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | [refactor(ner): remove dead _extract_with_spacy method and unused self.nlp](https://github.com/semantica-agi/semantica/pull/1220) *(+3 more)* |
| 2026-08-17 | [decionis/agent-safe-pipeline](https://github.com/decionis/agent-safe-pipeline) | [docs: cryptographic agility and TLS verification posture (closes #51)](https://github.com/decionis/agent-safe-pipeline/pull/56) *(+2 more)* |
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

*Profile refreshed daily by an automation I maintain - tables and stat cards
pulled live from the GitHub API on each run.*
