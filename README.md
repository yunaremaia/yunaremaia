# Yunare Maia 🇧🇷

Open-source developer from Mossoró, Rio Grande do Norte - Brazil. I build
**driftcheck** — a CLI that catches version drift between docs and toolchain
files before your contributors hit a build failure. I also contribute to agent
runtimes, security scanners, and developer tooling: AI-policy classification,
vulnerability reporting, CLI ergonomics, and the CI hygiene that keeps big repos
mergeable. Steady, reproducible, reviewed — one focused PR at a time.

[![driftcheck](https://img.shields.io/badge/driftcheck-v0.1.46-2ea44f?logo=python&logoColor=white)](https://github.com/yunaremaia/driftcheck)
[![Apache Maka](https://img.shields.io/badge/contributor-apache%2Fmaka-BD0000?logo=apache&logoColor=white)](https://github.com/apache/maka)
[![Modular Mojo](https://img.shields.io/badge/contributor-modular%2Fmodular-black?logo=mojo&logoColor=white)](https://github.com/modular/modular)
[![anchore/syft](https://img.shields.io/badge/contributor-anchore%2Fsyft-239BBA?logo=linux&logoColor=white)](https://github.com/anchore/syft)
[![LMCache](https://img.shields.io/badge/contributor-LMCache%2FLMCache-FF6F00?logo=redis&logoColor=white)](https://github.com/LMCache/LMCache)
[![Merged PRs](https://img.shields.io/badge/merged_prs-80-2ea44f)](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Amerged&type=pullrequests)
[![Open to collaboration](https://img.shields.io/badge/open_to-collaboration-0969da)](mailto:yunare@gmail.com)

<div align="center">

![GitHub stats](./stats.svg)
![Contribution streak](./streak.svg)

</div>

## Now

- **Open PRs:** [open pull requests](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Aopen&type=pullrequests) across
  developer tooling, security scanners, and upstream reproducibility — including
  driftcheck lint hardening, Go lint pass, and GitHub Actions CI hygiene.
  Currently in flight:
  - `yunaremaia/driftcheck#160` — add ruff and mypy linting to CI workflow (fixes #148)
  - `anchore/syft#5302` — skip docker:// references in github-actions PURL generation
  - `LMCache/LMCache#5211` — remove stale G004 ignores for clean connector adapters
  - `karmada-io/karmada#7898` — remove retired Go Report Card badge from README
  - `ray-project/kuberay#5286` — remove unused DecompressStream to clear gosec G110
- **Recently merged:** [browse the live search](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Amerged&type=pullrequests)
  or see the highlights below.

## Featured contributions

- 🔍 **[yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck)** — my own project.
  Detects version drift between docs and toolchain files (README vs Dockerfile,
  build.gradle, pom.xml, versions.tf, .circleci/config.yml, .gitlab-ci.yml,
  GitHub Actions versions, Kubernetes manifests, Helm charts, Taskfiles, and more).
  64 detector modules, 1198+ tests, 25+ drift types.
- 🛡️ **[yunaremaia/aipr](https://github.com/yunaremaia/aipr)** — AI-policy pre-screening
  for contributors: classifies CONTRIBUTING/AI_POLICY/AGENTS docs and flags repos that
  require human-in-the-loop disclosure before you invest hours building a PR.
- ⚡ **[yunaremaia/agentcost](https://github.com/yunaremaia/agentcost)** — track and
  compare LLM API pricing across 20+ models with SQLite persistence for historical
  cost analysis.
- 🏛️ **[apache/maka](https://github.com/apache/maka)** (ASF agent runtime) - five
  merged PRs in one week: [permission-mode refactor](https://github.com/apache/maka/pull/3603),
  [usage-limit billing paths](https://github.com/apache/maka/pull/3660),
  [humanized retry delays](https://github.com/apache/maka/pull/3611),
  [DeepSeek V4 Flash metadata](https://github.com/apache/maka/pull/3732), and a
  [desktop flake fix](https://github.com/apache/maka/pull/3737).
- 📦 **[anchore/syft](https://github.com/anchore/syft)** — Syft is the open-source
  SBOM generator. Contributed PURL generation fixes for GitHub Actions packages
  (skip docker:// references to prevent malformed package URLs).
- 🔐 **[decionis/agent-safe-pipeline](https://github.com/decionis/agent-safe-pipeline)** -
  cryptographic-agility docs, TLS verification posture, and Unicode edge-case
  conformance vectors ([#56](https://github.com/decionis/agent-safe-pipeline/pull/56),
  [#55](https://github.com/decionis/agent-safe-pipeline/pull/55),
  [#23](https://github.com/decionis/agent-safe-pipeline/pull/23)).
- 🧠 **[LMCache/LMCache](https://github.com/LMCache/LMCache)** — KV-cache
  acceleration for LLM inference. Lint hygiene pass removing stale `gosec`
  suppresses now that connector adapters are clean.

## What I work on

- 🔍 **Drift detection** — version drift between docs and toolchain files
  (Dockerfile, build.gradle, pom.xml, versions.tf, CircleCI, GitLab CI,
  GitHub Actions, Kubernetes, Helm, Taskfiles, and more)
- 🤖 **AI policy tooling** — automated pre-screening of AI contribution policies
  so contributors know before building whether a repo accepts autonomous PRs
- 💰 **LLM cost tracking** — pricing APIs, historical cost analysis, model comparison
- 🔬 **Test infrastructure & CI hygiene** — flake elimination, conformance
  vectors, reproducible pipelines (Rust, Python, Mojo, Go, C++)
- 📦 **Software composition analysis** — SBOM generation, PURL correctness,
  vulnerability reporting
- 🔤 **Encoding & Unicode correctness** — UTF-8 sanitization, Windows code-page
  edge cases, `std::error_code` formatter robustness (C++)

## Recent merged work

<!-- yunare-dynamic:start -->
| When | Where | What |
|------|-------|------|
| 2026-09-18 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [fix: replace hand-rolled TOML parser with tomllib (fixes #151)](https://github.com/yunaremaia/driftcheck/pull/157) |
| 2026-09-18 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [feat: add driftcheck init subcommand with auto-detection](https://github.com/yunaremaia/driftcheck/pull/142) |
| 2026-09-18 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [security: prevent absolute path leakage in SARIF output (issue #133)](https://github.com/yunaremaia/driftcheck/pull/138) |
| 2026-09-18 | [yunaremaia/aipr](https://github.com/yunaremaia/aipr) | [perf(detector): cache detect_policy + fix CI indentation (fixes #47)](https://github.com/yunaremaia/aipr/pull/56) |
| 2026-09-18 | [yunaremaia/agentcost](https://github.com/yunaremaia/agentcost) | [feat: add SQLite persistence layer for historical cost tracking (fixes #65)](https://github.com/yunaremaia/agentcost/pull/65) |
| 2026-09-18 | [yunaremaia/vibeguard](https://github.com/yunaremaia/vibeguard) | [docs: API reference for scanner, formatters, CLI (resubmit of #19)](https://github.com/yunaremaia/vibeguard/pull/27) |
| 2026-09-18 | [yunaremaia/gfi](https://github.com/yunaremaia/gfi) | [feat: add GitHub CLI extension mode (gh gfi) (fixes #31)](https://github.com/yunaremaia/gfi/pull/31) |
| 2026-09-16 | [agentguard-ai/tealtiger](https://github.com/agentguard-ai/tealtiger) | [feat(mcp): add detect_secrets tool and redact_secrets utility](https://github.com/agentguard-ai/tealtiger/pull/1) |
| 2026-09-14 | [kelviq/tare](https://github.com/kelviq/tare) | [feat: add Cursor log parsing support to tare](https://github.com/kelviq/tare/pull/11) |
| 2026-09-14 | [ray-project/kuberay](https://github.com/ray-project/kuberay) | [fix(compression): remove unused DecompressStream to clear gosec G110](https://github.com/ray-project/kuberay/pull/5286) |
| 2026-09-08 | [cgrtml/neural-trees](https://github.com/cgrtml/neural-trees) | [feat: migrate packaging to pyproject.toml and wire ruff into CI](https://github.com/cgrtml/neural-trees/pull/46) |
| 2026-09-06 | [rancher/dashboard](https://github.com/rancher/dashboard) | [fix: support IPv6 CIDR in isValidCIDR validator](https://github.com/rancher/dashboard/pull/19043) |
| 2026-09-06 | [oras-project/oras](https://github.com/oras-project/oras) | [fix(ci): resolve licenserc go.mod path relative to config directory](https://github.com/oras-project/oras/pull/1) |
| 2026-09-06 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | [chore(ci): migrate GitHub Actions off deprecated Node 20 runtime](https://github.com/THU-MAIC/OpenMAIC/pull/1343) |
<!-- yunare-dynamic:end -->

## Stack

`TypeScript` `Python` `Rust` `Mojo` `C++` `Go` `Bash` · Node · git-first workflows ·
schema-driven pipelines · distributed test runners · drift detection ·
AI policy tooling · LLM cost tracking

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
