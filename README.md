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
| 2026-09-26 | [yunaremaia/agent-guard](https://github.com/yunaremaia/agent-guard) | [security: add path traversal protection to _normalize_path](https://github.com/yunaremaia/agent-guard/pull/153) *(+2 more)* |
| 2026-09-26 | [yunaremaia/aipr](https://github.com/yunaremaia/aipr) | [fix(ci): update GitHub Actions to known-stable versions](https://github.com/yunaremaia/aipr/pull/128) *(+2 more)* |
| 2026-09-26 | [yunaremaia/gfi](https://github.com/yunaremaia/gfi) | [fix(tests): correct _search_repo call signature](https://github.com/yunaremaia/gfi/pull/57) *(+1 more)* |
| 2026-09-26 | [yunaremaia/memwatch](https://github.com/yunaremaia/memwatch) | [security: add FTS5 query injection and table name validation](https://github.com/yunaremaia/memwatch/pull/70) |
| 2026-09-26 | [yunaremaia/prompt-drift](https://github.com/yunaremaia/prompt-drift) | [fix: replace invalid PyPI classifier 'Topic :: Artificial Intelligence'](https://github.com/yunaremaia/prompt-drift/pull/7) |
| 2026-09-26 | [yunaremaia/depscan](https://github.com/yunaremaia/depscan) | [ci: enhance workflow with matrix and coverage](https://github.com/yunaremaia/depscan/pull/188) *(+1 more)* |
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

## Featured Projects

| Project | What it does | Stack | Tests |
|---------|-------------|-------|-------|
| [driftcheck](https://github.com/yunaremaia/driftcheck) | 61 detectors for version drift between docs and toolchain files — Dockerfile, go.mod, rust-toolchain, package.json, Taskfile, Gradle, .NET/C#, Node 20→24 Actions, and more. `--fix` mode + SARIF output | Python · pytest | 1308 |
| [taintrace](https://github.com/yunaremaia/taintrace) | Typosquat detector for package managers — catches malicious lookalike names before they reach your lockfile | Python · rapidfuzz | 116 |
| [agent-guard](https://github.com/yunaremaia/agent-guard) | Policy-as-code for AI agent permissions — define bounded permissions in YAML, enforce at runtime with shell injection, ReDoS, and symlink path-traversal prevention | Python · YAML | — |
| [agentcost](https://github.com/yunaremaia/agentcost) | Token usage tracker for multi-agent AI sessions — per-agent, per-run cost breakdowns with SQLite persistence | Python · SQLite | 64 |
| [depscan](https://github.com/yunaremaia/depscan) | Multi-ecosystem dependency scanner (PyPI, npm, Cargo, Go, PHP) with vulnerability and typosquat detection | Python | 13 |
| [ci-test-gate](https://github.com/yunaremaia/ci-test-gate) | LLM-powered test selection for CI — runs only tests relevant to the semantic diff, cutting CI minutes | Python | 157 |
| [diff-contract](https://github.com/yunaremaia/diff-contract) | Deterministic guardrails for AI-generated diffs — block changes to protected paths, enforce contract boundaries | Python | 59 |
| [aipr](https://github.com/yunaremaia/aipr) | AI contribution policy scanner for repositories — CI exit codes for humans and agents; detects AI policy gates pre-flight | Python | 37 |
| [vibeguard](https://github.com/yunaremaia/vibeguard) | Security scanner for AI-generated code — shell injection, ReDoS, symlink traversal detection | Python | — |
| [mcp-guard](https://github.com/yunaremaia/mcp-guard) | Security scanner for MCP servers — audit capabilities, detect risks, generate SARIF reports | Python | — |
| [leanpipe](https://github.com/yunaremaia/leanpipe) | CLI output filter for AI agents — strip noise, keep signal, save tokens | Python | — |
| [memwatch](https://github.com/yunaremaia/memwatch) | Agent Memory Health Monitor — scan AI agent memory stores for rot, contradictions, and duplicates | Python | — |
| [ghstats](https://github.com/yunaremaia/ghstats) | GitHub Stats Dashboard — visualize contributions, PRs, and activity from the terminal | Python | — |
| [gfi](https://github.com/yunaremaia/gfi) | Good First Issue finder — search and filter GitHub issues for contributors | Python | — |

---

## Focus Areas

- **Drift Detection** — version drift between documentation and actual toolchain files across 14+ ecosystems (Maven, Terraform, CircleCI, GitLab CI, GitHub Actions, Kubernetes, Helm, Docker Compose, Dependabot, .NET/C#, Taskfile, Gradle, pip, npm, Node 20→24 Actions migration)
- **Dependency Security** — typosquat detection (taintrace), multi-ecosystem vulnerability scanning (depscan), supply-chain risk analysis
- **AI Agent Safety** — policy-as-code permissions with runtime enforcement (agent-guard), security scanning for AI-generated code (vibeguard), MCP server audits (mcp-guard), memory health monitoring (memwatch), CLI output filtering (leanpipe)
- **CI/CD Intelligence** — LLM-powered test selection (ci-test-gate), deterministic diff guardrails (diff-contract), AI policy gates for CI (aipr)
- **Agent Observability** — token usage tracking (agentcost), universal CLI adapters (cli-shim), session memory bridging (context-bridge)

---

## Stats

| Metric | Value |
|--------|-------|
| Public repos | 136 |
| Original projects | 28+ |
| Merged PRs | 125+ |
| Total tests | 1750+ |
| Stars received | 29 |
| Followers | 57 |
| Current streak | see card below |
| Primary language | Python |

---

## Contribution Streak

<p align="center">
  <img src="streak.svg" alt="Contribution streak card — self-hosted, always fresh" width="495" height="195">
</p>

---

## Upstream Contributions

Contributions to **apache/maka**, **modular/modular**, **sharkdp/bat**, **biopython/biopython**, **SeaQL/sea-orm**, **upscayl/upscayl**, and several others. Focus on actionable fixes: version drift, docs sync, test improvements, and CI hardening.

---

## Toolchain

- **Python** (primary) — pytest, click, rich, rapidfuzz, SQLite
- **Rust** — FFI layers, sandboxing primitives, proc-macro security
- **GitHub API** — GraphQL + REST, Actions, CI integration
- **CLI-first** — every tool installable via `pip install git+https://...`, designed for scripting and automation

---

## Reach Me

- **GitHub issues and PRs** are the fastest channel for anything project-related
- **Email:** [yunare@gmail.com](mailto:yunare@gmail.com)
- **Operating agreement:** [inicio.md](https://github.com/yunaremaia/yunaremaia/blob/main/inicio.md) (public-facing identity and contributor rules)

---

## For Contributors

- All projects are **open source first** — PRs welcome in any repo above
- Check each repo's `CONTRIBUTING.md` and AI policy before contributing (use [aipr](https://github.com/yunaremaia/aipr) to auto-detect policy gates)
- Issues labeled `good first issue` are actively maintained — claim before opening a PR
- Public artifacts (PRs, commits, issues) are **English only**

---

*Bio and stats refreshed automatically by [github-profile-keeper](https://github.com/yunaremaia/yunaremaia) cron.*

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/tests-1750%2B-green?logo=pytest)
![Merged PRs](https://img.shields.io/badge/merged_PRs-125+-blue)
![Followers](https://img.shields.io/badge/followers-57-0969da)
![Open source first](https://img.shields.io/badge/open--source--first-FF6B6B?logo=opensourceinitiative)
