<h1 align="center">🤖 CountAgent</h1>

<p align="center">
  <strong>A lightweight personal AI assistant framework</strong><br>
  30+ LLM providers &middot; 14+ chat channels &middot; 16+ built-in tools
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-%E2%89%A53.11-blue?logo=python&logoColor=white" alt="Python ≥3.11">
  <img src="https://img.shields.io/badge/version-0.1.0-orange" alt="v0.1.0">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
  <img src="https://img.shields.io/badge/status-Alpha-yellow" alt="Alpha">
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> &middot;
  <a href="#-cli-commands">CLI</a> &middot;
  <a href="#-supported-llm-providers">Providers</a> &middot;
  <a href="#-supported-channels">Channels</a> &middot;
  <a href="#-built-in-tools">Tools</a>
</p>

---

<p align="center">
  <strong>English</strong> &nbsp;|&nbsp;
  <a href="#-中文文档"><strong>中文</strong></a>
</p>

---

## ✨ Features

- **Multi-Provider** — 30+ LLM providers: Anthropic, OpenAI, DeepSeek, Gemini, Bedrock, Azure, and more
- **Omnichannel** — 14+ chat platforms: Telegram, Discord, Slack, WeChat, WeCom, DingTalk, Feishu, QQ, and more
- **Rich Toolset** — 16+ built-in tools: filesystem, shell, web search/fetch, cron, sub-agent spawning, and more
- **MCP Protocol** — Dynamically extend capabilities via Model Context Protocol
- **Skills System** — Markdown-based extensible skills with YAML frontmatter
- **Memory System** — Three-tier memory: MemoryStore (file I/O), Consolidator (compression), Dream (scheduled consolidation)
- **Session Management** — Unified or per-channel sessions with auto-compaction
- **Gateway Mode** — Run all channels in a single process with built-in heartbeat and cron scheduling

## 🚀 Quick Start

```bash
# Install (with dev dependencies)
pip install -e ".[dev]"

# First-time setup (interactive wizard)
countagent onboard --wizard

# Or create a default config
countagent onboard
```

Edit the config to add your API key:

```bash
# Config location
# Linux/macOS: ~/.countagent/config.json
# Windows:     %USERPROFILE%\.countagent\config.json
```

```bash
# Start chatting
countagent agent

# Send a single message
countagent agent -m "Hello!"

# Start the gateway (connects all chat channels)
countagent gateway
```

## 💻 CLI Commands

| Command | Description |
|---------|-------------|
| `countagent --help` | Show help |
| `countagent --version` | Show version |
| `countagent onboard` | Initialize config and workspace |
| `countagent onboard --wizard` | Interactive setup wizard |
| `countagent agent` | Start interactive chat |
| `countagent agent -m "msg"` | Send a single message |
| `countagent gateway` | Start gateway (all channels) |
| `countagent serve` | Start OpenAI-compatible API server |
| `countagent status` | Show runtime status |
| `countagent channels status` | Show channel status |
| `countagent channels login <n>` | Authenticate a channel |
| `countagent provider login <n>` | OAuth login for a provider |
| `countagent plugins list` | List discovered channel plugins |

## 📁 Architecture

```
countagent/
├── channels/         # Chat channel integrations (Telegram, Discord, WeChat, etc.)
├── commands/         # Command routing & built-in commands
├── core/             # Core abstractions (event bus, interfaces, hooks)
├── engine/           # Agent engine (loop, context builder, sub-agents)
├── infra/            # Infrastructure (CLI, config, scheduling, sessions, API server)
├── memory/           # Memory system (MemoryStore, Consolidator, Dream)
├── providers/        # LLM provider adapters
├── resources/        # Templates, skills, static assets
│   ├── skills/       # Built-in skills (github, weather, summarize, etc.)
│   └── templates/    # Prompt templates
├── tools/            # Built-in tools (filesystem, shell, search, web, etc.)
└── utils/            # Utility functions
```

## 🌐 Supported LLM Providers

### ☁️ Cloud

| Provider | Backend |
|----------|---------|
| Anthropic | Native SDK |
| OpenAI | OpenAI SDK |
| DeepSeek | OpenAI-compat |
| Gemini (Google) | OpenAI-compat |
| Mistral | OpenAI-compat |
| Groq | OpenAI-compat |
| Zhipu AI | OpenAI-compat |
| DashScope (Qwen) | OpenAI-compat |
| Moonshot | OpenAI-compat |
| MiniMax | OpenAI-compat |
| Step Fun | OpenAI-compat |
| Xiaomi MIMO | OpenAI-compat |
| LongCat | OpenAI-compat |
| Qianfan | OpenAI-compat |

### 🚪 Gateways

| Gateway | Description |
|---------|-------------|
| OpenRouter | Global model gateway |
| Hugging Face | HF Inference Providers |
| AiHubMix | OpenAI-compat gateway |
| SiliconFlow | Chinese model gateway |
| VolcEngine | ByteDance cloud |
| BytePlus | VolcEngine international |

### 🏠 Local

| Provider | Description |
|----------|-------------|
| Ollama | Local model runtime |
| vLLM | High-performance inference |
| LM Studio | Local model runtime |
| OpenVINO Model Server | Intel inference |

### 🏢 Enterprise

| Provider | Description |
|----------|-------------|
| Azure OpenAI | Azure-hosted OpenAI |
| AWS Bedrock | AWS-managed models |
| OpenAI Codex | OAuth-based |
| GitHub Copilot | OAuth device flow |

## 📱 Supported Channels

| Channel | Optional Deps |
|---------|---------------|
| Telegram | Built-in |
| Discord | `discord` |
| Slack | Built-in |
| WhatsApp | Built-in (requires Bridge) |
| WeChat | `weixin` |
| WeCom | `wecom` |
| DingTalk | Built-in |
| Feishu | Built-in |
| QQ | Built-in |
| Microsoft Teams | `msteams` |
| Matrix | `matrix` |
| Email | Built-in |
| WebSocket | Built-in |
| Mochat | Built-in |

## 🔧 Built-in Tools

| Tool | Description |
|------|-------------|
| `read_file` | Read file contents |
| `write_file` | Write to files |
| `edit_file` | Precise file editing (search & replace) |
| `list_dir` | List directory contents |
| `exec` | Execute shell commands |
| `glob` | Filename pattern search |
| `grep` | File content search |
| `web_search` | Search the web |
| `web_fetch` | Fetch and extract web page content |
| `cron` | Schedule recurring tasks |
| `message` | Send messages to channels |
| `ask_user` | Ask user a question and wait for reply |
| `spawn` | Spawn a sub-agent |
| `notebook_edit` | Edit Jupyter notebooks |
| `my` | Agent runtime self-inspection |
| `mcp_*` | Dynamic tools from MCP servers |

## ⚙️ Configuration

Config lives at `~/.countagent/config.json`. Environment variables with prefix `COUNTAGENT_*` override config values.

```bash
# Environment variable examples
export COUNTAGENT_PROVIDERS__ANTHROPIC__API_KEY="sk-..."
export COUNTAGENT_AGENTS__DEFAULTS__MODEL="anthropic/claude-sonnet-4"
```

> See the `docs/` directory for detailed configuration reference.

## 🔌 MCP Support

Extend CountAgent's toolset dynamically via the Model Context Protocol (MCP).

```json
{
  "tools": {
    "mcp_servers": {
      "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"]
      }
    }
  }
}
```

Supports **stdio** and **HTTP (SSE / Streamable HTTP)** transports.

## 🧠 Skills System

Skills are markdown-based extensible instruction sets with YAML frontmatter.

Built-in skills include: GitHub CLI, weather, summarize, tmux control, skill creator, ClawHub marketplace, and more.

```
workspace/skills/my-skill/
└── SKILL.md
```

```yaml
---
name: my-skill
description: Describe what this skill does
metadata:
  countagent:
    requires:
      bins: ["my-cli"]
---

# Skill Instructions

Tell the agent how to use this skill...
```

## 💾 Memory System

Three-tier memory architecture keeps context persistent yet efficient:

- **MemoryStore** — Pure file I/O layer managing `MEMORY.md`, `history.jsonl`, `SOUL.md`, and `USER.md`
- **Consolidator** — Lightweight token-budget-triggered compression that archives old messages into `history.jsonl`
- **Dream** — Heavyweight scheduled consolidation that analyzes conversation history and updates long-term memory files

## 🛠️ Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=countagent

# Lint
ruff check .
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📖 中文文档

<p align="center">
  <a href="#-features"><strong>English</strong></a> &nbsp;|&nbsp;
  <strong>中文</strong>
</p>

### ✨ 功能亮点

- **多模型支持** — 30+ 大模型供应商：Anthropic、OpenAI、DeepSeek、Gemini、Bedrock、Azure 等
- **全渠道覆盖** — 14+ 聊天平台：Telegram、Discord、Slack、微信、企业微信、钉钉、飞书、QQ 等
- **丰富的工具** — 16+ 内置工具：文件系统、Shell 执行、Web 搜索/抓取、定时任务、子代理等
- **MCP 协议** — 通过标准 Model Context Protocol 动态扩展工具能力
- **技能系统** — 基于 Markdown 的可扩展技能，支持 YAML 前置元数据
- **记忆系统** — 三层记忆架构：MemoryStore（文件 I/O）、Consolidator（压缩）、Dream（定时整合）
- **会话管理** — 跨渠道统一会话或独立会话，自动压缩
- **网关模式** — 单进程运行所有渠道，内置心跳和定时任务调度

### 🚀 快速开始

```bash
# 安装（含开发依赖）
pip install -e ".[dev]"

# 首次初始化（交互式配置向导）
countagent onboard --wizard

# 或者直接创建默认配置
countagent onboard
```

编辑配置文件添加 API 密钥：

```bash
# 配置文件位置
# Linux/macOS: ~/.countagent/config.json
# Windows:     %USERPROFILE%\.countagent\config.json
```

```bash
# 开始对话
countagent agent

# 发送单条消息
countagent agent -m "你好！"

# 启动网关（连接所有聊天渠道）
countagent gateway
```

### 💻 CLI 命令

| 命令 | 说明 |
|------|------|
| `countagent --help` | 显示帮助信息 |
| `countagent --version` | 显示版本号 |
| `countagent onboard` | 初始化配置和工作空间 |
| `countagent onboard --wizard` | 交互式配置向导 |
| `countagent agent` | 进入交互式聊天 |
| `countagent agent -m "消息"` | 发送单条消息 |
| `countagent gateway` | 启动网关服务（所有渠道） |
| `countagent serve` | 启动 OpenAI 兼容 API 服务器 |
| `countagent status` | 显示运行状态 |
| `countagent channels status` | 显示渠道状态 |
| `countagent channels login <name>` | 登录渠道（如微信、WhatsApp） |
| `countagent provider login <name>` | OAuth 登录供应商 |
| `countagent plugins list` | 列出所有已发现的渠道插件 |

### 📁 项目架构

```
countagent/
├── channels/         # 聊天渠道集成（Telegram、Discord、微信等）
├── commands/         # 命令路由与内置指令
├── core/             # 核心抽象（事件总线、接口、钩子）
├── engine/           # 代理引擎（循环、上下文构建、子代理）
├── infra/            # 基础设施（CLI、配置、调度、会话、API 服务器）
├── memory/           # 记忆系统（MemoryStore、Consolidator、Dream）
├── providers/        # LLM 供应商适配器
├── resources/        # 模板、技能、静态资源
│   ├── skills/       # 内置技能（github、weather、summarize 等）
│   └── templates/    # Prompt 模板
├── tools/            # 内置工具（文件、Shell、搜索、Web 等）
└── utils/            # 辅助工具函数
```

### 🌐 支持的 LLM 供应商

#### ☁️ 云服务

| 供应商 | 后端 |
|--------|------|
| Anthropic | 原生 SDK |
| OpenAI | OpenAI SDK |
| DeepSeek | OpenAI 兼容 |
| Gemini (Google) | OpenAI 兼容 |
| Mistral | OpenAI 兼容 |
| Groq | OpenAI 兼容 |
| 智谱 AI (Zhipu) | OpenAI 兼容 |
| 通义千问 (DashScope) | OpenAI 兼容 |
| Moonshot (月之暗面) | OpenAI 兼容 |
| MiniMax | OpenAI 兼容 |
| 阶跃星辰 (Step Fun) | OpenAI 兼容 |
| 小米 MIMO | OpenAI 兼容 |
| LongCat | OpenAI 兼容 |
| 百度千帆 (Qianfan) | OpenAI 兼容 |

#### 🚪 网关

| 网关 | 说明 |
|------|------|
| OpenRouter | 全球模型网关 |
| Hugging Face | HF 推理服务 |
| AiHubMix | OpenAI 兼容网关 |
| 硅基流动 (SiliconFlow) | 国内模型网关 |
| 火山引擎 (VolcEngine) | 字节跳动云服务 |
| BytePlus | 火山引擎国际版 |

#### 🏠 本地部署

| 供应商 | 说明 |
|--------|------|
| Ollama | 本地模型运行 |
| vLLM | 高性能推理服务 |
| LM Studio | 本地模型运行 |
| OpenVINO Model Server | Intel 推理服务 |

#### 🏢 企业

| 供应商 | 说明 |
|--------|------|
| Azure OpenAI | Azure 托管的 OpenAI |
| AWS Bedrock | AWS 托管的多模型 |
| OpenAI Codex | OAuth 认证 |
| GitHub Copilot | OAuth 设备流 |

### 📱 支持的聊天渠道

| 渠道 | 可选依赖 |
|------|----------|
| Telegram | 内置 |
| Discord | `discord` |
| Slack | 内置 |
| WhatsApp | 内置（需 Bridge） |
| 微信 (WeChat) | `weixin` |
| 企业微信 (WeCom) | `wecom` |
| 钉钉 (DingTalk) | 内置 |
| 飞书 (Feishu) | 内置 |
| QQ | 内置 |
| Microsoft Teams | `msteams` |
| Matrix | `matrix` |
| Email | 内置 |
| WebSocket | 内置 |
| Mochat | 内置 |

### 🔧 内置工具

| 工具 | 说明 |
|------|------|
| `read_file` | 读取文件内容 |
| `write_file` | 写入文件 |
| `edit_file` | 精确编辑文件（搜索替换） |
| `list_dir` | 列出目录内容 |
| `exec` | 执行 Shell 命令 |
| `glob` | 文件名模式匹配搜索 |
| `grep` | 文件内容搜索 |
| `web_search` | 网页搜索 |
| `web_fetch` | 抓取网页内容 |
| `cron` | 定时任务管理 |
| `message` | 向渠道发送消息 |
| `ask_user` | 向用户提问并等待回复 |
| `spawn` | 启动子代理 |
| `notebook_edit` | 编辑 Jupyter 笔记本 |
| `my` | 代理运行时状态自检 |
| `mcp_*` | MCP 服务器提供的动态工具 |

### ⚙️ 配置

配置文件位于 `~/.countagent/config.json`，支持通过环境变量覆盖（前缀 `COUNTAGENT_*`）。

```bash
# 环境变量示例
export COUNTAGENT_PROVIDERS__ANTHROPIC__API_KEY="sk-..."
export COUNTAGENT_AGENTS__DEFAULTS__MODEL="anthropic/claude-sonnet-4"
```

> 详细配置文档请参考项目 `docs/` 目录。

### 🔌 MCP 支持

CountAgent 通过标准 Model Context Protocol (MCP) 动态扩展工具能力。

```json
{
  "tools": {
    "mcp_servers": {
      "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"]
      }
    }
  }
}
```

支持 **stdio** 和 **HTTP (SSE / Streamable HTTP)** 连接方式。

### 🧠 技能系统

技能是基于 Markdown 的可扩展指令集，使用 YAML 前置元数据描述。

内置技能包括：GitHub CLI、天气查询、内容摘要、tmux 控制、技能创建器、ClawHub 技能市场等。

```
workspace/skills/my-skill/
└── SKILL.md
```

```yaml
---
name: my-skill
description: 描述这个技能做什么
metadata:
  countagent:
    requires:
      bins: ["my-cli"]
---

# 技能指令

告诉代理如何使用这个技能...
```

### 💾 记忆系统

三层记忆架构确保上下文持久且高效：

- **MemoryStore** — 纯文件 I/O 层，管理 `MEMORY.md`、`history.jsonl`、`SOUL.md`、`USER.md`
- **Consolidator** — 轻量级 Token 预算触发自动压缩，将旧消息摘要后归档到 `history.jsonl`
- **Dream** — 重量级定时记忆整合，分析对话历史并更新长期记忆文件

### 🛠️ 开发

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 带 Coverage
pytest --cov=countagent

# 代码检查
ruff check .
```

### 📄 许可证

本项目基于 [MIT 许可证](LICENSE) 开源。
