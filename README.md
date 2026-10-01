# Yunare Maia 🇧🇷

Open-source developer from Mossoró, Rio Grande do Norte — Brazil. I build tools that
keep repositories honest: [driftcheck](https://github.com/yunaremaia/driftcheck) catches
version drift between documentation and the files that actually build the project,
[taintrace](https://github.com/yunaremaia/taintrace) catches typosquatted package names,
and a family of small guardrails keeps generated changes inside the lines you drew.

**[228 merged PRs](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Amerged&type=pullrequests)
— 183 in my own projects, 45 upstream across 25 repositories.** Six tools are
[on PyPI](#install).

[![Merged PRs](https://img.shields.io/badge/merged_PRs-228-2ea44f)](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Amerged&type=pullrequests)
[![Upstream](https://img.shields.io/badge/upstream_repos-25-0969da)](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Amerged&type=pullrequests)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Open to collaboration](https://img.shields.io/badge/open_to-collaboration-FF6B6B)](mailto:yunare@gmail.com)
[![apache/maka](https://img.shields.io/badge/contributor-apache%2Fmaka-BD0000?logo=apache&logoColor=white)](https://github.com/apache/maka)
[![anchore/syft](https://img.shields.io/badge/contributor-anchore%2Fsyft-239BBA?logo=linux&logoColor=white)](https://github.com/anchore/syft)
[![LMCache](https://img.shields.io/badge/contributor-LMCache%2FLMCache-FF6F00?logo=redis&logoColor=white)](https://github.com/LMCache/LMCache)
[![ORAS](https://img.shields.io/badge/contributor-oras--2.5k-8A2BE2)](https://github.com/oras-project/oras)

<div align="center">

![GitHub stats](./stats.svg)
![Contribution streak](./streak.svg)

</div>

## Start here

| I want to… | Use |
|---|---|
| catch version drift before CI does | `pip install driftcheck-py` → [driftcheck](https://github.com/yunaremaia/driftcheck) |
| catch typosquatted dependencies | `pip install taintrace` → [taintrace](https://github.com/yunaremaia/taintrace) |
| block out-of-scope changes to protected paths | `pip install diff-contract` → [diff-contract](https://github.com/yunaremaia/diff-contract) |
| run only the CI tests a change actually affects | `pip install ci-test-gate` → [ci-test-gate](https://github.com/yunaremaia/ci-test-gate) |
| check a repo's AI policy before contributing | `pip install aipr-py` → [aipr](https://github.com/yunaremaia/aipr) |
| track token cost across agent runs | `pip install agentcost` → [agentcost](https://github.com/yunaremaia/agentcost) |

Every tool is MIT-licensed, installable from PyPI, and runs on Python 3.10+.

## Featured work

### [driftcheck](https://github.com/yunaremaia/driftcheck) · 1485 tests

Your README promises Node 18, your `package.json` says 24, and a new contributor
discovers it as a build failure. `driftcheck` catches it in CI instead.

86 detector modules across Maven, Gradle, Terraform, CircleCI, GitLab CI, GitHub
Actions, Kubernetes, Helm, Docker Compose, Dependabot, .NET/C#, Taskfile, Rust
toolchain files, Go modules, npm/pnpm/yarn lockfiles, proto schemas, SPDX license
headers, dotfiles, `.env`, and the A2A agent protocol. `--fix` rewrites the
documentation side; `--sarif` emits SARIF 2.1.0 for GitHub code scanning.

**1485 tests, green on Python 3.10–3.14 across Linux, macOS and Windows.**

### [taintrace](https://github.com/yunaremaia/taintrace) · 178 tests

`reqeusts` instead of `requests` is one character away from a malicious package.
Detects typosquat lookalikes across Cargo, Go, npm and PyPI before they reach a
lockfile.

### Upstream contributions · 45 merged PRs across 25 repos

Defects with an actual reproduction, not drive-by changes:

- **[apache/maka](https://github.com/apache/maka)** (5.7k⭐, agent runtime) — six merged PRs, including
  [dropping a retired permission mode from the capability audit](https://github.com/apache/maka/pull/3603)
  and [classifying usage-limit failures as billing rather than auth](https://github.com/apache/maka/pull/3660).
- **[anchore/syft](https://github.com/anchore/syft)** (9.6k⭐, SBOM generator) —
  [skip `docker://` references in GitHub Actions PURL generation](https://github.com/anchore/syft/pull/5302),
  which were producing malformed package URLs.
- **[LMCache](https://github.com/LMCache/LMCache)** (11.9k⭐, KV-cache for inference) —
  [removed stale `gosec` suppressions](https://github.com/LMCache/LMCache/pull/5211) once the connector
  adapters were clean.
- **[oras-project/oras](https://github.com/oras-project/oras)** (2.5k⭐) —
  [fixed a licenserc CI path resolved relative to the wrong directory](https://github.com/oras-project/oras/pull/2155).
- **[rancher/dashboard](https://github.com/rancher/dashboard)** —
  [IPv6 CIDR support in the network validator](https://github.com/rancher/dashboard/pull/19043).

Plus merged work in `MisakaNet`, `semantica`, `agent-safe-pipeline`, `Agentrace`,
`OpenMAIC`, `cratestack`, `neural-trees`, `tealtiger`, `Prism-platform`, and others.

## Now

Six PRs open — two need a maintainer click, the rest are under review:

- [`ray-project/kuberay#5286`](https://github.com/ray-project/kuberay/pull/5286) — remove an unused
  `DecompressStream` to clear gosec G110 (37 checks green, awaiting maintainer)
- [`ayghri/i-have-adhd#225`](https://github.com/ayghri/i-have-adhd/pull/225) — replace a `node -e` launcher
  with POSIX sh for Node-free environments
- [`driftcheck#457`](https://github.com/yunaremaia/driftcheck/pull/457) — cover the Python 3.10 TOML
  spelling in the declared-dependency guard

Browse the [full list](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Aopen&type=pullrequests).

## Recent merged work

<!-- yunare-dynamic:start -->
| When | Where | What |
|------|-------|------|
| 2026-10-01 | [yunaremaia/a2a-drift](https://github.com/yunaremaia/a2a-drift) | [fix: match protocolVersion by major.minor instead of substring](https://github.com/yunaremaia/a2a-drift/pull/27) *(+1 more)* |
| 2026-10-01 | [yunaremaia/depscan](https://github.com/yunaremaia/depscan) | [fix(ci): add missing pytest-cov dep and drop duplicate test class](https://github.com/yunaremaia/depscan/pull/221) *(+1 more)* |
| 2026-10-01 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [fix(ci): serialize the Pages deployment so merged batches do not race](https://github.com/yunaremaia/driftcheck/pull/452) *(+2 more)* |
| 2026-10-01 | [yunaremaia/cli-shim](https://github.com/yunaremaia/cli-shim) | [build: migrate packaging metadata to pyproject.toml](https://github.com/yunaremaia/cli-shim/pull/65) |
| 2026-10-01 | [yunaremaia/oss-contribution-finder](https://github.com/yunaremaia/oss-contribution-finder) | [build: complete project metadata for PyPI publishing](https://github.com/yunaremaia/oss-contribution-finder/pull/59) |
| 2026-10-01 | [yunaremaia/mcp-guard](https://github.com/yunaremaia/mcp-guard) | [build: complete project metadata for PyPI publishing](https://github.com/yunaremaia/mcp-guard/pull/78) |
<!-- yunare-dynamic:end -->

## What I work on

**Drift detection** — the recurring theme. When a value is declared in two places,
something will eventually make them disagree, and the failure surfaces to a user as a
confusing build error instead of the configuration mismatch it actually is.
[`driftcheck`](https://github.com/yunaremaia/driftcheck) (86 detectors), plus
[`a2a-drift`](https://github.com/yunaremaia/a2a-drift),
[`prompt-drift`](https://github.com/yunaremaia/prompt-drift),
[`env-drift`](https://github.com/yunaremaia/env-drift),
[`proto-drift`](https://github.com/yunaremaia/proto-drift),
[`license-drift`](https://github.com/yunaremaia/license-drift),
[`dotfiles-drift`](https://github.com/yunaremaia/dotfiles-drift),
[`org-policy-drift`](https://github.com/yunaremaia/org-policy-drift),
[`ci-gate-watch`](https://github.com/yunaremaia/ci-gate-watch).

**Supply-chain security** — [`taintrace`](https://github.com/yunaremaia/taintrace) (typosquat detection
for Cargo/Go/npm/PyPI), [`depscan`](https://github.com/yunaremaia/depscan) (multi-ecosystem vulnerability
scanning), [`ai-reputation-guard`](https://github.com/yunaremaia/ai-reputation-guard).

**Guardrails for generated changes** — the premise: a large diff is fine; a *silent*
out-of-scope one is not. [`diff-contract`](https://github.com/yunaremaia/diff-contract) fails a run that
touches protected paths, [`aipr`](https://github.com/yunaremaia/aipr) surfaces a repo's AI policy before you
build, [`agent-guard`](https://github.com/yunaremaia/agent-guard) enforces bounded permissions at runtime,
[`vibeguard`](https://github.com/yunaremaia/vibeguard) and [`mcp-guard`](https://github.com/yunaremaia/mcp-guard) scan
generated code and MCP servers, [`ai-reputation-guard`](https://github.com/yunaremaia/ai-reputation-guard) scores
contributions that look low-effort.

**CI intelligence** — [`ci-test-gate`](https://github.com/yunaremaia/ci-test-gate) (semantic test
selection), [`ci-sandbox`](https://github.com/yunaremaia/ci-sandbox) (see what a pipeline *would* run
without running it), [`ghstats`](https://github.com/yunaremaia/ghstats) (contribution dashboard),
[`gfi`](https://github.com/yunaremaia/gfi) (good-first-issue finder).

**Agent observability** — [`agentcost`](https://github.com/yunaremaia/agentcost) (token spend),
[`memwatch`](https://github.com/yunaremaia/memwatch) (memory rot detection),
[`context-bridge`](https://github.com/yunaremaia/context-bridge) (session memory),
[`agent-checkpoint`](https://github.com/yunaremaia/agent-checkpoint) (crash recovery),
[`agent-undo`](https://github.com/yunaremaia/agent-undo) (rollback),
[`agent-workspace`](https://github.com/yunaremaia/agent-workspace) (worktree isolation),
[`leanpipe`](https://github.com/yunaremaia/leanpipe) (CLI output filtering).

## Install

```bash
pip install driftcheck-py    # version drift across 86 detectors
pip install taintrace        # typosquat detection
pip install diff-contract    # diff guardrails
pip install ci-test-gate     # semantic CI test selection
pip install aipr-py          # AI contribution policy detection
pip install agentcost        # LLM token cost tracking
```

Source, issues and PRs live in the `yunaremaia/*` repos above.

## Stack

`Python` `Rust` `C++` `Go` `TypeScript` `Mojo` `Bash` · pytest · GitHub Actions · SARIF ·
SQLite · rapidfuzz · CLI-first, scriptable, no daemon

## Stats

| Metric | Value |
|--------|-------|
| Merged PRs | 228 |
| — in my own projects | 183 |
| — upstream, across 25 repos | 45 |
| Own projects | 43 |
| Public repos | 142 |
| — of which forks of other people's work | 99 |
| Tests across featured tools | 2200+ |
| Packages on PyPI | 6 |
| Stars | 24 |
| Followers | 58 |
| Primary language | Python |

## Contributing

PRs are welcome in any repo above. Before you open one:

- Read the repo's `CONTRIBUTING.md` and any AI policy — [`aipr`](https://github.com/yunaremaia/aipr)
  detects those gates automatically
- Issues labeled `good first issue` are actively maintained — claim before starting
- **All public artifacts (PRs, commits, issues, comments) are in English**

## Support

If this saves you time, you can support it:

- **Solana / cbBTC:** `Eeztv1nCYUt1fwGWpzKC948gaWfjejYCAuLtUMgzDWbW`
- Or collaborate — pick an [open issue](https://github.com/search?q=author%3Ayunaremaia+is%3Aissue+is%3Aopen&type=issues)
  in a project above

## Reach me

- **Email:** [yunare@gmail.com](mailto:yunare@gmail.com)
- **GitHub issues and PRs** — fastest channel for anything project-related
- **Operating agreement:** [inicio.md](blob/main/inicio.md) — public identity and contributor rules

---

*Numbers verified against the GitHub API.*
