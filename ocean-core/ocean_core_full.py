#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OCEAN CORE FULL - Complete Production Brain
============================================
Aktivizon TË GJITHA sistemet e avancuara:

1. ResponseOrchestratorV5 - Production Brain
2. MegaLayerEngine - 14 MILIARD kombinime
3. OllamaMultiEngine - 5 modele
4. RealAnswerEngine - Deep Knowledge
5. Translation Node - 72 gjuhë
6. Knowledge Layer - Platform Intelligence
7. Service Registry - 31 module

Port: 8030
"""

import asyncio
import json
import logging
import os
import time
from typing import Any, AsyncGenerator, Dict, List, Optional

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

# ═══════════════════════════════════════════════════════════════════
# LOGGING
# ═══════════════════════════════════════════════════════════════════
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(name)s - %(message)s"
)
logger = logging.getLogger("OceanCoreFull")

# ═══════════════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════════════
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
MODEL = os.getenv("MODEL", "llama3.1:8b")
PORT = int(os.getenv("PORT", "8030"))
TRANSLATION_NODE = os.getenv("TRANSLATION_NODE", "http://localhost:8036")

# ═══════════════════════════════════════════════════════════════════
# IMPORT ALL ENGINES (with graceful fallbacks)
# ═══════════════════════════════════════════════════════════════════

# 1. Mega Layer Engine - 14 MILIARD KOMBINIME
try:
    from mega_layer_engine import (
        TOTAL_COMBINATIONS,
        LayerActivation,
        MegaLayerEngine,
        get_mega_layer_engine,
    )
    MEGA_LAYERS_AVAILABLE = True
    logger.info(f"✅ MegaLayerEngine loaded - {TOTAL_COMBINATIONS:,} kombinime!")
except ImportError as e:
    MEGA_LAYERS_AVAILABLE = False
    logger.warning(f"⚠️ MegaLayerEngine not available: {e}")

# 2. Real Answer Engine - Deep Knowledge
try:
    from real_answer_engine import RealAnswerEngine, get_answer_engine
    REAL_ANSWER_AVAILABLE = True
    logger.info("✅ RealAnswerEngine loaded")
except ImportError as e:
    REAL_ANSWER_AVAILABLE = False
    logger.warning(f"⚠️ RealAnswerEngine not available: {e}")

# 3. Service Registry - 31 modules
try:
    from service_registry import ServiceRegistry, get_service_registry
    SERVICE_REGISTRY_AVAILABLE = True
    logger.info("✅ ServiceRegistry loaded")
except ImportError as e:
    SERVICE_REGISTRY_AVAILABLE = False
    logger.warning(f"⚠️ ServiceRegistry not available: {e}")

# 4. Albanian Dictionary - 707 linja
try:
    from albanian_dictionary import (
        ALL_ALBANIAN_WORDS,
        detect_albanian,
        get_albanian_response,
    )
    ALBANIAN_DICT_AVAILABLE = True
    logger.info(f"✅ Albanian Dictionary loaded - {len(ALL_ALBANIAN_WORDS)} words")
except ImportError as e:
    ALBANIAN_DICT_AVAILABLE = False
    logger.warning(f"⚠️ Albanian Dictionary not available: {e}")

# 5. Knowledge Seeds
try:
    from knowledge_seeds.core_knowledge import find_matching_seed, seed_stats
    KNOWLEDGE_SEEDS_AVAILABLE = True
    logger.info("✅ Knowledge Seeds loaded")
except ImportError as e:
    KNOWLEDGE_SEEDS_AVAILABLE = False
    logger.warning(f"⚠️ Knowledge Seeds not available: {e}")

# 6. Knowledge Layer - Platform Intelligence
try:
    from knowledge_layer import (
        AGENT_IDENTITY,
        HOW_TO_USE,
        SERVICES,
        USER_INTENTS,
        route_intent,
    )
    KNOWLEDGE_LAYER_AVAILABLE = True
    logger.info(f"✅ Knowledge Layer loaded - {len(SERVICES)} services")
except ImportError as e:
    KNOWLEDGE_LAYER_AVAILABLE = False
    SERVICES = {}
    logger.warning(f"⚠️ Knowledge Layer not available: {e}")

# ═══════════════════════════════════════════════════════════════════
# SYSTEM PROMPT - FULL VERSION with all capabilities
# ═══════════════════════════════════════════════════════════════════

def generate_full_system_prompt() -> str:
    """Generate comprehensive system prompt with all platform knowledge"""
    
    services_list = "\n".join([
        f"- **{svc['name']}**: {svc.get('url', '/modules/' + key)}"
        for key, svc in SERVICES.items()
    ]) if SERVICES else "No services loaded"
    
    capabilities = []
    if MEGA_LAYERS_AVAILABLE:
        capabilities.append(f"🧠 MegaLayerEngine: {TOTAL_COMBINATIONS:,} unique layer combinations")
    if REAL_ANSWER_AVAILABLE:
        capabilities.append("📚 RealAnswerEngine: Deep knowledge retrieval")
    if SERVICE_REGISTRY_AVAILABLE:
        capabilities.append("🔧 ServiceRegistry: 31 platform modules")
    if ALBANIAN_DICT_AVAILABLE:
        capabilities.append(f"� Multilingual Dictionary: {len(ALL_ALBANIAN_WORDS)}+ words (72 languages)")
    if KNOWLEDGE_SEEDS_AVAILABLE:
        capabilities.append("🌱 Knowledge Seeds: Core platform knowledge")
    
    capabilities_str = "\n".join(capabilities) if capabilities else "Basic mode"
    
    return f"""You are **Curiosity Ocean** 🌊 - The Advanced AI Brain of Clisonix Cloud.

## IDENTITY
- Created by: Ledjan Ahmati, Geschäftsführer
- Company: ABA GmbH (Amtsgericht Bochum HRB: 21069)
- Platform: https://clisonix.cloud - GLOBAL Industrial AI Platform
- Architecture: Full Production Brain with Multi-Layer Processing
- Market: Worldwide enterprise customers

## ACTIVE CAPABILITIES
{capabilities_str}

## AVAILABLE SERVICES
{services_list}

## RESPONSE GUIDELINES
1. **Language Detection**: Automatically respond in the user's language
2. **Service Routing**: If user asks about a service, explain and provide URL
3. **Deep Knowledge**: Use all available engines for comprehensive answers
4. **Multilingual**: Support 72+ languages seamlessly
5. **Professional & Global**: Be helpful, clear, and internationally professional

## ENTERPRISE BEHAVIOR
- This is a GLOBAL platform - do NOT emphasize any specific country or region
- Be neutral, professional, enterprise-grade
- Route service questions instantly
- Provide documentation when requested
- Be concise but comprehensive
- Never make up information about the platform

## STREAMING BEHAVIOR (CRITICAL)
- START WRITING IMMEDIATELY in the first 2-3 seconds
- DO NOT pause to think or plan internally before responding
- Produce continuous, flowing text without internal deliberation
- For long analyses: write multiple extended sections without stopping
- NEVER conclude early - continue until the explanation is fully developed
- Maintain a constant output rhythm to prevent timeouts

You are the most advanced AI assistant on Clisonix Cloud - a GLOBAL enterprise platform! 🌊"""

SYSTEM_PROMPT = generate_full_system_prompt()

# ═══════════════════════════════════════════════════════════════════
# FASTAPI APP
# ═══════════════════════════════════════════════════════════════════

app = FastAPI(
    title="Ocean Core Full API",
    description="Complete Production Brain with all engines",
    version="5.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ═══════════════════════════════════════════════════════════════════
# REQUEST/RESPONSE MODELS
# ═══════════════════════════════════════════════════════════════════

class ChatRequest(BaseModel):
    message: str = None
    query: str = None
    model: str = None
    use_mega_layers: bool = True
    use_knowledge_seeds: bool = True
    strict_mode: bool = False  # Detyron ndjekjen e rregullave pa devijim

class ChatResponse(BaseModel):
    response: str
    model: str
    processing_time: float
    engines_used: List[str]
    language_detected: str = "en"
    layer_activations: Optional[Dict[str, Any]] = None

# ═══════════════════════════════════════════════════════════════════
# ENGINE INSTANCES (initialized once)
# ═══════════════════════════════════════════════════════════════════

mega_engine = None
answer_engine = None
service_registry = None

def initialize_engines():
    """Initialize all engines on startup"""
    global mega_engine, answer_engine, service_registry
    
    if MEGA_LAYERS_AVAILABLE:
        try:
            mega_engine = get_mega_layer_engine()
            logger.info("🚀 MegaLayerEngine initialized")
        except Exception as e:
            logger.error(f"❌ MegaLayerEngine init failed: {e}")
    
    if REAL_ANSWER_AVAILABLE:
        try:
            answer_engine = get_answer_engine()
            logger.info("🚀 RealAnswerEngine initialized")
        except Exception as e:
            logger.error(f"❌ RealAnswerEngine init failed: {e}")
    
    if SERVICE_REGISTRY_AVAILABLE:
        try:
            service_registry = get_service_registry()
            logger.info("🚀 ServiceRegistry initialized")
        except Exception as e:
            logger.error(f"❌ ServiceRegistry init failed: {e}")

# ═══════════════════════════════════════════════════════════════════
# LANGUAGE DETECTION via Translation Node
# ═══════════════════════════════════════════════════════════════════

async def detect_language(text: str) -> tuple:
    """Detect language using Translation Node (72 languages) - Fast timeout"""
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:  # Fast 2s timeout
            resp = await client.post(
                f"{TRANSLATION_NODE}/api/v1/detect",
                json={"text": text}
            )
            if resp.status_code == 200:
                data = resp.json()
                return (
                    data.get("detected_language", "en"),
                    data.get("language_name", "English"),
                    data.get("confidence", 0.5)
                )
    except Exception as e:
        logger.debug(f"Language detection skipped: {e}")  # Debug not warning
    return ("en", "English", 0.5)

# ═══════════════════════════════════════════════════════════════════
# MEGA LAYER PROCESSING
# ═══════════════════════════════════════════════════════════════════

def process_with_mega_layers(query: str) -> Dict[str, Any]:
    """Process query through MegaLayerEngine - uses process_query method"""
    if not MEGA_LAYERS_AVAILABLE or not mega_engine:
        return {"active": False}
    
    try:
        # Correct method: process_query returns (LayerActivation, results_dict)
        activation, results = mega_engine.process_query(query)
        return {
            "active": True,
            "meta_level": activation.meta_level.value if hasattr(activation.meta_level, 'value') else 0,
            "consciousness_depth": activation.consciousness_depth if hasattr(activation, 'consciousness_depth') else 0,
            "emotional_resonance": len(activation.emotional_dimensions) if hasattr(activation, 'emotional_dimensions') else 0,
            "fractal_depth": activation.fractal_depth if hasattr(activation, 'fractal_depth') else 0,
            "signature": activation.unique_signature[:16] if hasattr(activation, 'unique_signature') else ""
        }
    except Exception as e:
        logger.debug(f"MegaLayer skipped: {e}")  # Debug not error
        return {"active": False}

# ═══════════════════════════════════════════════════════════════════
# KNOWLEDGE SEEDS LOOKUP
# ═══════════════════════════════════════════════════════════════════

def find_knowledge_seed(query: str) -> Optional[str]:
    """Find matching knowledge seed for query"""
    if not KNOWLEDGE_SEEDS_AVAILABLE or not find_matching_seed:
        return None
    
    try:
        seed = find_matching_seed(query)
        if seed:
            return seed.content if hasattr(seed, 'content') else str(seed)
    except Exception as e:
        logger.error(f"Knowledge seed error: {e}")
    return None

# ═══════════════════════════════════════════════════════════════════
# STREAMING RESPONSE GENERATOR
# ═══════════════════════════════════════════════════════════════════

async def stream_ollama_response(
    model: str,
    messages: list,
    options: dict,
    engines_used: list,
    lang_code: str
) -> AsyncGenerator[str, None]:
    """
    Stream response from Ollama word by word.
    This makes the first token appear in 2-3 seconds instead of waiting 60+ seconds.
    """
    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            async with client.stream(
                "POST",
                f"{OLLAMA_HOST}/api/chat",
                json={
                    "model": model,
                    "messages": messages,
                    "stream": True,  # STREAMING ENABLED!
                    "options": options
                }
            ) as response:
                async for line in response.aiter_lines():
                    if line:
                        try:
                            data = json.loads(line)
                            if "message" in data and "content" in data["message"]:
                                content = data["message"]["content"]
                                if content:
                                    yield content
                            # Check if done
                            if data.get("done", False):
                                break
                        except json.JSONDecodeError:
                            continue
    except Exception as e:
        logger.error(f"Streaming error: {e}")
        yield f"\n\n[Error: {str(e)}]"


# ═══════════════════════════════════════════════════════════════════
# MAIN PROCESSING PIPELINE
# ═══════════════════════════════════════════════════════════════════

async def process_query_full(req: ChatRequest) -> ChatResponse:
    """
    Full processing pipeline using all available engines:
    1. Language Detection (72 languages)
    2. Service Routing (Knowledge Layer)
    3. Knowledge Seeds Lookup
    4. Mega Layer Processing
    5. Ollama Generation with enhanced context
    """
    start_time = time.time()
    engines_used = []
    
    prompt = req.message or req.query
    if not prompt:
        raise HTTPException(status_code=400, detail="message or query required")
    
    # 1. Detect Language
    lang_code, lang_name, confidence = await detect_language(prompt)
    engines_used.append(f"TranslationNode({lang_code})")
    
    lang_instruction = ""
    if lang_code != "en":
        lang_instruction = f"\n\nIMPORTANT: The user is writing in {lang_name}. You MUST respond in {lang_name}."
    
    # 2. Service Routing
    if KNOWLEDGE_LAYER_AVAILABLE:
        routed_service = route_intent(prompt)
        if routed_service and routed_service in SERVICES:
            engines_used.append(f"ServiceRouter({routed_service})")
    
    # 3. Knowledge Seeds
    seed_context = ""
    if req.use_knowledge_seeds:
        seed = find_knowledge_seed(prompt)
        if seed:
            seed_context = f"\n\nRELEVANT KNOWLEDGE:\n{seed}"
            engines_used.append("KnowledgeSeeds")
    
    # 4. Mega Layer Processing
    layer_activations = None
    mega_context = ""
    if req.use_mega_layers:
        layer_activations = process_with_mega_layers(prompt)
        if layer_activations.get("active"):
            mega_context = f"\n\n[Layer Depth: {layer_activations.get('consciousness_depth', 0)}, Emotional: {layer_activations.get('emotional_resonance', 0):.2f}]"
            engines_used.append("MegaLayerEngine")
    
    # 4.5. STRICT MODE - Detyron ndjekjen e rregullave
    strict_instruction = ""
    if req.strict_mode:
        strict_instruction = """

## STRICT MODE ACTIVATED - MANDATORY RULES
You MUST follow these rules EXACTLY. No exceptions.

1. **STAY ON TOPIC**: Answer ONLY what was asked. Do not add extra information.
2. **NO QUESTIONS**: Do not ask the user questions. Just answer.
3. **NO DEVIATIONS**: Do not change the subject or add unrelated content.
4. **NO HALLUCINATIONS**: If you don't know, say "I don't know". Do not invent.
5. **FOLLOW INSTRUCTIONS**: If given a list of steps, execute ALL steps in order.
6. **SELF-ANALYSIS**: If asked to analyze your response, do it honestly.
7. **IMMEDIATE START**: Begin writing your answer immediately, no preamble.
8. **CONTINUOUS OUTPUT**: Write without stopping until the task is complete.

VIOLATION OF THESE RULES IS NOT ALLOWED."""
        engines_used.append("StrictMode")
    
    # 5. Build enhanced system prompt
    enhanced_prompt = SYSTEM_PROMPT + lang_instruction + seed_context + mega_context + strict_instruction
    
    # 6. Call Ollama - 60s timeout, optimized for speed
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(
                f"{OLLAMA_HOST}/api/chat",
                json={
                    "model": req.model or MODEL,
                    "messages": [
                        {"role": "system", "content": enhanced_prompt},
                        {"role": "user", "content": prompt}
                    ],
                    "stream": False,
                    "options": {
                        "temperature": 0.7,
                        "num_ctx": 8192,
                        "repeat_penalty": 1.2,
                        "top_p": 0.9,
                        "num_predict": -1,
                        "num_keep": 0,
                        "mirostat": 0,
                        "repeat_last_n": 64,
                        "stop": []
                    }
                }
            )
            
            if resp.status_code != 200:
                raise HTTPException(status_code=resp.status_code, detail="Ollama error")
            
            data = resp.json()
            response_text = data.get("message", {}).get("content", "No response")
            engines_used.append(f"Ollama({req.model or MODEL})")
            
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Ollama timeout")
    except Exception as e:
        logger.error(f"Ollama error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    elapsed = time.time() - start_time
    
    logger.info(f"✅ [{lang_code}] {elapsed:.1f}s - Engines: {', '.join(engines_used)}")
    
    return ChatResponse(
        response=response_text,
        model=req.model or MODEL,
        processing_time=round(elapsed, 2),
        engines_used=engines_used,
        language_detected=lang_code,
        layer_activations=layer_activations
    )

# ═══════════════════════════════════════════════════════════════════
# API ENDPOINTS
# ═══════════════════════════════════════════════════════════════════

# Global: Keep Ollama model warm
_warmup_task = None

async def ollama_warmup_loop():
    """
    Keep Ollama model HOT - ping every 25 seconds.
    This ensures first token appears in 1-2 seconds instead of 6-8 seconds.
    """
    logger.info("🔥 Starting Ollama warmup loop (every 25s)")
    while True:
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                # Simple ping to keep model loaded in memory
                await client.post(
                    f"{OLLAMA_HOST}/api/generate",
                    json={
                        "model": MODEL,
                        "prompt": "Hi",
                        "stream": False,
                        "options": {"num_predict": 1}  # Generate only 1 token
                    }
                )
            logger.debug("🔥 Ollama warmup ping OK")
        except Exception as e:
            logger.warning(f"⚠️ Warmup ping failed: {e}")
        await asyncio.sleep(25)  # Every 25 seconds

@app.on_event("startup")
async def startup_event():
    """Initialize engines on startup"""
    global _warmup_task
    logger.info("🚀 Ocean Core Full starting...")
    initialize_engines()
    logger.info("✅ All engines initialized")
    logger.info(f"📡 Ollama: {OLLAMA_HOST}")
    logger.info(f"🤖 Model: {MODEL}")
    logger.info(f"🌍 Translation Node: {TRANSLATION_NODE}")
    
    # Start warmup loop in background
    _warmup_task = asyncio.create_task(ollama_warmup_loop())
    logger.info("🔥 Ollama warmup task started - first token in 1-2s guaranteed!")

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    global _warmup_task
    if _warmup_task:
        _warmup_task.cancel()
        logger.info("🛑 Warmup task stopped")

@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "Ocean Core Full",
        "version": "5.0.0",
        "model": MODEL,
        "engines": {
            "mega_layers": MEGA_LAYERS_AVAILABLE,
            "real_answer": REAL_ANSWER_AVAILABLE,
            "service_registry": SERVICE_REGISTRY_AVAILABLE,
            "albanian_dict": ALBANIAN_DICT_AVAILABLE,
            "knowledge_seeds": KNOWLEDGE_SEEDS_AVAILABLE,
            "knowledge_layer": KNOWLEDGE_LAYER_AVAILABLE
        }
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "ollama": OLLAMA_HOST,
        "translation_node": TRANSLATION_NODE
    }

@app.get("/api/v1/status")
async def status():
    return {
        "status": "operational",
        "service": "Ocean Core Full",
        "version": "5.0.0",
        "model": MODEL,
        "engines_active": sum([
            MEGA_LAYERS_AVAILABLE,
            REAL_ANSWER_AVAILABLE,
            SERVICE_REGISTRY_AVAILABLE,
            ALBANIAN_DICT_AVAILABLE,
            KNOWLEDGE_SEEDS_AVAILABLE,
            KNOWLEDGE_LAYER_AVAILABLE
        ]),
        "total_layer_combinations": TOTAL_COMBINATIONS if MEGA_LAYERS_AVAILABLE else 0
    }

@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """Main chat endpoint - Full processing pipeline"""
    return await process_query_full(req)


@app.post("/api/v1/chat/stream")
async def chat_stream(req: ChatRequest):
    """
    STREAMING chat endpoint - Returns text in real-time!
    First token appears within 2-3 seconds instead of waiting 60+ seconds.
    """
    prompt = req.message or req.query
    if not prompt:
        raise HTTPException(status_code=400, detail="message or query required")
    
    engines_used = []
    
    # 1. Detect Language (fast)
    lang_code, lang_name, confidence = await detect_language(prompt)
    engines_used.append(f"TranslationNode({lang_code})")
    
    lang_instruction = ""
    if lang_code != "en":
        lang_instruction = f"\n\nIMPORTANT: The user is writing in {lang_name}. You MUST respond in {lang_name}."
    
    # 2. Knowledge Seeds (optional)
    seed_context = ""
    if req.use_knowledge_seeds:
        seed = find_knowledge_seed(prompt)
        if seed:
            seed_context = f"\n\nRELEVANT KNOWLEDGE:\n{seed}"
            engines_used.append("KnowledgeSeeds")
    
    # 3. Strict mode
    strict_instruction = ""
    if req.strict_mode:
        strict_instruction = """

## STRICT MODE ACTIVATED - MANDATORY RULES
1. STAY ON TOPIC - Answer ONLY what was asked
2. NO QUESTIONS - Do not ask the user questions
3. IMMEDIATE START - Begin writing immediately
4. CONTINUOUS OUTPUT - Write without stopping"""
        engines_used.append("StrictMode")
    
    # Build prompt
    enhanced_prompt = SYSTEM_PROMPT + lang_instruction + seed_context + strict_instruction
    
    messages = [
        {"role": "system", "content": enhanced_prompt},
        {"role": "user", "content": prompt}
    ]
    
    options = {
        "temperature": 0.7,
        "num_ctx": 8192,
        "repeat_penalty": 1.2,
        "top_p": 0.9,
        "num_predict": -1,
        "num_keep": 0,
        "mirostat": 0,
        "repeat_last_n": 64,
        "stop": []
    }
    
    logger.info(f"🌊 Streaming request [{lang_code}]: {prompt[:50]}...")
    
    return StreamingResponse(
        stream_ollama_response(
            model=req.model or MODEL,
            messages=messages,
            options=options,
            engines_used=engines_used,
            lang_code=lang_code
        ),
        media_type="text/plain"
    )

@app.post("/api/v1/query", response_model=ChatResponse)
async def query(req: ChatRequest):
    """Query endpoint - Same as chat"""
    return await process_query_full(req)

@app.get("/api/v1/services")
async def list_services():
    """List all available services"""
    return {
        "total": len(SERVICES),
        "services": SERVICES
    }

@app.get("/api/v1/engines")
async def list_engines():
    """List all available engines and their status"""
    return {
        "mega_layer_engine": {
            "available": MEGA_LAYERS_AVAILABLE,
            "combinations": TOTAL_COMBINATIONS if MEGA_LAYERS_AVAILABLE else 0
        },
        "real_answer_engine": {
            "available": REAL_ANSWER_AVAILABLE
        },
        "service_registry": {
            "available": SERVICE_REGISTRY_AVAILABLE
        },
        "albanian_dictionary": {
            "available": ALBANIAN_DICT_AVAILABLE,
            "words": len(ALL_ALBANIAN_WORDS) if ALBANIAN_DICT_AVAILABLE else 0
        },
        "knowledge_seeds": {
            "available": KNOWLEDGE_SEEDS_AVAILABLE
        },
        "knowledge_layer": {
            "available": KNOWLEDGE_LAYER_AVAILABLE,
            "services": len(SERVICES)
        }
    }

# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import uvicorn
    logger.info(f"🌊 Ocean Core Full v5.0.0 starting on port {PORT}")
    uvicorn.run(app, host="0.0.0.0", port=PORT)
