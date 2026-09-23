# Yunare Maia 🇧🇷

**Open-source developer from Mossoró, Rio Grande do Norte, Brazil.** Building developer infrastructure for the AI era: drift detection, dependency security, agent observability, and CLI tooling that keeps humans in control of automated pipelines.

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
![Followers](https://img.shields.io/badge/followers-56-0969da)
![Open source first](https://img.shields.io/badge/open--source--first-FF6B6B?logo=opensourceinitiative)
