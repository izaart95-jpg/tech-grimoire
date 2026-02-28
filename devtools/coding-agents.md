# AI Coding Agents & Assistants

AI-powered coding agents, assistants, and intelligent IDEs. These tools go beyond simple code completion — they can autonomously edit files, run commands, generate tests, refactor entire codebases, and act as pair-programming partners. This document covers standalone IDEs, CLI agents, VS Code extensions, and specialized coding tools.

---

## Table of Contents
1. [Cursor](#1-cursor)
2. [Claude Code](#2-claude-code)
3. [Claude Code Router](#3-claude-code-router)
4. [OpenAI Codex](#4-openai-codex)
5. [Kilo Code](#5-kilo-code)
6. [Cline](#6-cline)
7. [BlackboxAI](#7-blackboxai)
8. [Roo Code](#8-roo-code-discontinued)
9. [OpenCode](#9-opencode)
10. [Shitty Coding Agent](#10-shitty-coding-agent)
11. [Copilot Arena](#11-copilot-arena)
12. [Void Editor](#12-void-editor-deprecated)
13. [Kiro](#13-kiro)
14. [Builder.io Fusion](#14-builderio-fusion)
15. [Trae AI](#15-trae-ai)
16. [Windsurf](#16-windsurf)
17. [Qodo AI](#17-qodo-ai)
18. [Zencoder](#18-zencoder)
19. [ShuttleAI](#19-shuttleai)
20. [OpenClaw / ZeroClaw](#20-openclaw--zeroclaw)
21. [Comparison Table](#21-comparison-table)
22. [Which Should You Use?](#22-which-should-you-use)

---

## 1. Cursor

- **Website:** https://cursor.com
- **What it is:** An AI-first code editor built as a fork of VS Code. Cursor deeply integrates AI into every part of the editing experience — from intelligent tab completions to multi-file agentic editing powered by frontier models.

**Key Features:**
- **Tab Completion** — context-aware autocomplete that predicts multi-line edits
- **Chat** — inline AI chat for asking questions about your codebase
- **Composer** — agentic multi-file editing with natural language instructions
- **Cmd+K** — inline code generation and editing
- **Codebase indexing** — AI understands your entire project
- **Multi-model support** — GPT-4o, Claude, and custom models
- **VS Code extension compatibility** — most VS Code extensions work

**Install:**
```bash
# Download from https://cursor.com
# Available for macOS, Linux, and Windows
# Supports existing VS Code settings and extensions
```

**Pricing:**
- **Free:** $0 — limited agent and chat requests
- **Plus:** $8/month (base usage, Cursor's own models only)
- **Premium:** $30/month (4x Plus usage, cloud agents, third-party models)
- **Super:** $100/month (15x Plus, priority model access)
- **Ultra:** $200/month (50x Plus, earliest access to new models)
- **Teams:** $30+/user/month (seat tiers, SSO, admin controls)

> Legacy Hobby/Start/Pro/Pro+/Ultra plans still work for existing subscribers.

---

## 2. Claude Code

- **Website:** https://platform.claude.com/docs/en/docs/claude-code
- **What it is:** Anthropic's official CLI-based agentic coding tool. Claude Code runs in your terminal and can understand your codebase, edit files, run shell commands, manage git workflows, and execute multi-step tasks autonomously.

**Key Features:**
- **Terminal-native** — works in any terminal, no IDE required
- **Agentic coding** — autonomously plans and executes multi-step tasks
- **File editing** — reads, creates, and modifies files directly
- **Shell command execution** — runs tests, builds, linting, and more
- **Git integration** — commits, creates PRs, resolves merge conflicts
- **Large context** — understands entire codebases via indexing
- **Extended thinking** — step-by-step reasoning for complex tasks
- **Sub-agents** — spawns focused agents for parallel tasks

**Install:**
```bash
npm install -g @anthropic-ai/claude-code

# Requires an Anthropic API key
export ANTHROPIC_API_KEY="your-key"

# Run in any project directory
cd your-project
claude
```

**Pricing:**
- The tool itself is free; you pay for Anthropic API usage
- Works with Claude Pro/Max subscriptions or API credits
- **Max plan:** $100/month or $200/month for heavy usage

---

## 3. Claude Code Router

- **Website:** https://github.com/musistudio/claude-code-router
- **What it is:** A proxy server that intercepts Claude Code API requests and routes them to cheaper or alternative LLM providers. Dramatically reduces costs by using less expensive models for simpler tasks while reserving premium models for complex reasoning.

**Key Features:**
- **Cost reduction** — route simple tasks to cheaper models (e.g., Haiku, GPT-4o-mini)
- **Model routing** — configurable rules for which model handles which task type
- **Drop-in replacement** — works transparently with Claude Code
- **Multiple provider support** — OpenAI, Anthropic, OpenRouter, local models

**Install:**
```bash
git clone https://github.com/musistudio/claude-code-router.git
cd claude-code-router
npm install
npm start

# Configure Claude Code to use the router as its API endpoint
```

**Pricing:** Free and open-source (you pay for the underlying API providers)

---

## 4. OpenAI Codex

- **Website:** https://openai.com/index/introducing-codex/
- **What it is:** OpenAI's cloud-based coding agent that runs tasks autonomously in a sandboxed environment. It can read and write files, execute code, run tests, and produce complete implementations from natural language descriptions.

**Key Features:**
- **Cloud sandboxed execution** — each task runs in an isolated environment
- **Autonomous task completion** — reads your repo, writes code, runs tests
- **File read/write** — creates and modifies files across the project
- **Test execution** — runs your test suite and iterates until tests pass
- **Git-aware** — understands repository structure and history
- **Parallel tasks** — run multiple coding tasks simultaneously

**Usage:**
```
# Available through the OpenAI platform / ChatGPT interface
# Connect your GitHub repository
# Describe a task in natural language
# Codex clones, edits, tests, and produces a PR
```

**Pricing:**
- Included with ChatGPT Pro ($200/month) and Plus ($20/month, limited)
- API access billed per token

---

## 5. Kilo Code

- **Website:** https://kilocode.ai
- **What it is:** An open-source AI coding assistant that runs as a VS Code extension. Supports multiple AI providers and offers an autonomous mode for hands-free coding.

**Key Features:**
- **Multi-provider support** — Anthropic, OpenAI, Google, OpenRouter, local models
- **Autonomous mode** — let the AI complete tasks without manual approval steps
- **File editing** — creates and modifies files in your workspace
- **Terminal integration** — runs commands directly
- **Diff view** — review AI changes before applying
- **Context-aware** — indexes and understands your project

**Install:**
```
# Install from VS Code Marketplace
# Search "Kilo Code" in Extensions
# Or: code --install-extension kilocode.kilo-code
```

**Pricing:** Free and open-source (bring your own API keys)

---

## 6. Cline

- **Website:** https://github.com/cline/cline
- **What it is:** An open-source AI coding agent for VS Code (formerly known as "Claude Dev"). Cline can autonomously create and edit files, run terminal commands, use a browser, and complete complex software engineering tasks with human-in-the-loop approval.

**Key Features:**
- **Autonomous file editing** — creates, modifies, and deletes files
- **Terminal command execution** — runs build, test, and deploy commands
- **Browser integration** — can launch and interact with web applications
- **Multi-model support** — Claude, GPT-4o, Gemini, local models via Ollama
- **Human-in-the-loop** — approve each action or enable auto-approve
- **MCP support** — extensible via Model Context Protocol servers
- **Context mentions** — reference files, URLs, or problems inline

**Install:**
```
# Install from VS Code Marketplace
# Search "Cline" in Extensions
# Configure your API key (Anthropic, OpenAI, OpenRouter, etc.)
```

**Pricing:** Free and open-source (bring your own API keys)

---

## 7. BlackboxAI

- **Website:** https://www.blackbox.ai
- **What it is:** An AI-powered coding assistant offering code generation, chat, code search, and a web-based IDE. Available as a VS Code extension and a standalone web platform.

**Key Features:**
- **Code generation** — generate code from natural language prompts
- **AI chat** — ask coding questions with context from your project
- **Code search** — semantic search across open-source code
- **Web IDE** — browser-based development environment
- **Multi-language support** — code generation and search across many programming languages
- **Code completion** — inline autocomplete suggestions

**Install:**
```
# VS Code Extension
# Search "Blackbox AI" in the VS Code Marketplace

# Web IDE
# Visit https://www.blackbox.ai
```

**Pricing:**
- **Pro:** $10/month
- **Pro Plus:** $20/month
- **Pro Max:** $40/month
- **Enterprise:** Custom pricing

---

## 8. Roo Code (Discontinued)

- **Website:** https://github.com/RooCodeInc/Roo-Code
- **Status:** **Shut down on 15 May 2026.** The extension received its final release and the repository is archived and read-only; the team has moved on to Roomote.
- **What it is:** A fork of Cline with custom modes, improved multi-model support, and a polished VS Code experience. It is no longer maintained, so use it only if you already depend on it.

> **Alternatives:** Cline (where Roo Code originated) or ZooCode (the community-maintained fork).

**Key Features (historical):**
- **Custom modes** — define specialized AI personas (architect, reviewer, debugger)
- **Multi-model support** — use different models for different tasks
- **Enhanced diff view** — better change visualization
- **File editing** — autonomous file creation and modification
- **Terminal integration** — run commands within VS Code
- **MCP support** — extend with Model Context Protocol servers
- **Improved context management** — better memory and project understanding

**Install:**
```
# Install from VS Code Marketplace
# Search "Roo Code" in Extensions
```

**Pricing:** Free and open-source (bring your own API keys) — no longer maintained

---

## 9. OpenCode

- **Website:** https://opencode.ai
- **What it is:** A lightweight, terminal-based AI coding assistant that supports multiple LLM providers. Designed for developers who prefer working in the terminal over an IDE.

**Key Features:**
- **Terminal-native** — runs entirely in your terminal
- **Multi-provider support** — OpenAI, Anthropic, Google, OpenRouter, Ollama
- **Lightweight** — minimal resource usage compared to IDE-based tools
- **File operations** — read, write, and modify project files
- **Shell integration** — execute commands and review output
- **Session management** — save and resume conversations

**Install:**
```bash
# Install script (recommended)
curl -fsSL https://opencode.ai/install | bash

# Or via npm
npm install -g opencode-ai

# Or via Homebrew
brew install anomalyco/tap/opencode
# Configure with your preferred API provider
```

**Pricing:** Free and open-source (bring your own API keys)

> **Note:** OpenCode 2 is a separate major release with its own package (`@opencode/cli`, `opencode.ai/v2/install`). OpenCode 1 and 2 both install a binary called `opencode`, so they cannot coexist side by side.

---

## 10. Shitty Coding Agent

- **Website:** https://shittycodingagent.ai
- **What it is:** A humorous yet functional AI coding agent that takes a deliberately irreverent approach to automated code generation. Despite the name, it can autonomously generate working code, commit changes, and open pull requests.

**Key Features:**
- **Autonomous code generation** — generates code from issue descriptions
- **GitHub integration** — reads issues, writes code, opens PRs
- **Intentionally opinionated** — makes bold coding decisions
- **Fun factor** — entertaining commit messages and PR descriptions

**Usage:**
```
# Assign a GitHub issue to the agent
# It reads the issue, generates code, and opens a PR
# Review and merge (or laugh and close)
```

**Pricing:** Free / open-source

---

## 11. Copilot Arena

- **Website:** https://github.com/lmarena/copilot-arena
- **What it is:** A VS Code extension that performs blind side-by-side comparisons of AI coding assistants. It shows you completions from two different models simultaneously (anonymized) and lets you pick the better one, contributing to an open leaderboard.

**Key Features:**
- **Blind comparison** — see two completions without knowing which model generated them
- **Rate completions** — choose the better response to contribute to rankings
- **Multiple models** — compares completions from GPT-4o, Claude, Gemini, and others
- **Open leaderboard** — community-driven rankings of coding model quality
- **Seamless integration** — works like a normal code completion extension

**Install:**
```
# Install from VS Code Marketplace
# Search "Copilot Arena" in Extensions
```

**Pricing:** Free

---

## 12. Void Editor (Deprecated)

- **Website:** https://github.com/voideditor/void
- **Status:** **Deprecated and archived (2 June 2026).** The repository is read-only and the project no longer accepts contributions; the last shipped build predates current VS Code.
- **What it is:** An open-source AI code editor forked from VS Code, originally positioned as a privacy-focused alternative to Cursor. It remains a useful reference implementation for people forking VS Code, but it is not a maintained editor.

**Key Features:**
- **Open-source** — fully transparent codebase
- **Built-in AI** — code completion, chat, and editing without third-party extensions
- **Multi-provider** — supports various AI backends including local models
- **VS Code compatible** — familiar interface and extension support
- **Privacy-focused** — no telemetry, local-first design
- **Community-driven** — open development process

**Install:**
```bash
# Source is still available for reference / forking
git clone https://github.com/voideditor/void.git
```

For maintained alternatives with a similar direct-to-provider model, see VS Code's built-in BYOK, Cline, or Zed.

**Pricing:** Free and open-source (Apache-2.0) — archived

---

## 13. Kiro

- **Website:** https://kiro.dev
- **What it is:** An AI-powered IDE built by Amazon Web Services (AWS). Kiro focuses on spec-driven development, using structured specifications to guide AI code generation. It features hooks for automated workflows and steering rules for project-specific conventions.

**Key Features:**
- **Spec-driven development** — write specs, AI generates implementation
- **Hooks** — automated triggers that run on file save, commit, or other events
- **Steering rules** — project-level instructions that guide AI behavior
- **AWS integration** — deep integration with AWS services
- **Agentic coding** — autonomous multi-step task execution
- **Built on VS Code** — familiar interface with AI augmentation

**Install:**
```bash
# Download from https://kiro.dev
# Available for macOS, Linux, and Windows
```

**Pricing:**
- **Free tier** — 50 credits/month
- **Pro:** $20/user/month (1,000 credits)
- **Pro+:** $40/user/month (2,000 credits)
- **Pro Max:** $100/user/month (5,000 credits)
- **Power:** $200/user/month (10,000 credits)

---

## 14. Builder.io Fusion

- **Website:** https://www.builder.io/fusion
- **What it is:** A visual development platform powered by AI that bridges design and code. Fusion takes Figma designs and converts them to clean, production-ready code across multiple frameworks.

**Key Features:**
- **Figma-to-code** — import Figma designs and generate framework code
- **Visual editor** — drag-and-drop UI builder with AI assistance
- **Multi-framework output** — generates React, Vue, Svelte, Angular, and more
- **Responsive design** — AI handles responsive layouts automatically
- **Code export** — clean, maintainable output (not spaghetti)
- **CMS integration** — connect to Builder.io's headless CMS

**Usage:**
```
# 1. Connect your Figma project at builder.io/fusion
# 2. Select components or pages to convert
# 3. Choose target framework (React, Vue, etc.)
# 4. Export generated code to your project
```

**Pricing:**
- **Free:** $0 (up to 5 users, 60 monthly Agent Credits)
- **Pro:** $24/user/month (500 credits)
- **Team:** $40/user/month
- **Enterprise:** Custom pricing
- On-demand credits: $25 per 500

---

## 15. Trae AI

- **Website:** https://www.trae.ai
- **What it is:** An AI-powered IDE developed by ByteDance (the company behind TikTok). Trae offers a built-in AI assistant with chat, code generation, and an agentic Builder mode for multi-step tasks.

**Key Features:**
- **Built-in AI assistant** — no separate extension needed
- **Builder mode** — agentic multi-step task execution
- **AI chat** — ask questions with full codebase context
- **Code completion** — inline AI suggestions
- **Multi-model support** — Claude, GPT-4o models available
- **Free tier** — generous free access to AI features
- **VS Code compatible** — supports VS Code extensions

**Install:**
```bash
# Download from https://www.trae.ai
# Available for macOS, Linux, and Windows
```

**Pricing:**
- **Free:** Generous AI usage included at no cost
- **Pro plans** available for teams

---

## 16. Windsurf

- **Website:** https://windsurf.com
- **What it is:** An AI-powered IDE formerly known as Codeium, rebranded and rebuilt as a full coding environment. Windsurf features Cascade, an agentic AI system that can handle multi-step coding tasks across files.

**Key Features:**
- **Cascade** — agentic mode that autonomously plans and executes coding tasks
- **Flows** — AI understands and follows your coding patterns and context
- **Tab completion** — fast, context-aware code completions
- **Multi-file editing** — AI can modify multiple files in a single operation
- **Chat** — inline AI conversation with codebase awareness
- **Command palette AI** — natural language commands for IDE actions
- **Extension support** — compatible with VS Code extensions

**Install:**
```bash
# Download from https://windsurf.com
# Available for macOS, Linux, and Windows
```

**Pricing:**
- **Free:** $0 (token-based "Dollar Usage" allowance)
- **Lite:** $8/month
- **Pro:** $20/month
- **Pro+:** $60/month
- **Ultra:** $200/month

---

## 17. Qodo AI

- **Website:** https://www.qodo.ai
- **What it is:** An AI platform focused on code quality and testing (formerly known as CodiumAI). Qodo specializes in generating meaningful tests, reviewing pull requests, and ensuring code integrity.

**Key Features:**
- **Test generation** — automatically generates unit tests for your code
- **PR review** — AI-powered pull request analysis and feedback
- **Code suggestions** — quality-focused improvements and refactoring
- **VS Code extension** — integrate directly into your editor
- **JetBrains extension** — support for IntelliJ, PyCharm, WebStorm
- **CLI tool** — run from your terminal or CI/CD pipeline
- **Multi-language** — Python, JavaScript, TypeScript, Java, Go, and more

**Install:**
```
# VS Code: Search "Qodo" in the Marketplace
# JetBrains: Search "Qodo" in the Plugin Marketplace
# CLI: Follow instructions at qodo.ai
```

**Pricing:**
- **Developer:** $0 (individual use)
- **Teams:** $38/month monthly, or $30/user/month billed annually (workspace pricing, 2,500 pooled credits)
- **Enterprise:** Custom pricing

---

## 18. Zencoder

- **Website:** https://zencoder.ai
- **What it is:** An AI coding assistant with multi-IDE support and context-aware code generation. Zencoder focuses on understanding your full project context to deliver more accurate suggestions and edits.

**Key Features:**
- **Multi-IDE support** — VS Code, JetBrains, and more
- **Context-aware generation** — understands project structure and dependencies
- **Code review** — AI-powered review suggestions
- **Repository indexing** — semantic understanding of your codebase
- **Chat interface** — ask questions about your code
- **Multi-language** — broad programming language support

**Install:**
```
# Install from your IDE's extension/plugin marketplace
# Search "Zencoder" in VS Code (id: zencoder.zencoder) or JetBrains (id: zencoder)
```

**Pricing:**
- **Free tier** — limited usage
- **Pro:** Paid plans for higher usage

---

## 19. ShuttleAI

- **Website:** https://shuttleai.com
- **What it is:** An AI API aggregator that provides access to multiple AI models through a unified API. While not exclusively a coding tool, ShuttleAI is commonly used for coding tasks by routing requests to the best-suited model.

**Key Features:**
- **Unified API** — single endpoint for multiple AI providers
- **Multiple models** — access GPT-4, Claude, Llama, Mistral, and more
- **OpenAI-compatible** — drop-in replacement for OpenAI API calls
- **Affordable pricing** — competitive rates across models
- **Code generation** — use any model for coding tasks
- **Fast switching** — change models by changing one parameter

**Usage:**
```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_SHUTTLE_KEY",
    base_url="https://api.shuttleai.com/v1"
)
response = client.chat.completions.create(
    model="shuttleai/auto",
    messages=[{"role": "user", "content": "Write a Python function to sort a list"}]
)
print(response.choices[0].message.content)
```

**Pricing:**
- **Free:** $0 (2 requests/min, 8K context)
- **Basic:** $10/month (10 req/min, 16K context)
- **Premium:** $25/month (30 req/min, 36K context)
- **Scale:** $75/month (80 req/min, 128K context)
- Request multipliers and on-demand usage on top of the subscription

---

## 20. OpenClaw / ZeroClaw

Two separate open-source projects, not one:

- **OpenClaw** — https://github.com/openclaw/openclaw — a personal agent runtime
- **ZeroClaw** — https://github.com/zeroclaw-labs/zeroclaw — a Rust personal AI assistant runtime

- **What it is:** ZeroClaw is a single-binary Rust personal assistant that reaches the outside world through 30+ channels (Discord, Telegram, Matrix, email, voice, webhooks, its own CLI). It is a general assistant runtime, not a coding agent.

**Key Features:**
- **Terminal-based** — works in any terminal environment
- **Autonomous execution** — plans and executes multi-step coding tasks
- **File operations** — create, edit, and manage project files
- **Shell integration** — run commands and process output
- **Multi-provider** — supports various LLM backends
- **Extensible** — plugin architecture for custom tools

**Install:**
```bash
git clone https://github.com/zeroclaw-labs/zeroclaw.git
cd zeroclaw
# Follow install instructions in README
```

**Pricing:** Free and open-source (bring your own API keys)

---

## 21. Comparison Table

| Tool | Type | Open Source | Key Strength | Pricing |
|------|------|-----------|--------------|---------|
| **Cursor** | IDE | No | All-in-one AI editor | Free / $8 / $30 / $100 / $200 mo |
| **Claude Code** | CLI | No | Best terminal-based agent | API usage (pay-per-token) |
| **Claude Code Router** | Proxy | Yes | Cost reduction for Claude Code | Free (BYOK) |
| **OpenAI Codex** | Cloud Agent | No | Autonomous sandboxed execution | ChatGPT Pro ($200/mo) |
| **Kilo Code** | VS Code Ext | Yes | Multi-provider flexibility | Free (BYOK) |
| **Cline** | VS Code Ext | Yes | Full autonomous coding agent | Free (BYOK) |
| **BlackboxAI** | Extension/Web | No | Code search + web IDE | From $10/mo |
| **Roo Code** | VS Code Ext | Yes | Discontinued (May 2026) — use Cline | Archived |
| **OpenCode** | CLI | Yes | Lightweight terminal agent | Free (BYOK) |
| **Shitty Coding Agent** | Agent | Yes | Fun autonomous agent | Free |
| **Copilot Arena** | VS Code Ext | Yes | Model comparison/benchmarking | Free |
| **Void Editor** | IDE | Yes | Deprecated (June 2026) — reference only | Archived |
| **Kiro** | IDE | No | Spec-driven development | Free / $20/mo |
| **Builder.io Fusion** | Web/Visual | No | Figma-to-code | Free tier / Paid |
| **Trae AI** | IDE | No | AI IDE by ByteDance | Free / $8 / $20 / $60 / $200 mo |
| **Windsurf** | IDE | No | Cascade agentic mode (now Devin Desktop) | Free / $20 mo |
| **Qodo AI** | Extension/CLI | Partial | Test generation, PR review | Free / $30-$38 workspace |
| **Zencoder** | Extension | No | Context-aware multi-IDE | Free tier / Paid |
| **ShuttleAI** | API | No | Multi-model unified API | Free tier / Pay-per-token |
| **OpenClaw/ZeroClaw** | CLI | Yes | Lightweight open-source agent | Free (BYOK) |

**Legend:** BYOK = Bring Your Own (API) Key

---

## 22. Which Should You Use?

| Use Case | Recommended Tool |
|----------|-----------------|
| **Best all-in-one AI IDE** | Cursor or Devin Desktop (ex-Windsurf) |
| **Best terminal-based agent** | Claude Code |
| **Best free/open-source IDE** | Trae AI (or VS Code + Cline) |
| **Best VS Code extension** | Cline |
| **Best for autonomous coding** | Claude Code or OpenAI Codex |
| **Best for testing and quality** | Qodo AI |
| **Best for design-to-code** | Builder.io Fusion |
| **Best for AWS projects** | Kiro |
| **Cheapest AI coding setup** | Cline + Claude Code Router + cheap models |
| **Best for comparing models** | Copilot Arena |
| **Best for beginners** | Cursor (familiar VS Code UI) or Trae AI (free) |
| **Best for privacy/self-hosted** | VS Code + Cline + Ollama |
| **Best for teams** | Cursor Teams or Devin (Enterprise) |
| **Most fun** | Shitty Coding Agent |

---

## See Also

- [AI Platforms & APIs](../ai/platforms-and-apis.md) — OpenRouter, Hugging Face, Pollinations, and inference tools
- [AI Chat Interfaces](../ai/chat-interfaces.md) — ChatGPT, Claude, DeepSeek, and self-hosted chat UIs
