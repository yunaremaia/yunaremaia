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
[![ripgrep](https://img.shields.io/badge/contributor-sharkdp%2Fripgrep-006FC7?logo=rust&logoColor=white)](https://github.com/sharkdp/ripgrep)
[![Biopython](https://img.shields.io/badge/contributor-biopython-3776AB?logo=python&logoColor=white)](https://github.com/biopython/biopython)
[![Merged PRs](https://img.shields.io/badge/merged_prs-56+-2ea44f)](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Amerged&type=pullrequests)
[![Open PRs](https://img.shields.io/badge/open_prs-20-0969da)](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Aopen&type=pullrequests)
[![Open to collaboration](https://img.shields.io/badge/open_to-collaboration-0969da)](mailto:yunare@gmail.com)

<div align="center">

![GitHub stats](./stats.svg)
![Contribution streak](./streak.svg)

</div>

## Now

- **Open PRs:** [open pull requests](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Aopen&type=pullrequests) across
  agent runtimes, developer tooling, and upstream reproducibility — including
  CI modernization, i18n consistency, docs coverage, and grammar fixes.
  Currently in flight:
  - [`DietrichGebert/ponytail#832`](https://github.com/DietrichGebert/ponytail/pull/832) — chore(ci): bump GitHub Actions to Node 24-compatible versions
  - [`django-helpdesk/django-helpdesk#1428`](https://github.com/django-helpdesk/django-helpdesk/pull/1428) — chore(i18n): standardize templates on translate/blocktranslate tags
  - [`reticlehq/reticle#860`](https://github.com/reticlehq/reticle/pull/860) — feat: add // @reticle-ignore comment to skip source stamping per-file
  - [`AgentPostmortem/Agentrace#32`](https://github.com/AgentPostmortem/Agentrace/pull/32) — fix(parse): guard _ts against non-string timestamp values
  - [`doobidoo/mcp-memory-service#1174`](https://github.com/doobidoo/mcp-memory-service/pull/1174) — fix(scripts): import mcp_memory_service via editable install
  - [`sharkdp/bat#3936`](https://github.com/sharkdp/bat/pull/3936) — docs: update MSRV in README from 1.79 to 1.88
  - [`chainloop-dev/chainloop#3406`](https://github.com/chainloop-dev/chainloop/pull/3406) — fix(annotations): allow hyphens in annotation names
  - [`rapina-rs/rapina#795`](https://github.com/rapina-rs/rapina/pull/795) — docs(cli): add rapina seed command reference
  - [`cratestack/cratestack#929`](https://github.com/cratestack/cratestack/pull/929) — feat(editor): highlight "part", "part of", and "import" as keyword literals
  - [`VeridionLabs/veridion#88`](https://github.com/VeridionLabs/veridion/pull/88) — feat(plugins): add UncheckedReturnPlugin
  - [`debug-js/debug#1055`](https://github.com/debug-js/debug/pull/1055) — fix: preserve existing namespaces on enable() call
  - [`medusajs/medusa#16715`](https://github.com/medusajs/medusa/pull/16715) — fix: translate country and currency names using Intl.DisplayNames
  - [`coopfinance/coopfin-contracts#34`](https://github.com/coopfinance/coopfin-contracts/pull/34) — docs(contracts): add rustdoc comments to all 5 Soroban contracts
  - [`firecrawl/pdf-inspector#484`](https://github.com/firecrawl/pdf-inspector/pull/484) — fix: expand bullet glyph recognition in markdown classifier
  - [`affaan-m/ECC#2928`](https://github.com/affaan-m/ECC/pull/2928) — fix(docs): make naming conventions language-agnostic
  - [`affaan-m/ECC#2927`](https://github.com/affaan-m/ECC/pull/2927) — fix(commands): give prp-pr a distinct description from pr
  - [`K-Dense-AI/scientific-agent-skills#248`](https://github.com/K-Dense-AI/scientific-agent-skills/pull/248) — fix: normalize skill count in README and citation metadata
  - [`MunGell/awesome-for-beginners#2111`](https://github.com/MunGell/awesome-for-beginners/pull/2111) — Add LibreSign to the list
  - [`up-for-grabs/up-for-grabs.net#6119`](https://github.com/up-for-grabs/up-for-grabs.net/pull/6119) — Add LibreSign to projects
- **Recently merged:** [browse the live search](https://github.com/search?q=author%3Ayunaremaia+is%3Apr+is%3Amerged&type=pullrequests)
  or see the highlights below.

## Featured contributions

- 🔍 **[yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck)** — my own project.
  Detects version drift between docs and toolchain files (README vs Dockerfile,
  build.gradle, Gradle Version Catalog, pom.xml, versions.tf, Pipfile/Conda envs,
  Elixir mix.exs, CMakeLists.txt, .circleci/config.yml, .gitlab-ci.yml,
  GitHub Actions versions, Kubernetes manifests, Helm charts, Swift Package.swift,
  Bun lockfiles, PHP/Composer, Ruby versions, environment files, and more).
  41 detectors, 319 tests, v0.1.33.
- 📜 **[yunaremaia/aipr](https://github.com/yunaremaia/aipr)** — my own project.
  Reads an open-source repository's AI contribution policy before you (or your
  agent) contributes. Exit codes for CI/agents.
- 🏛️ **[apache/maka](https://github.com/apache/maka)** (ASF agent runtime) — six
  merged PRs including [permission-mode refactor](https://github.com/apache/maka/pull/3603),
  [usage-limit billing paths](https://github.com/apache/maka/pull/3660),
  [humanized retry delays](https://github.com/apache/maka/pull/3611),
  [DeepSeek V4 Flash metadata](https://github.com/apache/maka/pull/3732), and a
  [desktop flake fix](https://github.com/apache/maka/pull/3737).
- ⚡ **[modular/modular](https://github.com/modular/modular)** — stdlib test-suite
  modernization in Mojo: [test_string_span_bounds_abort migration](https://github.com/modular/modular/pull/6957).
- 🌳 **[cgrtml/neural-trees](https://github.com/cgrtml/neural-trees)** —
  [packaging migration to pyproject.toml + ruff CI](https://github.com/cgrtml/neural-trees/pull/46).
- 📐 **[codeforstartups/dynavec](https://github.com/codeforstartups/dynavec)** —
  [embedding dimension selection guide](https://github.com/codeforstartups/dynavec/pull/148).
- 📊 **[DaBestCode/JudgeGauge](https://github.com/DaBestCode/JudgeGauge)** —
  [deterministic Markdown report renderer](https://github.com/DaBestCode/JudgeGauge/pull/5).
- ☕ **[Sekelenao/Flinkboot](https://github.com/Sekelenao/Flinkboot)** —
  [@NotNull constraint fix](https://github.com/Sekelenao/Flinkboot/pull/110) and
  [ValidatorFactory lazy-init leak fix](https://github.com/Sekelenao/Flinkboot/pull/106).
- 🔐 **[decionis/agent-safe-pipeline](https://github.com/decionis/agent-safe-pipeline)** —
  cryptographic-agility docs, TLS verification posture, and Unicode edge-case
  conformance vectors ([#56](https://github.com/decionis/agent-safe-pipeline/pull/56),
  [#55](https://github.com/decionis/agent-safe-pipeline/pull/55),
  [#23](https://github.com/decionis/agent-safe-pipeline/pull/23)).
- 📦 **[oras-project/oras](https://github.com/oras-project/oras)** (OCI registry
  tooling) — [licenserc go.mod path fix](https://github.com/oras-project/oras/pull/2155).
- 🐳 **[rancher/dashboard](https://github.com/rancher/dashboard)** —
  [IPv6 CIDR validation support](https://github.com/rancher/dashboard/pull/19043).
- 🎓 **[THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)** —
  [CI modernization: migrate off deprecated Node 20 runtime](https://github.com/THU-MAIC/OpenMAIC/pull/1343).
- 🧠 **[Ikalus1988/MisakaNet](https://github.com/Ikalus1988/MisakaNet)** —
  lesson quality gates, MCP endpoint docs, and test coverage expansion
  ([#894](https://github.com/Ikalus1988/MisakaNet/pull/894),
  [#893](https://github.com/Ikalus1988/MisakaNet/pull/893)).
- 📊 **[semantica-agi/semantica](https://github.com/semantica-agi/semantica)** —
  vector-store persistence fixes, reproducible CI dependency pinning, and a
  private-IP opt-in for trusted internal APIs
  ([#914](https://github.com/semantica-agi/semantica/pull/914),
  [#945](https://github.com/semantica-agi/semantica/pull/945),
  [#959](https://github.com/semantica-agi/semantica/pull/959)).
- 🔎 **[sharkdp/bat](https://github.com/sharkdp/bat)** —
  [MSRV documentation update](https://github.com/sharkdp/bat/pull/3936).
- 🧬 **[biopython/biopython](https://github.com/biopython/biopython)** —
  contributions to the official Biopython repository.
- 🤖 **[AgentPostmortem/Agentrace](https://github.com/AgentPostmortem/Agentrace)** —
  [parse guard for non-string timestamps](https://github.com/AgentPostmortem/Agentrace/pull/32).
- 🧠 **[doobidoo/mcp-memory-service](https://github.com/doobidoo/mcp-memory-service)** —
  [editable install fix](https://github.com/doobidoo/mcp-memory-service/pull/1174).

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
| 2026-09-08 | [DaBestCode/JudgeGauge](https://github.com/DaBestCode/JudgeGauge) | [feat: add deterministic Markdown report renderer](https://github.com/DaBestCode/JudgeGauge/pull/5) |
| 2026-09-08 | [cgrtml/neural-trees](https://github.com/cgrtml/neural-trees) | [feat: migrate packaging to pyproject.toml and wire ruff into CI](https://github.com/cgrtml/neural-trees/pull/46) |
| 2026-09-07 | [codeforstartups/dynavec](https://github.com/codeforstartups/dynavec) | [docs: add embedding dimension selection guide](https://github.com/codeforstartups/dynavec/pull/148) |
| 2026-09-07 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [feat(detector): add lockfile drift detection (v0.1.24)](https://github.com/yunaremaia/driftcheck/pull/17) |
| 2026-09-07 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [refactor: modular architecture + PHP/Composer and Bun detectors (v0.1.23)](https://github.com/yunaremaia/driftcheck/pull/16) |
| 2026-09-07 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [ci: expand test matrix to ubuntu/macos/windows, Python 3.10-3.14; add integration tests](https://github.com/yunaremaia/driftcheck/pull/15) |
| 2026-09-07 | [Sekelenao/Flinkboot](https://github.com/Sekelenao/Flinkboot) | [fix(properties): enforce @NotNull on LocalWebUiProperties.enabled](https://github.com/Sekelenao/Flinkboot/pull/110) |
| 2026-09-07 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [feat(detector): add Ruby version drift detection (v0.1.22)](https://github.com/yunaremaia/driftcheck/pull/14) |
| 2026-09-06 | [Sekelenao/Flinkboot](https://github.com/Sekelenao/Flinkboot) | [fix(core): lazy-init ValidatorFactory after capacity validation](https://github.com/Sekelenao/Flinkboot/pull/106) |
| 2026-09-06 | [oras-project/oras](https://github.com/oras-project/oras) | [fix(ci): resolve licenserc go.mod path relative to config directory](https://github.com/oras-project/oras/pull/2155) |
| 2026-09-06 | [rancher/dashboard](https://github.com/rancher/dashboard) | [fix: support IPv6 CIDR in isValidCIDR validator](https://github.com/rancher/dashboard/pull/19043) |
| 2026-09-06 | [yunaremaia/skills](https://github.com/yunaremaia/skills) | [docs: fix one-skill install command and name prerequisites for delegating skills](https://github.com/yunaremaia/skills/pull/2) |
| 2026-09-05 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [feat: add GitHub Actions version drift auto-fix (v0.1.20)](https://github.com/yunaremaia/driftcheck/pull/13) |
| 2026-09-05 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [feat(detector): add CI OS drift detection (v0.1.19)](https://github.com/yunaremaia/driftcheck/pull/12) |
| 2026-09-05 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [feat(detector): add Dependabot drift detection (v0.1.18)](https://github.com/yunaremaia/driftcheck/pull/11) |
| 2026-09-05 | [yunaremaia/driftcheck](https://github.com/yunaremaia/driftcheck) | [feat(detector): add Docker Compose drift detection (v0.1.17)](https://github.com/yunaremaia/driftcheck/pull/10) |
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
