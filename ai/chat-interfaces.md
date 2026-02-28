# AI Chat Interfaces & Assistants

This document covers AI chat platforms — commercial assistants, free web interfaces, prompt engineering tools, and self-hosted chat UIs for running your own private AI.

---

## Table of Contents
1. [Commercial AI Assistants](#1-commercial-ai-assistants)
2. [Free & Open AI Chat Platforms](#2-free--open-ai-chat-platforms)
3. [Prompt Engineering & Community Platforms](#3-prompt-engineering--community-platforms)
4. [Self-Hosted UIs](#4-self-hosted-uis)
5. [Comparison Table](#5-comparison-table)
6. [Which Should You Use?](#6-which-should-you-use)

---

## 1. Commercial AI Assistants

### 1.1 ChatGPT (OpenAI)
- **Website:** https://chatgpt.com
- **Company:** OpenAI
- **Models:** GPT-6 family (Astra, Sol, Sol 1.1, Luna), GPT-5.6 (Sol, Terra, Luna) — OpenAI's tiers are Luna (fastest/cheapest), Sol, 1.1 Sol, and Astra (most capable); Terra belonged to the GPT-5.6 generation
- **Free Tier:** GPT-6 Luna (unlimited text chats; limited uploads, voice, and deep research) — in Chat, Free and Go default to GPT-5.6 Luna
- **Paid:** Go ($8/mo), Plus ($20/mo), Pro ($200/mo)

**Key Features:**
- Text, image, and file analysis
- Code interpreter (runs Python in sandbox)
- Image generation (native model; images carry C2PA provenance metadata)
- Web browsing
- Custom GPTs (create and share specialized chatbots)
- Voice mode (real-time conversation)
- Canvas (collaborative writing/code editing)
- Memory (remembers context across conversations)
- API: https://platform.openai.com

**API:**
```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_KEY")
response = client.chat.completions.create(
    model="gpt-6-luna",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

**Strengths:** Broadest feature set, best plugin ecosystem, voice mode, image generation
**Weaknesses:** Free tier rate-limited on best models, privacy concerns for sensitive data

---

### 1.2 Claude (Anthropic)
- **Website:** https://claude.ai
- **Company:** Anthropic
- **Models:** Claude Fable 5.1 (public release Sep 1, 2026), Claude Mythos 5.1 (same weights, but access restricted to Anthropic's trusted-access programs for vetted cyber/life-science organisations), Claude Opus 5.5 (Sep 22, 2026), Claude Sonnet 5.5 (Sep 28, 2026), Claude Haiku 5.5 (Oct 7, 2026)
- **Free Tier:** Haiku and Sonnet (rate-limited)
- **Paid:** Pro (~$20/mo), Max (5x/20x usage)

**Key Features:**
- 200K–1M token context window (reads entire codebases, books)
- Web search with citations (plus web fetch of page contents)
- Artifacts (generates interactive code, documents, visualizations)
- Projects (organized workspaces with persistent context)
- File upload (PDF, code, images, CSV)
- Computer Use (controls desktop)
- Voice mode (real-time conversation on mobile, desktop, and web)
- Memory (remembers context across conversations)
- API: https://platform.claude.com

**API:**
```python
import anthropic

client = anthropic.Anthropic(api_key="YOUR_KEY")
response = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.content[0].text)
```

**Strengths:** Best for long documents, coding, nuanced reasoning, safety
**Weaknesses:** No image generation, rate limits on free tier

---

### 1.3 Gemini (Google)
- **Website:** https://gemini.google.com
- **Company:** Google DeepMind
- **Models:** Gemini 4 Argon (current flagship, announced Sep 30 2026), Gemini Pro, Gemini Deep Think, Gemini Flash, and Gemini Flash Lite — the Flash line iterates fast (3.5 Flash-Lite → 3.6 → 3.7 → **3.8 Flash**, Sept 2026); "Nano Banana" image models — Nano Banana Pro (Gemini 3 Pro Image), Nano Banana 2 / 2.1 (Gemini 3.x Flash Image)
- **Free Tier:** Auto model selection (mostly Flash-Lite; Flash requires AI Plus)
- **Paid:** Google AI Plus ($4.99/mo), AI Pro ($19.99/mo), AI Ultra ($99.99–$199.99/mo)

**Key Features:**
- Deep Google integration (Gmail, Drive, Docs, Maps)
- 1M token context window (Gemini 3.1 Pro)
- Multimodal (text, image, audio, video input)
- Google Search grounding
- Gems (custom AI personalities)
- Gemini CLI (open-source terminal AI agent)
- API: https://aistudio.google.com

**Strengths:** Largest context window, Google ecosystem integration, multimodal
**Weaknesses:** Model access increasingly gated by plan tier; can be less precise than GPT-6/Claude for complex reasoning

---

### 1.4 Copilot (Microsoft)
- **Website:** https://copilot.microsoft.com
- **Company:** Microsoft
- **Models:** OpenAI GPT-6 family (OpenAI partnership); Claude Sonnet models also serve Microsoft 365 Copilot users
- **Free Tier:** Yes (free with a Microsoft account)
- **Paid:** Pro ($20/mo)

**Key Features:**
- Web search integration (Bing)
- Image generation
- Microsoft 365 integration (Word, Excel, PowerPoint)
- Copilot in Windows (system-level assistant)
- GitHub Copilot (code completion in IDEs)

---

### 1.5 Grok (SpaceXSI)
- **Website:** https://grok.com
- **Company:** SpaceXSI (Elon Musk's AI unit)
- **Models:** Grok 4.7 (Sept 2026 flagship), Grok 4.6, Grok 4.5 (July 2026) — older Grok 4 Fast shipped a 2M-token window
- **Free Tier:** Limited daily access (at grok.com and via X)
- **Paid:** SuperGrok ($30/mo, includes the Grok Build coding agent), X Premium+ ($40/mo)

**Key Features:**
- Real-time X/Twitter data access
- Image and video generation (Grok Imagine)
- DeepSearch / DeeperSearch (multi-step research with citations)
- Grok Build (agentic terminal coding CLI, SuperGrok subscription)
- Less content restrictions than competitors
- API: https://console.x.ai

---

## 2. Free & Open AI Chat Platforms

### 2.1 DeepSeek
- **Website:** https://chat.deepseek.com
- **Company:** DeepSeek (China)
- **Models:** DeepSeek-V4-Pro-0813 & V4-Flash-0731 (1M context, MIT license), DeepSeek-V4.1-Flash (Sept 2026 — new causal encoder-decoder architecture, lower memory, natively multimodal)
- **Free Tier:** Free web chat (generous)
- **API:** Extremely cheap (deepseek-flash: $0.15/M cache-miss input, $0.60/M output off-peak — peak is 2×; Anthropic-format base URL also available), OpenAI-compatible

**Key Features:**
- DeepSeek-V4.1-Flash: 1M-token context (384K max output), thinking mode, native vision — served under the `deepseek-flash` API name
- Strong at math, coding, and Chinese/English
- Open-weight models (download and run locally)
- API: https://platform.deepseek.com

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_DEEPSEEK_KEY",
    base_url="https://api.deepseek.com"
)
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

**Strengths:** Free chat, cheapest API, strong reasoning, open-weight
**Weaknesses:** Censorship on some topics (Chinese regulation), occasional downtime

---

### 2.2 Qwen (Alibaba)
- **Website:** https://qwen.ai
- **Company:** Alibaba Cloud
- **Models:** Qwen3.8-Omni-Flash (Sept 2026), Qwen3.8-Max (2.4T sparse MoE, open weights under a revenue-share license for >$50M/yr providers), Qwen3 Coder
- **Free Tier:** Free web chat
- **API:** Free tier available

**Key Features:**
- Strong multilingual support (Chinese, English, and more)
- Qwen3.8-Omni-Flash: Latest natively multimodal omni model
- Qwen3 Coder: Specialized code model
- Open-weight models available on Hugging Face
- Multimodal (Qwen3.8-Omni accepts text, images, audio, and video)

**Strengths:** Free, strong coding models, open-weight, good multilingual
**Weaknesses:** Less known in Western markets

---

### 2.3 Kimi (Moonshot AI)
- **Website:** https://kimi.com
- **Company:** Moonshot AI (China)
- **Models:** Kimi K3 (2.8T params — the largest open-weights model ever, July 2026, **1M context**), K2.7 Code (open weights, 262K context), K2.6 (April 2026)
- **Free Tier:** Free web chat
- **Paid:** Plus ($19/mo), Pro ($39/mo), Max ($99/mo), Ultra ($199/mo)
- **Key Feature:** Agent Swarm (hundreds of sub-agents for deep research) and the 1M-token window on K3

**Strengths:** Frontier-class open weights, free, strong coding, Agent Swarm
**Weaknesses:** Primarily Chinese-focused, English performance varies

---

### 2.4 ChatZ (chat.z.ai)
- **Website:** https://chat.z.ai
- **What it is:** Free multi-model AI chat interface
- **Free Tier:** Free access to multiple models
- **Features:** Switch between different AI models in one interface

---

### 2.5 MiniMax (Hailuo AI)
- **Website:** https://www.minimax.io / https://agent.minimax.io
- **Company:** MiniMax (China)
- **Models:** MiniMax-M3 (June 2026), M3.1-Flash (Oct 2026), M2.7 + M2.7-Highspeed (Mar 2026), M2.5 + M2.5-Highspeed (Feb 2026), M2.1, M2
- **Free Tier:** Free web chat; MiniMax Agent (free for a limited time)
- **Key Product:** **Hailuo AI Video** — text-to-video generation (competes with Runway, Kling)

**Key Features:**
- Open-weight agentic model line (M2 launched at ~$0.30/M input, $1.20/M output)
- Video generation (Hailuo AI — free credits)
- Voice + music generation
- API: https://platform.minimax.io

**Strengths:** MiniMax Agent product, cheap open-weight API, multimodal
**Weaknesses:** Less established outside China

---

### 2.6 Poe (Quora)
- **Website:** https://poe.com
- **Company:** Quora
- **What it is:** Multi-model chat platform — access GPT-6, Claude, Gemini, Llama, and more from one interface
- **Free Tier:** Limited daily messages
- **Paid:** $20/mo (higher limits)
- **Features:** Create custom bots, share bots, API access

---

### 2.7 Perplexity AI
- **Website:** https://perplexity.ai
- **What it is:** AI-powered search engine with citations
- **Free Tier:** Free (limited Pro searches)
- **Paid:** Pro ($20/mo)
- **Strength:** Always cites sources, real-time web access

---

### 2.8 HuggingChat
- **Website:** https://huggingface.co/chat
- **What it is:** Open-source chat interface powered by Hugging Face Inference Providers
- **Free Tier:** Free (monthly inference credits; PRO tier gets a larger allowance)
- **Models:** Llama, Qwen, DeepSeek, and more
- **Features:** Web search, tools, model switching

---

### 2.9 Duck.ai (DuckDuckGo)
- **Website:** https://duck.ai
- **What it is:** Private AI chat (no data stored)
- **Free Tier:** Free; DuckDuckGo Subscription (Pro/Plus, ex-Privacy Pro) adds limits + advanced models
- **Models:** OpenAI, Anthropic, and Mistral models (rotating lineup — see duck.ai for the current list)
- **Extras:** Image generation with C2PA metadata, voice chat (added January 2026)
- **Strength:** Complete privacy — conversations stored locally on-device; prompts anonymized and not retained for training

---

### 2.10 Sakana Chat (Sakana AI)
- **Website:** https://chat.sakana.ai — main: https://sakana.ai
- **Company:** Sakana AI (Tokyo; founded by David Ha, Llion Jones, Ren Ito)
- **Models:** Fugu (orchestrator; Max / Cyber / Ultra tiers), Namazu (Japanese specialist — web search + code execution built in; "High" tier in the chat)
- **Differentiator:** Fugu routes each task step to the right frontier model (cost-vs-performance Pareto frontier); keeps working if a provider goes down
- **Research:** Trinity + The Conductor (ICLR 2026), AB-MCTS (NeurIPS 2025 Spotlight)
- **Also:** Sakana Translate (translate.sakana.ai, built on Namazu); deployed at MUFG, SMBC, Daiwa, Japan MoD/ATLA
- **Weaknesses:** proprietary; smaller ecosystem than Western majors

---

## 3. Prompt Engineering & Community Platforms

### 3.1 PromptHero
- **Website:** https://prompthero.com
- **What it is:** Search engine for AI prompts (text + image generation)
- **Features:** Prompt search, image prompt library, community

---

### 3.2 Toggle's Jailbreaks (togg53192-cmd/jailbreaks)
- **Repository:** https://github.com/togg53192-cmd/jailbreaks
- **What it is:** curated collection of 31 paste-ready prompt files targeting 25+ models (3.1k stars, updated Oct 2026)
- **Contents:** system prompts, persona locks, workspace policies, `AGENTS.md` files, config blocks, Ollama Modelfiles — complete files, no excerpts
- **Targets:** OpenCode Zen stealth models (Big Pickle, Space Bunny, LongCat 2.5, MiMo V2.6, Muse Spark…), open-weight families (GLM, DeepSeek, Kimi, Qwen, Gemma, GPT-OSS), closed frontier (Claude, Gemini, Grok, Mistral)
- **Use case:** studying instruction hierarchies, persona framing, prompt conflicts, policy overrides (prompt-injection defense research)
- **Caveat:** research/education-framed per the repo's own warning; platform ToS still apply

---

### 3.3 Forge (twaai/forge)
- **Repository:** https://github.com/twaai/forge
- **What it is:** Forge 3.1 — desktop prompt workshop: describe a goal → get a ready-to-run system prompt → revise via chat
- **Features:** streaming chat, saved threads (search/rename/reopen), hosted model picker, PURPOSE / ROLE / TASK / OUTPUT prompt compilation, refusal recovery
- **Platforms:** Windows / Linux x64, macOS (Apple Silicon + Intel); SHA-256 checksums per release; Python source
- **Caveat:** small project (16 stars); hosted providers only (Ollama support removed in 3.1)

---

## 4. Self-Hosted UIs

Run your own private AI interface — chat UIs for local models or external APIs, plus a node-based generation workspace.

### 4.1 LibreChat
- **Repository:** https://github.com/danny-avila/LibreChat
- **What it is:** Open-source ChatGPT-clone UI supporting multiple AI providers
- **License:** MIT

**Supported Backends:**
- OpenAI (GPT-6, GPT-5.6)
- Anthropic (Claude)
- Google (Gemini)
- Azure OpenAI
- Ollama (local models)
- Any OpenAI-compatible API (OpenRouter, Together, Groq, etc.)
- Plugins and tools support

```bash
# Docker deployment
git clone https://github.com/danny-avila/LibreChat.git
cd LibreChat
cp .env.example .env
# Edit .env with your API keys
docker compose up -d
# Access at http://localhost:3080
```

**Key Features:**
- Multi-model conversations
- User authentication and management
- Conversation search and export
- File uploads
- Plugin system
- Presets and prompt templates
- Mobile-friendly

**Best for:** Teams or individuals who want a unified private chat UI for all AI providers.

> **See Also:** [Docker Essentials](../devtools/docker-essentials.md) for Docker fundamentals and a detailed LibreChat Docker deployment walkthrough.

---

### 4.2 Open WebUI
- **Repository:** https://github.com/open-webui/open-webui
- **What it is:** Self-hosted ChatGPT-style interface, designed for Ollama
- **License:** Open WebUI License (custom BSD-3 derivative; branding must stay above 50 end users / 30 days without enterprise permission)

```bash
# Run with Docker (connects to local Ollama)
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  ghcr.io/open-webui/open-webui:main

# Access at http://localhost:3000
```

**Key Features:**
- Beautiful UI (closest to ChatGPT)
- Ollama integration (auto-detects local models)
- OpenAI API support
- RAG (upload documents, chat with them)
- User management
- Voice input/output
- Model management and download
- Web search integration
- Image generation
- Pipelines (custom processing)

**Best for:** Running a private ChatGPT with local Ollama models.

---

### 4.3 text-generation-webui (oobabooga)
- **Repository:** https://github.com/oobabooga/text-generation-webui
- **What it is:** Gradio-based web UI for running LLMs locally
- **Features:** GGUF, GPTQ, AWQ, ExLlama support; character chat; extensions; training

---

### 4.4 SillyTavern
- **Repository:** https://github.com/SillyTavern/SillyTavern
- **What it is:** Frontend for LLM roleplay and character chat
- **Features:** Character cards, world info, group chats, TTS
- **Backends:** OpenAI, Claude, Ollama, KoboldCPP, and more

---

### 4.5 Chatbot UI
- **Repository:** https://github.com/mckaywrigley/chatbot-ui
- **What it is:** Open-source ChatGPT interface
- **Features:** Clean UI, OpenAI/Ollama support, conversation management
- **Note:** development dormant — last commit June 2024

---

### 4.6 Big-AGI
- **Repository:** https://github.com/enricoros/big-AGI
- **What it is:** Feature-rich AI chat with multi-model support
- **Features:** Personas, code execution, image generation, voice, multi-chat

---

### 4.7 ComfyUI
- **Repository:** https://github.com/comfyanonymous/ComfyUI
- **What it is:** open-source node-based workflow UI for diffusion-model generation (image/video) — not a chat interface
- **How it works:** nodes (model loader, CLIP encode, samplers, VAE, ControlNet, LoRA, upscalers) wire into a saved graph; workflows export as JSON and can be embedded in generated images
- **Models:** Stable Diffusion family, Flux, Hunyuan-DiT, Civitai checkpoints
- **State:** ~141k stars (Oct 2026), Comfy Org; 1,674+ node types (Dec 2024); video via AnimateDiff
- **License:** GPL-3.0

---

## 5. Comparison Table

### Commercial Assistants

| Platform | Free Tier | Best Model | Context Window | Image Gen | Web Search | Voice | API |
|----------|-----------|-----------|---------------|-----------|-----------|-------|-----|
| **ChatGPT** | GPT-6 Luna (limited) | GPT-6.1 Sol / Astra | — | ✅ | ✅ | ✅ | ✅ |
| **Claude** | Haiku + Sonnet (limited) | Opus 5.5 / Sonnet 5.5 | Up to 1M | ❌ | ✅ | ✅ | ✅ |
| **Gemini** | Flash-Lite (generous) | Gemini 4 Argon / 3.8 Flash | 1M+ | ✅ | ✅ | ✅ | ✅ |
| **Copilot** | Free (Microsoft account) | GPT-6 family | — | ✅ | ✅ Bing | ✅ | ✅ |
| **Grok** | Limited | Grok 4.7 | 500K | ✅ Grok Imagine | ✅ X data | ✅ | ✅ |

### Free & Open Platforms

| Platform | Free Tier | Models | Open-Weight | API | Best For |
|----------|-----------|--------|------------|-----|----------|
| **DeepSeek** | Generous | V4-Pro, V4.1-Flash | ✅ | ✅ (cheap) | Reasoning, code |
| **Qwen** | Free chat | 3.8, Coder | ✅ | ✅ | Multilingual, code |
| **Kimi** | Free chat | K3, K2.7 Code | ✅ | ✅ | Open weights, Agent research |
| **HuggingChat** | Free (credits) | Many | ✅ | Via HF | Open models |
| **Duck.ai** | Free (+ paid sub) | OpenAI, Anthropic, Mistral | N/A | ❌ | Privacy |
| **Perplexity** | Free + Pro | Multiple | N/A | ✅ | Search + citations |
| **Poe** | Limited | Multiple | N/A | ✅ | Multi-model |
| **Sakana Chat** | Free (sign-in) | Fugu orchestrator + Namazu | ❌ | ✅ | Model orchestration, Japanese |

### Self-Hosted UIs

| Platform | Backend Support | RAG | User Mgmt | Docker | Best For |
|----------|----------------|-----|-----------|--------|----------|
| **LibreChat** | All major APIs + Ollama | ✅ | ✅ | ✅ | Multi-provider unified UI |
| **Open WebUI** | Ollama + OpenAI API | ✅ | ✅ | ✅ | Local Ollama frontend |
| **text-gen-webui** | Local models (GGUF, GPTQ) | ❌ | ❌ | ✅ | Power users, model testing |
| **SillyTavern** | Many backends | ❌ | ❌ | ✅ | Roleplay, character chat |
| **Big-AGI** | Many APIs | ❌ | ❌ | ✅ | Feature-rich multi-chat |
| **ComfyUI** | Diffusion models (SD, Flux, Hunyuan) | ❌ | ❌ | ✅ | Node-based image/video generation |

---

## 6. Which Should You Use?

| Need | Recommended |
|------|------------|
| **Best overall assistant** | ChatGPT (Plus) or Claude (Pro) |
| **Best free assistant** | DeepSeek or Gemini |
| **Best for coding** | Claude or DeepSeek |
| **Best for Japanese** | Sakana Chat (Namazu) |
| **Best for research** | Perplexity (citations) or Gemini (long context) |
| **Best for privacy** | Duck.ai or Ollama (local) |
| **Completely free, no limits** | DeepSeek chat + Pollinations API |
| **Self-hosted for team** | LibreChat + Ollama |
| **Self-hosted for personal** | Open WebUI + Ollama |
| **Best local model runner** | Ollama (easy) or llama.cpp (performance) |
| **Multi-model comparison** | Poe or OpenRouter |
| **Prompt engineering** | PromptHero, Toggle's jailbreaks, or Forge (§3) |
| **Cheapest API** | DeepSeek API or OpenRouter free models |

---

## See Also

- [AI Platforms & APIs](platforms-and-apis.md) — OpenRouter, Hugging Face, Pollinations, Runway ML, and inference tools
- [Penetration Testing Tools](../security/penetration-testing-tools.md) — Security tools that can integrate with AI
