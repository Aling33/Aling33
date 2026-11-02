# Upstream Pull Requests

**65** PRs across **28** upstream projects, **25** merged.

<details><summary><b>bytedance/deer-flow</b> — 11 PR / 9 merged</summary>

- `2026-10-26` [#7533](https://github.com/bytedance/deer-flow/pull/7533) fix(utils): replace read-only capture destinations atomically — 🟡 open
- `2026-10-25` [#7499](https://github.com/bytedance/deer-flow/pull/7499) fix(projects): delete read-only documents when purging trash — ✅ merged
- `2026-10-24` [#7446](https://github.com/bytedance/deer-flow/pull/7446) fix(config): delete read-only thread directories on Windows — ✅ merged
- `2026-10-24` [#7434](https://github.com/bytedance/deer-flow/pull/7434) fix(runtime): delete read-only JSONL runs and republish their watermark — 🟡 open
- `2026-10-23` [#7377](https://github.com/bytedance/deer-flow/pull/7377) fix(artifacts): keep sandbox paths inside CJK corner brackets whole — ✅ merged
- `2026-10-22` [#7289](https://github.com/bytedance/deer-flow/pull/7289) fix(scripts): reject a non-file --out path in dev_multi_instance — ✅ merged
- `2026-10-22` [#7290](https://github.com/bytedance/deer-flow/pull/7290) fix(sandbox): treat a fetched process substitution as an interpreter program — ✅ merged
- `2026-10-22` [#7256](https://github.com/bytedance/deer-flow/pull/7256) fix(scripts): reject a directory passed to support_bundle --out — ✅ merged
- `2026-10-21` [#7247](https://github.com/bytedance/deer-flow/pull/7247) fix(sandbox): treat the . builtin as a source execution context — ✅ merged
- `2026-10-21` [#7246](https://github.com/bytedance/deer-flow/pull/7246) test(config): skip the config-upgrade cases that need Git Bash — ✅ merged
- `2026-10-20` [#7214](https://github.com/bytedance/deer-flow/pull/7214) fix(scripts): find Git Bash under a PortableGit mingw64 layout — ✅ merged

</details>

<details><summary><b>DeepGym/deepgym</b> — 5 PR / 3 merged</summary>

- `2026-10-13` [#69](https://github.com/DeepGym/deepgym/pull/69) feat: import 16 OSWorld LibreOffice tasks as computer-use environments — ✅ merged
- `2026-10-13` [#63](https://github.com/DeepGym/deepgym/pull/63) fix(bigcodebench): an empty test suite scores 0, not 1.0 — ✅ merged
- `2026-10-12` [#36](https://github.com/DeepGym/deepgym/pull/36) fix(bigcodebench): read the score over a private fd, not the solution's stdout — ⚪ closed
- `2026-10-12` [#37](https://github.com/DeepGym/deepgym/pull/37) test: do-nothing solution must score below 1.0; fix POSIX-only local runs — ⚪ closed
- `2026-10-12` [#35](https://github.com/DeepGym/deepgym/pull/35) ci: lint the tests directory with ruff and fix existing violations — ✅ merged

</details>

<details><summary><b>Tencent/WeKnora</b> — 4 PR / 3 merged</summary>

- `2026-11-02` [#5024](https://github.com/Tencent/WeKnora/pull/5024) fix(knowledge): keep a reparse searchable until its worker replaces the content — 🟡 open
- `2026-11-01` [#4989](https://github.com/Tencent/WeKnora/pull/4989) fix(client): recover deepseek-flash DSML calls with doubled bars — ✅ merged
- `2026-11-01` [#4992](https://github.com/Tencent/WeKnora/pull/4992) fix(client): bound successful response bodies in the SDK — ✅ merged
- `2026-10-30` [#4929](https://github.com/Tencent/WeKnora/pull/4929) fix(audit): widen audit_logs.actor_user_id to fit embed and MCP actors — ✅ merged

</details>

<details><summary><b>ZHangZHengEric/Sage</b> — 2 PR / 2 merged</summary>

- `2026-10-13` [#300](https://github.com/ZHangZHengEric/Sage/pull/300) feat(model): add OrcaRouter OpenAI-compatible provider preset — ✅ merged
- `2026-10-11` [#296](https://github.com/ZHangZHengEric/Sage/pull/296) test(mcp): cover catalog validation boundaries — ✅ merged

</details>

<details><summary><b>QwenLM/qwen-code</b> — 8 PR / 1 merged</summary>

- `2026-10-24` [#15440](https://github.com/QwenLM/qwen-code/pull/15440) fix(managed-agent): join a child's answer the way its journal does — 🟡 open
- `2026-10-21` [#15034](https://github.com/QwenLM/qwen-code/pull/15034) fix(scripts): run the workspace clean scripts on Windows — 🟡 open
- `2026-10-21` [#15045](https://github.com/QwenLM/qwen-code/pull/15045) fix(cli): exit 1 when an extension update fails — 🟡 open
- `2026-10-21` [#15037](https://github.com/QwenLM/qwen-code/pull/15037) fix(cli): fail closed when the extension consent prompt has no stdin — 🟡 open
- `2026-10-21` [#15044](https://github.com/QwenLM/qwen-code/pull/15044) fix(cli): refuse the marketplace plugin picker without a terminal — 🟡 open
- `2026-10-20` [#14952](https://github.com/QwenLM/qwen-code/pull/14952) fix(core): let the file crawler use the bundled ripgrep — 🟡 open
- `2026-10-20` [#14951](https://github.com/QwenLM/qwen-code/pull/14951) fix(docs-site): run the documented local preview on Windows cmd — 🟡 open
- `2026-10-20` [#14910](https://github.com/QwenLM/qwen-code/pull/14910) ci(sdk-java): preserve failure reports and SQL causes — ✅ merged

</details>

<details><summary><b>langgenius/dify</b> — 4 PR / 1 merged</summary>

- `2026-11-02` [#45297](https://github.com/langgenius/dify/pull/45297) fix(dify-agent): deduplicate plugin tool JSON output by content, not formatting — ✅ merged
- `2026-11-02` [#45300](https://github.com/langgenius/dify/pull/45300) fix(dify-agent): record the in-flight request usage when a run is cancelled — 🟡 open
- `2026-11-02` [#45278](https://github.com/langgenius/dify/pull/45278) fix(dify-agent): request the internal files URL for plugin file parameters — 🟡 open
- `2026-10-31` [#45209](https://github.com/langgenius/dify/pull/45209) fix(dify-agent): validate plugin-declared blob size before allocating chunk buffer — 🟡 open

</details>

<details><summary><b>1Panel-dev/MaxKB</b> — 1 PR / 1 merged</summary>

- `2026-10-18` [#7368](https://github.com/1Panel-dev/MaxKB/pull/7368) fix(reranker): 修正直接回答分段列表 — ✅ merged

</details>

<details><summary><b>comet-ml/opik</b> — 1 PR / 1 merged</summary>

- `2026-10-18` [#9011](https://github.com/comet-ml/opik/pull/9011) [issue-9010] [SDK] fix: keep tool calls in Nova invoke_model streaming traces — ✅ merged

</details>

<details><summary><b>Eigenwise/atomic-agents</b> — 1 PR / 1 merged</summary>

- `2026-10-18` [#313](https://github.com/Eigenwise/atomic-agents/pull/313) fix(mcp): preserve mapping schema values and validation — ✅ merged

</details>

<details><summary><b>opensandbox-group/OpenSandbox</b> — 1 PR / 1 merged</summary>

- `2026-10-18` [#2283](https://github.com/opensandbox-group/OpenSandbox/pull/2283) fix(sdk-python): forward credential proxy settings through sandbox pools — ✅ merged

</details>

<details><summary><b>qdrant/fastembed</b> — 1 PR / 1 merged</summary>

- `2026-10-17` [#828](https://github.com/qdrant/fastembed/pull/828) fix: compute weighted static pooling in float32 for float16 tables — ✅ merged

</details>

<details><summary><b>The-PR-Agent/pr-agent</b> — 1 PR / 1 merged</summary>

- `2026-10-17` [#4152](https://github.com/The-PR-Agent/pr-agent/pull/4152) fix(plain-diff): decode Git-quoted file paths — ✅ merged

</details>

<details><summary><b>deepseek-ai/DeepInfer</b> — 9 PR / 0 merged</summary>

- `2026-10-21` [#189](https://github.com/deepseek-ai/DeepInfer/pull/189) eval: recognise markdown-emphasised GPQA answer lines — 🟡 open
- `2026-10-20` [#114](https://github.com/deepseek-ai/DeepInfer/pull/114) tests: lock the anyres image geometry — 🟡 open
- `2026-10-20` [#56](https://github.com/deepseek-ai/DeepInfer/pull/56) deep_cluster: reject visible-device assignments past the last GPU — 🟡 open
- `2026-10-20` [#113](https://github.com/deepseek-ai/DeepInfer/pull/113) fix(eval): preserve negative signs in AIME answer extraction — 🟡 open
- `2026-10-20` [#112](https://github.com/deepseek-ai/DeepInfer/pull/112) fix: validate Pareto sweep configurations before deduplication — 🟡 open
- `2026-10-20` [#103](https://github.com/deepseek-ai/DeepInfer/pull/103) fix: validate stale handles before freeing shared-pool blocks — 🟡 open
- `2026-10-20` [#90](https://github.com/deepseek-ai/DeepInfer/pull/90) fix(eval): weight tasks equally in per-modality Pass@1 — 🟡 open
- `2026-10-20` [#72](https://github.com/deepseek-ai/DeepInfer/pull/72) fix(eval): avoid stale HLE images when task IDs are reused — 🟡 open
- `2026-10-20` [#61](https://github.com/deepseek-ai/DeepInfer/pull/61) eval: classify rollouts by the finish reasons the engine returns — 🟡 open

</details>

<details><summary><b>czlonkowski/n8n-mcp</b> — 2 PR / 0 merged</summary>

- `2026-10-19` [#1165](https://github.com/czlonkowski/n8n-mcp/pull/1165) fix(validation): accept n8n expressions in numeric and boolean properties — 🟡 open
- `2026-10-18` [#1163](https://github.com/czlonkowski/n8n-mcp/pull/1163) fix(validation): accept n8n expressions in numeric and boolean properties — ⚪ closed

</details>

<details><summary><b>charmbracelet/crush</b> — 1 PR / 0 merged</summary>

- `2026-10-18` [#4094](https://github.com/charmbracelet/crush/pull/4094) fix(download): 网络读取失败时保留目标文件 — 🟡 open

</details>

<details><summary><b>coleam00/Archon</b> — 1 PR / 0 merged</summary>

- `2026-10-17` [#4439](https://github.com/coleam00/Archon/pull/4439) fix(core): reject case-insensitive project rename collisions — ⚪ closed

</details>

<details><summary><b>confident-ai/deepeval</b> — 1 PR / 0 merged</summary>

- `2026-10-17` [#3479](https://github.com/confident-ai/deepeval/pull/3479) fix(agent_loop_detection): hash full inputs to avoid false cycle detection — 🟡 open

</details>

<details><summary><b>getpaseo/paseo</b> — 1 PR / 0 merged</summary>

- `2026-10-18` [#7340](https://github.com/getpaseo/paseo/pull/7340) fix(server): 正确编码 MCP 终端按键 — ⚪ closed

</details>

<details><summary><b>go-git/go-git</b> — 1 PR / 0 merged</summary>

- `2026-10-13` [#2523](https://github.com/go-git/go-git/pull/2523) plumbing: transport, Send server shallow boundary in v2 fetch — 🟡 open

</details>

<details><summary><b>livekit/agents</b> — 1 PR / 0 merged</summary>

- `2026-10-13` [#7791](https://github.com/livekit/agents/pull/7791) fix(silero): prefer CUDA when TensorRT is unavailable — 🟡 open

</details>

<details><summary><b>mastra-ai/mastra</b> — 1 PR / 0 merged</summary>

- `2026-10-13` [#26863](https://github.com/mastra-ai/mastra/pull/26863) fix(core): stop repeating text-only responses with unmarked finish reasons — ⚪ closed

</details>

<details><summary><b>mattpocock/sandcastle</b> — 1 PR / 0 merged</summary>

- `2026-10-18` [#1047](https://github.com/mattpocock/sandcastle/pull/1047) fix(orchestrator): ignore output after agent invocation settles — ⚪ closed

</details>

<details><summary><b>meta/pyrefly</b> — 1 PR / 0 merged</summary>

- `2026-10-13` [#5225](https://github.com/meta/pyrefly/pull/5225) feat(typecheck): report abstract methods with implementations — 🟡 open

</details>

<details><summary><b>NousResearch/hermes-agent</b> — 1 PR / 0 merged</summary>

- `2026-10-25` [#144617](https://github.com/NousResearch/hermes-agent/pull/144617) fix(approval): fold every spelling of HERMES_HOME before gating config.yaml edits — 🟡 open

</details>

<details><summary><b>openclaw/openclaw</b> — 1 PR / 0 merged</summary>

- `2026-10-25` [#183782](https://github.com/openclaw/openclaw/pull/183782) docs: note that Go before 1.27 ignores the egress proxy CA bundle on macOS — 🟡 open

</details>

<details><summary><b>pipecat-ai/pipecat</b> — 1 PR / 0 merged</summary>

- `2026-10-18` [#6228](https://github.com/pipecat-ai/pipecat/pull/6228) fix(tts): 保留流式重采样的完整音频 — 🟡 open

</details>

<details><summary><b>run-llama/llama_index</b> — 1 PR / 0 merged</summary>

- `2026-10-13` [#23490](https://github.com/run-llama/llama_index/pull/23490) fix(core): avoid mutating retriever results during fusion — 🟡 open

</details>

<details><summary><b>TencentCloud/Octop</b> — 1 PR / 0 merged</summary>

- `2026-10-14` [#2042](https://github.com/TencentCloud/Octop/pull/2042) fix(dashboard): stop autofilling provider model field — 🟡 open

</details>
