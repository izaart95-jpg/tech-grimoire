# AI Platforms, APIs & Creative Tools

This document covers AI model hosting platforms, API aggregators, free inference endpoints, and AI-powered creative tools — essential for developers, researchers, and builders integrating AI into projects.

---

## Table of Contents
1. [API Aggregators & Routers](#1-api-aggregators--routers)
2. [Model Hosting & Inference](#2-model-hosting--inference)
3. [Free & Open Inference](#3-free--open-inference)
4. [AI Creative & Media Tools](#4-ai-creative--media-tools)
5. [Local AI Inference](#5-local-ai-inference)
6. [Comparison Table](#6-comparison-table)
7. [Pricing & Free Tier Summary](#7-pricing--free-tier-summary)
8. [Getting Started Examples](#8-getting-started-examples)
9. [New Paradigms: Model Metadata and Machine-Native Intelligence](#9-new-paradigms-model-metadata-and-machine-native-intelligence)

---

## 1. API Aggregators & Routers

These platforms provide a **single API endpoint** that routes requests to many different AI models and providers.

### 1.1 OpenRouter
- **Website:** https://openrouter.ai
- **What it is:** Unified API gateway to 470+ models from OpenAI, Anthropic, Google, Meta, and the open-source labs (471 models verified via the live `/api/v1/models` endpoint, Oct 2026)
- **Pricing:** Pay-per-token, varies by model. Some models are **free** (rate-limited)
- **API:** OpenAI-compatible (`/v1/chat/completions`)
- **Key Feature:** Single API key → access GPT-6.x, Claude, Gemini, Kimi, Qwen, GLM, etc.

**Why use it:**
- Don't need separate accounts for every provider
- Automatic fallback between providers
- Compare models easily
- Some free models available (e.g., free Llama, Mistral variants)

```python
import requests

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer YOUR_OPENROUTER_KEY",
        "Content-Type": "application/json"
    },
    json={
        "model": "nvidia/nemotron-3.5-lightning:free",
        "messages": [{"role": "user", "content": "Hello!"}]
    }
)
print(response.json()["choices"][0]["message"]["content"])
```

**Free Models on OpenRouter (rate-limited — 17 free verified Oct 21, 2026):**
- `thinkingmachines/inkling-small:free`
- `poolside/laguna-xs-2.1:free`
- `nvidia/nemotron-3.5-lightning:free`
- `cohere/north-mini-code:free`
- Free slots rotate often — check current: https://openrouter.ai/models?q=free

---

### 1.2 g4f (GPT4Free)
- **Website:** https://g4f.ai / https://github.com/xtekky/gpt4free
- **What it is:** Open-source library that provides free access to AI models through reverse-engineered and public provider endpoints
- **Pricing:** Free
- **Language:** Python
- **Models:** rotating provider lineup (GPT-6.x, Claude, Kimi, DeepSeek, Gemini — whatever providers currently work; 66.9k stars, updated daily)

> ⚠️ **Legal Notice:** g4f uses unofficial API endpoints. Reliability varies. Providers can break at any time. Not recommended for production use. Review terms of service for each provider.

```python
import g4f

response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response)
```

**Key Features:**
- No API key required for many providers
- OpenAI-compatible API server mode
- Web UI included
- Provider rotation and fallback

```bash
# Install
pip install g4f

# Run local API server (OpenAI-compatible)
g4f api

# Run web UI
g4f gui
```

---

### 1.3 TokenRouter
- **Website:** https://www.tokenrouter.com
- **What it is:** unified AI model hub — leading LLMs behind one endpoint ("verified models with enterprise-grade controls")
- **API:** OpenAI, Claude, and Gemini compatible formats
- **Target:** individuals and enterprises; centralized key/usage management
- **Note:** built on the open-source `new-api` gateway — self-hosted equivalent available

---

### 1.4 OpenCode Zen
- **Website:** https://opencode.ai/zen
- **What it is:** curated, benchmarked model gateway from the OpenCode team — "reliable optimized models for coding agents"; works with any agent
- **Models:** tested model-provider combinations only; includes free stealth models (Big Pickle, Space Bunny, LongCat 2.5, MiMo V2.6, Step 5 Preview, Muse Spark 1.3)
- **Pricing:** $20 pay-as-you-go balance, per-request "zero markups", auto top-up at $5
- **Privacy:** US-hosted; zero-retention providers (documented exceptions)
- **API:** OpenAI-compatible

---

## 2. Model Hosting & Inference

### 2.1 Hugging Face
- **Website:** https://huggingface.co
- **What it is:** The largest open-source AI model hub — hosting, training, datasets, and inference
- **Models:** 500,000+ models (text, image, audio, video, multimodal)
- **Free Tier:** Free Inference API (rate-limited), free model hosting, free Spaces

**Core Services:**

| Service | Description | Free? |
|---------|-------------|-------|
| **Hub** | Host and share models, datasets, Spaces | ✅ |
| **Inference API** | Run any hosted model via API | ✅ (rate-limited) |
| **Inference Endpoints** | Dedicated GPU inference | 💰 Pay-per-hour |
| **Spaces** | Host Gradio/Streamlit apps | ✅ (CPU), 💰 (GPU) |
| **Datasets** | 100,000+ datasets | ✅ |
| **Transformers** | Python library for model loading | ✅ Open source |
| **GGUF/GPTQ/AWQ Models** | Quantized models for local inference | ✅ |

```python
# Free Inference API
from huggingface_hub import InferenceClient

client = InferenceClient(token="hf_YOUR_TOKEN")
response = client.text_generation(
    "Explain quantum computing",
    model="meta-llama/Llama-3.1-8B-Instruct"
)
print(response)
```

```bash
# Download a model
pip install huggingface_hub
hf download TheBloke/Llama-2-7B-GGUF llama-2-7b.Q4_K_M.gguf   # `huggingface-cli` is deprecated
```

**Why it matters:** Hugging Face is the GitHub of AI. Most open-source models are hosted here. If you work with AI, you will use Hugging Face.

---

### 2.2 Replicate
- **Website:** https://replicate.com
- **What it is:** Run open-source AI models in the cloud via simple API
- **Pricing:** Pay-per-second of compute
- **Models:** Llama, Stable Diffusion, Whisper, and thousands more
- **API:** REST + Python/JS SDKs

```python
import replicate

output = replicate.run(
    "meta/llama-2-70b-chat",
    input={"prompt": "What is quantum computing?"}
)
print(output)
```

---

### 2.3 Together AI
- **Website:** https://www.together.ai
- **What it is:** Fast inference and fine-tuning for open-source models
- **Free Tier:** $1 free credit on signup
- **Models:** Llama, Mixtral, Qwen, Code Llama, and more
- **API:** OpenAI-compatible

---

### 2.4 Groq
- **Website:** https://groq.com
- **What it is:** Ultra-fast inference using custom LPU (Language Processing Unit) hardware
- **Free Tier:** Free API access (rate-limited)
- **Speed:** Fastest available inference (500+ tokens/sec for Llama 3)
- **API:** OpenAI-compatible

```python
from groq import Groq

client = Groq(api_key="YOUR_KEY")
response = client.chat.completions.create(
    model="llama-3.1-70b-versatile",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

---

### 2.5 Fireworks AI
- **Website:** https://fireworks.ai
- **What it is:** Fast inference platform for open models
- **Free Tier:** Free credits on signup
- **API:** OpenAI-compatible
- **Models:** Llama, Mixtral, Qwen, function-calling models

---

### 2.6 Cerebras
- **Website:** https://cerebras.ai
- **What it is:** AI inference on custom wafer-scale chips
- **Free Tier:** Free API (rate-limited)
- **Speed:** Extremely fast inference (competes with Groq)
- **API:** OpenAI-compatible

### 2.7 NVIDIA NIM
- **Website:** https://build.nvidia.com
- **What it is:** prebuilt, optimized inference microservices for foundation models — hosted API endpoints + self-hostable containers
- **Free Tier:** free API credits on build.nvidia.com (pick model → get key)
- **API:** OpenAI-compatible
- **Models:** NVIDIA Nemotron family (Nemotron 3 / 3.5 Lightning, Super VL, Content Safety…) + partner models

---

### 2.8 ModelScope
- **Website:** https://www.modelscope.cn
- **What it is:** Alibaba's open model community — models, datasets, online demos (China's Hugging Face alternative)
- **Content:** Qwen family at release, most Chinese labs' open weights, large dataset collection
- **Free Tier:** free in-browser demos (Studio) + SDK/API
- **Note:** Chinese-first UI, region-fast hosting

---

## 3. Free & Open Inference

### 3.1 Pollinations AI
- **Website:** https://pollinations.ai
- **What it is:** Free, open-source AI generation platform — text, images, audio, code
- **Pricing:** Completely free, no API key required
- **API:** REST endpoints, no auth needed

**Text Generation:**
```bash
curl "https://text.pollinations.ai/What%20is%20Linux?"
```

**Image Generation:**
```bash
# Returns image directly
curl "https://image.pollinations.ai/prompt/A%20cyberpunk%20city" --output image.jpg
```

**Key Features:**
- No API key, no signup, no rate limits (fair use)
- Text, image, and code generation
- OpenAI-compatible chat endpoint
- Great for prototyping and education

```python
import requests

# Text
response = requests.get("https://text.pollinations.ai/Explain DNS in one paragraph")
print(response.text)

# Image (returns PNG)
img = requests.get("https://image.pollinations.ai/prompt/A%20futuristic%20server%20room")
with open("output.png", "wb") as f:
    f.write(img.content)
```

---

### 3.2 Hugging Face Inference API
- Free tier with rate limits
- Access to thousands of models
- See section 2.1 above

---

### 3.3 Google AI Studio (Gemini)
- **Website:** https://aistudio.google.com
- **Free Tier:** Free Gemini API access (rate-limited)
- **Models:** the current Gemini Flash / Pro line (3.x era — the Flash line iterates fast; check the AI Studio model picker)
- **API:** Google AI SDK + OpenAI-compatible

---

## 4. AI Creative & Media Tools

### 4.1 Runway ML
- **Website:** https://runwayml.com
- **What it is:** AI-powered creative suite for video, image, and media generation
- **Key Product:** current line is **Gen-4.5** plus the **Aleph 2.0** in-context editor (Gen-3 Alpha is retired — see [AI Video Tools](ai-video-tools.md) for the full verified video-model landscape)

**Features:**
| Tool | Function |
|------|----------|
| **Gen-4.5** | Text/image to video generation |
| **Aleph 2.0** | In-context video editing |
| **Inpainting** | Remove/replace objects in images |
| **Motion Brush** | Add motion to static images |
| **Super Slow Motion** | AI frame interpolation |
| **Background Removal** | Automatic subject isolation |
| **Text to Image** | Generate images from prompts |
| **Upscaling** | AI image resolution enhancement |
| **Audio Cleanup** | Remove background noise |

**Pricing:**
- Free Tier: $0 — 125 one-time credits
- Standard: $12/month billed annually ($15 monthly) — 625 credits/mo
- Pro: $28/month billed annually ($35 monthly) — 2250 credits/mo
- Max: $76/month billed annually ($95 monthly) — 9500 credits/mo (credits roll over one month)

**Use Cases:**
- Film and video production
- Content creation
- Social media
- Advertising
- Art and design

---

### 4.2 Stability AI
- **Website:** https://stability.ai
- **Products:** Stable Diffusion (image), Stable Video Diffusion, Stable Audio
- **Open Source:** Core models are open-weight
- **API:** https://platform.stability.ai
- **Free Tier:** Free credits on signup

---

### 4.3 ElevenLabs
- **Website:** https://elevenlabs.io
- **What it is:** AI voice synthesis and cloning
- **Free Tier:** 10,000 characters/month
- **Features:** Text-to-speech, voice cloning, audio dubbing

---

### 4.4 Suno AI
- **Website:** https://suno.com
- **What it is:** AI music generation
- **Free Tier:** 10 songs/day
- **Features:** Text-to-music, lyrics generation

---

### 4.5 Leonardo AI
- **Website:** https://leonardo.ai
- **What it is:** AI image generation platform
- **Free Tier:** 150 tokens/day
- **Features:** Image generation, fine-tuning, canvas editor

---

### 4.6 Ideogram
- **Website:** https://ideogram.ai
- **What it is:** AI image generation (strong text rendering)
- **Free Tier:** Free daily generations
- **Strength:** Best at rendering text within images

---

### 4.7 Flux (by Black Forest Labs)
- **Website:** https://blackforestlabs.ai
- **What it is:** Open-weight image generation model
- **Models:** FLUX.2 family (FLUX.2, FLUX.2 [max], FLUX.2 Klein), FLUX.1 Kontext, FLUX.1 [dev]/[schnell]/[pro], FLUX 1.1 Pro / Pro Ultra
- **Free:** Dev and Schnell models are open
- **Available on:** Hugging Face, Replicate, ComfyUI

---

### 4.8 Kling AI
- **Website:** https://klingai.com
- **What it is:** Text/image to video generation (by Kuaishou)
- **Free Tier:** Free daily credits
- **Strength:** High-quality video generation

---

## 5. Local AI Inference

Tools for running AI models on your own hardware.

### 5.1 Ollama
- **Website:** https://ollama.com
- **What it is:** Run LLMs locally with a single command
- **Platform:** macOS, Linux, Windows
- **API:** OpenAI-compatible (`/v1/chat/completions`)

```bash
# Install
curl -fsSL https://ollama.com/install.sh | sh

# Download and run models
ollama pull llama3.1
ollama pull mistral
ollama pull qwen2.5
ollama pull codellama
ollama pull gemma2

# Run interactively
ollama run llama3.1

# Serve API
ollama serve
# API available at http://localhost:11434

# List models
ollama list

# API usage
curl http://localhost:11434/v1/chat/completions \
  -d '{
    "model": "llama3.1",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

**Model Library:** https://ollama.com/library
- hundreds of models: Llama, Mistral, Qwen3.8, GLM-5, Gemma 4, DeepSeek, Kimi, Phi, and more

---

### 5.2 llama.cpp
- **Repository:** https://github.com/ggerganov/llama.cpp
- **What it is:** High-performance C/C++ inference engine for LLMs
- **Format:** GGUF (quantized models)
- **Platform:** CPU (any), GPU (CUDA, Metal, Vulkan, ROCm, SYCL)
- **Key Feature:** Runs models on consumer hardware, from phones to servers

```bash
# Build
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
cmake -B build
cmake --build build --config Release

# Run model
./build/bin/llama-cli \
  -m models/llama-3.1-8b-q4_k_m.gguf \
  -p "Explain Linux in simple terms" \
  -n 256

# Run server (OpenAI-compatible API)
./build/bin/llama-server \
  -m models/llama-3.1-8b-q4_k_m.gguf \
  --host 0.0.0.0 --port 8080
```

**Quantization Levels:**
| Quantization | Size Reduction | Quality | Speed |
|-------------|---------------|---------|-------|
| Q8_0 | ~50% | Excellent | Moderate |
| Q6_K | ~60% | Very Good | Good |
| Q5_K_M | ~65% | Good | Good |
| Q4_K_M | ~70% | Good | Fast |
| Q3_K_M | ~75% | Decent | Fast |
| Q2_K | ~80% | Low | Fastest |

**Recommendation:** Q4_K_M offers the best balance of quality and speed for most users.

---

### 5.3 LM Studio
- **Website:** https://lmstudio.ai
- **What it is:** Desktop GUI for downloading and running LLMs locally
- **Platform:** macOS, Linux, Windows
- **Features:** Model browser (Hugging Face), chat UI, local server
- **API:** OpenAI-compatible
- **Best for:** Users who want a GUI experience

---

### 5.4 LocalAI
- **Website:** https://localai.io
- **Repository:** https://github.com/mudler/LocalAI
- **What it is:** Drop-in OpenAI API replacement, runs locally
- **Features:** Text, image, audio, embeddings — all local
- **API:** OpenAI-compatible

---

### 5.5 vLLM
- **Repository:** https://github.com/vllm-project/vllm
- **What it is:** High-throughput LLM serving engine
- **Key Feature:** PagedAttention for efficient memory management
- **Best for:** Production deployments, high-concurrency serving
- **API:** OpenAI-compatible

---

### 5.6 Jan
- **Website:** https://jan.ai
- **What it is:** Open-source alternative to ChatGPT that runs fully offline
- **Platform:** macOS, Linux, Windows
- **Features:** Chat UI, model management, local API, extensions

---

### 5.7 SGLang
- **Repository:** https://github.com/sgl-project/sglang — site: https://sglang.io
- **What it is:** high-performance serving framework for LLM, vision-language, and diffusion models — built for agentic workloads, large-scale serving, RL rollouts
- **License:** Apache 2.0 — 37k stars
- **Extras:** SGLang Diffusion (built-in image/video generation engine)
- **API:** OpenAI-compatible; Docker (`lmsysorg/sglang`) or `uv pip install sglang`

---

### 5.8 FreeToken (FlashML)
- **Repository:** https://github.com/FlashML-org/FreeToken — site: https://www.flashml.ai
- **What it is:** edge-native MoE serving engine — 290B+ frontier open-weight models on consumer hardware (14.5k stars, arXiv paper)
- **Tech:** bandwidth-adaptive CPU–GPU co-execution, global LRU expert caching, runtime VRAM re-allocation, semantic anchor checkpoints for agentic context edits
- **Models:** DeepSeek-V4-Flash, Qwen3.6-35B-A3B, GLM-5.2; MXFP4 / NVFP4 / FP8 / BF16
- **API:** OpenAI- and Anthropic-compatible (Codex, Claude Code, OpenCode, OpenClaw)
- **Hardware:** RTX 30/40/50 desktop + laptop GPUs; Windows/Linux desktop app or CLI (uv/pip)

---

## 6. Comparison Table

### API Providers & Aggregators

| Platform | Free Tier | Models | API Compatible | Best For |
|----------|-----------|--------|---------------|----------|
| **OpenRouter** | 16 free models | 470+ | OpenAI | Multi-provider access |
| **g4f** | Free | Many | OpenAI | Experimentation |
| **TokenRouter** | — | Many | OpenAI / Claude / Gemini formats | Enterprise-managed aggregation |
| **OpenCode Zen** | Some free stealth models | Curated set | OpenAI | Coding agents |
| **Hugging Face** | Rate-limited API | 500K+ | HF / OpenAI | Open-source models |
| **Groq** | Rate-limited | ~20 | OpenAI | Speed |
| **Cerebras** | Rate-limited | ~10 | OpenAI | Speed |
| **Together AI** | $1 credit | 100+ | OpenAI | Open model fine-tuning |
| **Fireworks AI** | Free credits | 50+ | OpenAI | Fast open model serving |
| **Pollinations** | Fully free | Several | REST | No-key prototyping |
| **Replicate** | Pay-per-second | 1000+ | REST | Run any model |
| **Google AI Studio** | Rate-limited | Gemini | Google / OpenAI | Gemini access |

### Local Inference

| Tool | GUI | API | GPU Required | Best For |
|------|-----|-----|-------------|----------|
| **Ollama** | No (CLI) | OpenAI-compat | Optional | Easy local LLMs |
| **llama.cpp** | No (CLI) | OpenAI-compat | Optional | Maximum performance |
| **LM Studio** | Yes | OpenAI-compat | Optional | Desktop users |
| **LocalAI** | No | OpenAI-compat | Optional | Self-hosted API |
| **Jan** | Yes | OpenAI-compat | Optional | Offline ChatGPT |
| **vLLM** | No | OpenAI-compat | Yes (GPU) | Production serving |
| **SGLang** | No | OpenAI-compat | Yes (GPU) | Production + agentic/RL serving |
| **FreeToken** | Desktop GUI + CLI | OpenAI + Anthropic-compat | Consumer GPU (RTX 30/40/50) | 290B+ MoE at home |

### Creative AI Tools

| Platform | Type | Free Tier | Strength |
|----------|------|-----------|----------|
| **Runway ML** | Video/Image | 125 credits | Best text-to-video |
| **Stability AI** | Image/Video/Audio | Free credits | Open-weight models |
| **ElevenLabs** | Voice | 10K chars/mo | Voice cloning |
| **Suno** | Music | 10 songs/day | Text-to-music |
| **Leonardo AI** | Image | 150 tokens/day | Image generation |
| **Ideogram** | Image | Free daily | Text in images |
| **Flux** | Image | Open models | Open-weight quality |
| **Kling AI** | Video | Free credits | Video generation |
| **Pollinations** | Text/Image | Unlimited | Zero-friction |

---

## 7. Pricing & Free Tier Summary

### Completely Free (No Payment Required)
- **Pollinations AI** — text + image generation, no key needed
- **g4f** — open-source, community providers
- **Duck.ai** — free, private (limited models)
- **OpenCode Zen free tier** — free stealth models (Big Pickle, Space Bunny, LongCat…)
- **Hugging Face Inference API** — rate-limited
- **Groq** — rate-limited free tier
- **Cerebras** — rate-limited free tier
- **Ollama / llama.cpp / SGLang / FreeToken** — run on your hardware

### Free Credits on Signup
- **Together AI** — $1 credit
- **Fireworks AI** — free credits
- **Replicate** — free credits
- **Stability AI** — free credits
- **NVIDIA NIM** — free API credits at build.nvidia.com
- **ModelScope** — free in-browser demos and SDK
- **Google AI Studio** — generous free tier

### Pay-Per-Use (No Subscription)
- **OpenRouter** — pay per token
- **Replicate** — pay per second

---

## 8. Getting Started Examples

### Fastest Free Text Generation (No Key)
```bash
# Pollinations — zero setup
curl "https://text.pollinations.ai/What%20is%20a%20kernel?"
```

### Fastest Free Image Generation (No Key)
```bash
curl "https://image.pollinations.ai/prompt/A%20hacker%20terminal%20with%20green%20text" -o image.jpg
```

### Fastest Local Setup
```bash
# Ollama — one command
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3.1
```

### OpenRouter Multi-Model Access
```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nvidia/nemotron-3.5-lightning:free",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

---

## 9. New Paradigms: Model Metadata and Machine-Native Intelligence

### 9.1 Models.dev
- **Website:** https://models.dev — repo: https://github.com/sst/models.dev
- **What it is:** open-source database of AI models — context window, max output, capabilities (reasoning / tool call / structured), open vs closed weights, release dates, live provider pricing
- **Note:** updated within hours of releases; machine-readable data; the spec/pricing layer most agent tools resolve against

### 9.2 TypeSafe AI
- **Website:** https://typesafe.ai — console: https://console.typesafe.ai — docs: https://docs.typesafe.ai
- **What it is:** "System One Models" — models built for machines, not chat; trained with RLCD (Reinforcement Learning for Calibrated Decisions)
- **Key product:** Jev (early access) — returns typed decisions with calibrated confidence; act/escalate thresholds; composes in code
- **Claimed economics:** $42/B input tokens; 193.6x faster / 444.6x cheaper than LLMs on their workflows (vendor-published)
- **State:** v0.x, early access (Oct 2026)
- **Compare:** Sakana Fugu ([chat-interfaces.md](chat-interfaces.md)) orchestrates frontier models; TypeSafe replaces prose with machine-decisions

---

## See Also

- [AI Chat Interfaces](chat-interfaces.md) — ChatGPT, Claude, DeepSeek, Kimi, Sakana Chat, and self-hosted UIs
- [AI Video Tools](ai-video-tools.md) — the verified video-generation landscape (Veo, Kling, Seedance, Wan, Hunyuan)
- [Network Protocols](../fundamentals/network-protocols.md) — HTTP/REST/gRPC protocols used by AI APIs
