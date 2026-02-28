# AI Video Tools

This document explains what "AI video tools" actually split into as a landscape — five capability families that solve fundamentally different problems — with representative tools as references for each. The worked example at the end goes deeper on one family, because hands-on understanding of one makes the rest legible.

> **Ethical Notice:** Identity manipulation (face swap/deepfake) carries legal and ethical weight — impersonating real people without consent, misinformation, and harassment are harmful and illegal in many jurisdictions. Use the manipulation families for legitimate creative, research, and entertainment work, disclose AI-generated content, and note that several of the model weights described below are explicitly non-commercial.

---

## Table of Contents
1. [The Landscape — Five Families](#1-the-landscape--five-families)
2. [Face Swap & Identity Manipulation](#2-face-swap--identity-manipulation)
3. [Generative Video — Text/Image-to-Video](#3-generative-video--textimage-to-video)
4. [Talking Heads & Avatars](#4-talking-heads--avatars)
5. [Editing, Enhancement & Restoration](#5-editing-enhancement--restoration)
6. [Video Understanding & Analysis](#6-video-understanding--analysis)
7. [Worked Example — Deep-Live-Cam](#7-worked-example--deep-live-cam)
8. [Choosing Tools](#8-choosing-tools)
9. [See Also](#9-see-also)

---

## 1. The Landscape — Five Families

Everything marketed as an "AI video tool" falls into one of five families, each with its own model architecture and its own failure modes:

| Family | Core operation | Where it fails | Example tools |
|--------|---------------|----------------|---------------|
| **Identity manipulation** | Replacing or animating who appears in existing footage | Identity drift over time, mouth artifacts | Deep-Live-Cam, FaceFusion, Rope, SimSwap |
| **Generative video** | Creating footage that never existed from text/images | Temporal consistency (warping, morphing), physics | Veo, Kling, Seedance, Runway Gen, Wan, HunyuanVideo |
| **Talking heads / avatars** | Synchronizing speech and a portrait | Lip leakage, uncanny stiffness | OmniHuman, Wav2Lip, LivePortrait, SadTalker, HeyGen |
| **Editing & enhancement** | Modifying or improving real footage (repair, retime, upscale) | Flicker between frames — edits must be temporally stabilized | Runway Aleph, RIFE, Topaz Video AI, ProPainter |
| **Video understanding** | Machines *reading* video (index, summarize, moderate) | Grounding, long-context memory | Twelve Labs, VideoChat, InternVideo |

The dividing line between families is *who the frames are for*. Manipulation and editing start from existing frames; generation and avatars produce frames from other modalities (text, images, audio). Understanding does the reverse: it collapses video into text/metadata.

---

## 2. Face Swap & Identity Manipulation

### 2.1 The Concept

Deepfake-era research split into two approaches, and the tools below differ mainly in which they use:

1. **One-shot inference swap** — a network (InsightFace's `inswapper_128`) trained on large face-corpus data maps one identity onto another *in a single forward pass per frame*. No per-person training needed, which is what makes real-time webcam use feasible — but at fixed resolution (128px, hence the enhancement stage that follows).
2. **Training-based (GAN/autoencoder) reconstruction** — classic tools (DeepFaceLab, FaceSwap) learn a shared latent space between two identities over hours of training. Higher ceiling on quality, but realtime is impossible and setup is slow.

Either way, the frame pipeline is the same shape:

```
detect + align face (SCRFD/retinaface detector)
   → swap/model the identity   (inswapper or trained encoder/decoder)
   → enhance (GFPGAN / CodeFormer)   ← fixes the low-res swap output
   → mask + recomposite        ← blend face back with lighting/occlusion
   → repeat every frame        ← temporal consistency is the hard part
```

Mouth-region masking and occlusion masks exist because the two steps each fail differently: the swap erases the target's facial expression, and the enhancer can bleed detail outside the face region.

### 2.2 Examples

| Tool | Approach | Positioning |
|------|----------|-------------|
| **[Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam)** | One-shot (inswapper) + GUI | The reference for **real-time** webcam swapping; see §7 |
| **[FaceFusion](https://github.com/facefusion/facefusion)** | Extended one-shot pipeline, CLI-first | Actively maintained power-user fork lineage of roop — more processors (frame enhancement, lip syncer), more mask variants |
| **[Rope](https://github.com/Hillobar/Rope)** | One-shot, GUI | Video-file focused batch swapping |
| **[SimSwap](https://github.com/neuralchen/SimSwap)** | Research (ACID architecture) | Higher-id-fidelity academic baseline, not realtime |
| **DeepFaceLab / FaceSwap** | Training-based | The pre-realtime classics quality ceiling route |
| **Reface, Akool** | Commercial SaaS | Consumer apps — same ideas, hosted, paid |

### 2.3 Real-Time Operation (applies to the whole family)

Runtime is bound by the execution backend — all of the one-shot tools above are Python/ONNX-based and expose an execution-provider switch (`cuda`, `rocm`, `coreml`, `directml`, `cpu`). Real-time preview is a GPU phenomenon: consumer-class cards run ~10–30 FPS, CPU-only runs at slide-show speed. To feed calls/apps, the output goes through a virtual camera (OBS Virtual Camera, or Linux `v4l2loopback`).

---

## 3. Generative Video — Text/Image-to-Video

### 3.1 The Concept

Instead of moving pixels from existing frames, generative video models *denoise noise into footage*. The dominant recipe is latent diffusion extended to time:

```
text/image prompt → conditioning embeddings
   → iterative denoising of a spatio-temporal latent tensor
      (spatial UNet or DiT + temporal attention layers)
   → video VAE decoder → frames
```

Two properties define where this family stands:

- **Temporal consistency is the core failure mode.** Naive per-frame generation produces temporal *boil* and morphing faces. Every model below spends most of its engineering on cross-frame attention, 3D/joint VAEs, or autoregressive continuation so that objects persist and physics roughly holds — and modern benchmarks ([VBench](https://github.com/Vchitect/VBench)) score exactly this.
- **Compute scales steeply with duration and resolution.** A 5-second clip costs as much generation time as dozens of image generations; practical length is pushed out by specialized tricks (see FramePack below) rather than bigger models alone.

The field's 2025–2026 state has four visible trend lines, all developments verified against primary sources:

- **Audio-native generation** — Veo 3 (May 2025; Veo 3.1 since Oct 2025) generates synchronized dialogue, sound effects, and ambient audio with the picture; Kling 3.0-era models followed, and open research explores the same space (MOVA).
- **Editing became in-context** — editing moved from "regenerate the clip" to *video-in → edited-set video-out* on one model (Runway Aleph, July 2025, now Aleph 2.0 — see §5).
- **Real-time / interactive generation** — autoregressive next-frame chaining (MAGI-1, FramePack, SkyReels-V2) reached minute-scale real-time: Helios (built on Wan2.1) reports ~19.5 FPS generation on a single H100; Causal Forcing targets interactive speed.
- **Open weights caught up** — Wan2.2 (Apache-2.0) introduced MoE denoising (27B total, 14B active per step) and a 5B model rendering 720P@24fps on a single RTX 4090; HunyuanVideo-1.5 (8.3B, 14 GB VRAM floor) ships step-distilled 480p in ~75 s on a 4090. Benchmarks evolved too: VBench 2.0 scores *intrinsic faithfulness* — physics and consistency, not just prettiness.

### 3.2 Examples

**Commercial (October 2026 state, verified):**

| Model | Notable |
|-------|---------|
| **Veo 3.1 + Google Flow** (Google DeepMind) | Native synchronized audio; Flow is the movie-editor shell with scene continuity (~8 s clips); exposure via Gemini API, plus **Gemini Omni Flash** for fast generation and conversational multi-turn editing |
| **Kling 3.0** (Kuaishou) | Strong motion dynamics; ranked above Sora 2 Pro on the Artificial Analysis leaderboard in 2026 |
| **Seedance 2.0** (ByteDance) | Tops the 2026 video generation leaderboards |
| **Runway Gen-4.5 / Aleph 2.0** | Editing suite with in-context editing (see §5); Act-Two (performance capture), Solaris, GWM Worlds (world simulation) |
| **Luma Dream Machine, Pika, Hailuo** (MiniMax) | Consumer-facing fast-iteration players |

> **Volatility lesson — Sora:** previewed Feb 2024, launched Dec 2024 for ChatGPT Plus/Pro; its Sora 2 release (Sept 2025) was a TikTok-style social app with cameos and native audio — then OpenAI announced discontinuation in March 2026 (app shut April 26, API shut Sept 24, 2026). Video models churn faster than almost any other AI category: never hard-couple an application to a single provider's model endpoint.

> **Provenance:** major hosted models ship authorship signals — moving watermarks (Sora 2's could be removed by third-party tools within a week) and **C2PA content credentials** (Runway publishes a [verification page](https://runwayml.com/safety/verify)). Treat watermark/C2PA removal as the compliance red line it is.

**Open source (weights + code on GitHub/Hugging Face):**

| Model | Positioning |
|-------|-------------|
| **[Wan 2.2](https://github.com/Wan-Video/Wan2.2)** (Alibaba, Apache-2.0) | The heavyweight: MoE T2V/I2V-A14B (27B params, 14B active per step — high-noise and low-noise expert denoisers) and a high-compression TI2V-5B doing 720P@24fps on one RTX 4090; also S2V-14B (speech-driven video) and Animate-14B (character animation/replacement) |
| **[HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5)** (Tencent, Nov 2025) | The lightweight: 8.3B DiT + 3D causal VAE, 14 GB VRAM floor with offloading, SSTA sparse attention, built-in 1080p super-resolution network; step-distilled 480p I2V ≈ 75 s on a single 4090; training code + LoRA tuning included |
| **LTX-Video** (Lightricks) | Speed-first open family; distilled variants approach real-time |
| **Mochi 1** (Genmo) | Apache-2.0 base model |
| **CogVideoX / Open-Sora 2.0** | Long-established open lineages |
| **Stable Video Diffusion** | Image-to-video ancestor, still used for animation tasks |
| **FramePack** | Long-video generation on modest VRAM |
| **SkyReels-V2** (Skywork) | "Infinite-length" diffusion-forcing chaining |

**The glue layer** — most people don't invoke model repos directly:

- **[ComfyUI](https://github.com/comfyanonymous/ComfyUI)** — node-graph UI, the de-facto orchestration layer for chaining VAE/conditioners/upscalers
- **[DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio)** / **[FastVideo](https://github.com/hao-ai-lab/FastVideo)** / **[LightX2V](https://github.com/ModelTC/LightX2V)** — frameworks packaging training plus accelerated (step-distilled, sparse-attention, cache-based) inference for the models above
- Hosted APIs (Replicate, fal.ai, Runway API) wrap the commercial models for programmatic use

---

## 4. Talking Heads & Avatars

### 4.1 The Concept

Same skeleton as §2 — animate a portrait — but driven by *audio or a driving video* rather than another face. Four sub-approaches define the family:

1. **Landmark conditioning** — detect facial landmarks from the audio/gesture source, render the face to hit them (SadTalker, EchoMimic) — robust but sometimes stiff.
2. **Driving-video retargeting** — take my performance on video, retarget the motion (and expression) onto a still image in real time (LivePortrait) — the streaming-vtuber approach.
3. **Full diffusion synthesis** — let a video diffusion model generate head/mouth/body dynamics conditioned on audio (Hallo3, MEMO, MoCha) — highest ceiling, still heavy.
4. **Pure 2D lip-sync repair** — leave the video untouched; regenerate only the mouth region so speech matches its audio (Wav2Lip classic; KeySync research fixes leakage) — the dubbing path.

### 4.2 Examples

| Tool | Approach |
|------|----------|
| **[Wav2Lip](https://github.com/Rudrabha/Wav2Lip)** | Classic mouth-only sync — the original dubbing baseline |
| **[LivePortrait](https://github.com/KwaiVGI/LivePortrait)** | Real-time driving-video retargeting (Kuaishou) |
| **SadTalker / EchoMimic / Hallo3 / MEMO** | Audio-driven portrait animation, open research lineage |
| **KeySync** | Leakage-free high-res lip sync research |
| **OmniHuman-1** (ByteDance) | One image + audio → *full-body* human video; the scaling milestone of this family |
| **Wan2.2-Animate-14B** | Character animation *and* replacement from a driving video — animate mode mimics a performer's motion/expression, replace mode inserts your character into footage |
| **HunyuanPortrait** | Implicit condition control for portrait animation (2025 research) |
| **HeyGen, Synthesia, D-ID** | Commercial hosted avatars: script in -> presenter video out (translate/dub built on the lip-sync approach) |

---

## 5. Editing, Enhancement & Restoration

### 5.1 The Concept

These models modify frames you already have — the family the classic NLE (DaVinci, Premiere) increasingly re-implements in-house. What distinguishes AI-native editing from per-filter processing:

- **Instruction-driven editing** — "make it snow", "change the outfit": a diffusion model re-synthesizes the region while holding the rest (VACE, UniVideo, Runway's editing tools).
- **Temporal stabilization is mandatory.** A per-frame edit flickers — each edit model carries some cross-frame attention or propagation (optical-flow-based methods like ProPainter) to hold the result consistent across frames.
- **Restoration is frame-consistent super-resolution/denoise** — upscalers built for stills produce shimmering on video, so video-specialized variants (RIFE-style or trained-sequential) exist. Classical algebra runs the other direction too — interpolation nets (RIFE, Google FILM) invent missing in-between frames to retime slow footage to 60fps.

### 5.2 Examples

| Task | Tools |
|------|-------|
| **Upscaling/restoration** | Topaz Video AI (commercial), GFPGAN/CodeFormer for faces, Real-ESRGAN pipelines — see [Image Upscalers](../media/image-upscalers.md) for the still-image versions |
| **Frame interpolation (retime)** | RIFE, FILM |
| **In-context editing (one model, many edits)** | **Runway Aleph / Aleph 2.0** — add/remove/transform objects, re-light, re-style, regenerate any camera angle from one input clip; open analog: OmniWeaving (video-to-video editing built on HunyuanVideo-1.5) |
| **Inpainting & object removal** | ProPainter, VideoPainter (any-length inpainting), MiniMax-Remover, Premiere generative features |
| **Camera control** | ReCamMaster — re-shoot one source video along any camera path |
| **Relighting** | RelightVid, TC-Light (temporally-consistent world transfer) |
| **In-app AI features** | CapCut, Premiere Pro, Descript (edit-by-transcript) — see [Creative Software](../media/creative-software.md) |

---

## 6. Video Understanding & Analysis

The reverse of everything above: models that *compress* video into text/structured data — used for search, tagging, moderation, and highlight extraction. These sit behind the scenes of most video platforms rather than in creator workflows.

| Approach | Examples |
|----------|----------|
| **Commercial video-understanding APIs** | Twelve Labs (semantic video search), Google Video Intelligence + Gemini's native multimodal video understanding, AWS Rekognition Video (objects/faces/moderation) |
| **Speech-in-video** | AssemblyAI, Whisper — transcription that feeds editing (Descript) workflows |
| **Open research models** | [VideoChat-Flash](https://github.com/OpenGVLab/VideoChat-Flash) (long-context video conversation), [InternVideo](https://github.com/OpenGVLab/InternVideo) |
| **Retrieval over long video** | VideoRAG — retrieval-augmented generation with extreme long-context videos |
| **Evaluation research** | VBench 2.0 (intrinsic-faithfulness scoring: physics, consistency), VideoScore2 (think-then-score MLLM judge), Stable Cinemetrics (professional cinematography taxonomy) |

> **Note:** A previously listed tool, `ruvnet/RuView`, turned out to be a WiFi-sensing platform (presence detection via RF signals, not video). It is not a video-analysis tool and has been removed.

---

## 7. Worked Example — Deep-Live-Cam

The best way to grasp family #2 is to run it. Deep-Live-Cam is the reference real-time implementation: one source photo, live webcam output, built on InsightFace's one-shot inswapper plus a GFPGAN enhancer — descended from `s0md3v/roop`.

- **Repository:** https://github.com/hacksider/Deep-Live-Cam (AGPL-3.0; ~97k stars)
- **License nuance:** the *code* is AGPL-3.0 — the non-commercial restriction lives on the **inswapper model weights** (InsightFace's research-only terms)
- **Prebuilt binaries** (paid "Ultimate" build): https://deeplivecam.net — the source version below is free

### 7.1 Requirements

```
Python 3.10
GPU strongly recommended:
  NVIDIA:  CUDA 11.8+ (onnxruntime-gpu)
  Apple:   CoreML backend
  Windows: DirectML alternative
CPU-only works but is very slow (~1–3 FPS)
RAM 8 GB min / 16 GB recommended · VRAM 4 GB+
```

### 7.2 Install & Run

```bash
git clone https://github.com/hacksider/Deep-Live-Cam.git
cd Deep-Live-Cam
python -m venv venv && source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Models auto-download on first run into ./models/ (or grab from
# https://huggingface.co/hacksider/deep-live-cam):
#   inswapper_128_fp16.onnx (~256 MB)
#   GFPGANv1.4.pth (~332 MB)

python run.py     # GUI: select face image → select target (video/webcam) → Live
```

With the GUI: **Select a face** → one clear photo; **Live** starts real-time preview after a 10–30s warm-up; switch the source image to switch identity mid-stream. For OBS/streaming, capture the preview window and output via OBS Virtual Camera.

```bash
# Useful runtime switches:
--mouth-mask                 # preserve the target's real mouth (expression integrity)
--many-faces                 # swap every detected face, not just the first
--map-faces                  # separate source identity per target face (multi-person)
--frame-processor face_swapper face_enhancer   # chain the GFPGAN restoration stage
--execution-provider cuda    # or coreml / directml / rocm / cpu
--video-encoder libx264 --video-quality 14
```

The upstream CLI is marked **unmaintained** — GUI-first is the supported path; for scripting other tools, FaceFusion's CLI is the actively maintained alternative.

### 7.3 Performance Targets (reported approximations)

| Hardware | Live FPS |
|----------|---------|
| RTX 4090 | ~30 |
| RTX 3080 / M2 Pro | ~15–20 |
| RTX 3060 / M1 | ~8–12 |
| CPU only | 1–3 |

### 7.4 Networking It Into an App

The virtual-camera loop is generic across the family:

```bash
# Linux: v4l2loopback makes OBS's or any app's output appear as /dev/video*
sudo apt install v4l2loopback-dkms && sudo modprobe v4l2loopback
# macOS/Windows: OBS Virtual Camera (built-in) or CamTwist/ManyCam
# Path: SW window → OBS window-capture → OBS Virtual Camera → Zoom/Meet/Recorder
```

---

## 8. Choosing Tools

| If you need… | Reach for |
|--------------|-----------|
| Live identity swap in calls/streaming | Deep-Live-Cam (GUI) or FaceFusion (scripting) |
| Batch face swap in files, offline | Rope or FaceFusion |
| Highest-quality identity swap when training time is acceptable | DeepFaceLab-class training-based tools |
| Original footage from a script/storyboard | Veo/Kling/Seedance/Runway (hosted) or Wan 2.2/HunyuanVideo-1.5 (local) |
| Local video generation on a modest GPU | HunyuanVideo-1.5 (8.3B, 14 GB VRAM) · Wan TI2V-5B (4090-ready) · FramePack |
| Talking presenter from a script | HeyGen/Synthesia (hosted) or SadTalker/Hallo3-class (local) |
| Verify dubbed content matches audio | Wav2Lip-style mouth-region sync models |
| Repair/upscale/retime real footage | Topaz Video AI / RIFE / ProPainter |
| Edit existing footage by instruction | Runway Aleph (hosted) / VACE-class or OmniWeaving (open) |
| Search or audit video libraries programmatically | Twelve Labs class APIs, or InternVideo-type models |

---

## 9. See Also

- [Platforms & APIs](platforms-and-apis.md) — hosted inference (Ollama, Replicate, Hugging Face) for the models above
- [Image Upscalers](../media/image-upscalers.md) — the still-image siblings of the restoration models
- [Creative Software](../media/creative-software.md) — how the editing family is embedded in CapCut/Resolve/Premiere
- [Media Tools](../media/media-tools.md) — FFmpeg: always the final packaging step after any AI pipeline
