"""
Indian Philosophy Chatbot - Complete Backend
Modern FastAPI implementation with knowledge base integration
No external API dependencies - 100% free and open-source
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from dotenv import load_dotenv
import os
import logging
from datetime import datetime
import json

# ============ CONFIGURE LOGGING ============
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============ LOAD ENVIRONMENT ============
load_dotenv()

# ============ IMPORT KNOWLEDGE BASE ============
from .knowledge_base import (
    INDIAN_PHILOSOPHY_KB,
    get_answer_by_key,
    get_all_questions,
    search_kb
)

# ============ INITIALIZE FASTAPI ============
app = FastAPI(
    title="Indian Philosophy Chatbot 🕉️",
    description="Advanced AI Chatbot on Indian Knowledge Systems with 3D Animated UI",
    version="1.0.0",
    docs_url="/docs",
    openapi_url="/openapi.json"
)

# ============ CORS CONFIGURATION ============
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================
# DATA MODELS
# ============================================

class Citation(BaseModel):
    """Citation model for sources"""
    source: str = Field(..., description="Source text or scripture")
    verse: Optional[str] = Field(None, description="Verse reference")
    text: str = Field(..., description="Citation text")
    meaning: Optional[str] = Field(None, description="Meaning of citation")
    context: Optional[str] = Field(None, description="Additional context")


class PhilosophyQuery(BaseModel):
    """User query model"""
    question: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="Philosophical question"
    )
    philosophical_tradition: Optional[str] = Field(
        "general",
        description="Specific tradition: vedanta, buddhism, yoga, samkhya, nyaya, mimamsa"
    )
    language: Optional[str] = Field("english", description="Response language")

    class Config:
        json_schema_extra = {
            "example": {
                "question": "What is the relationship between Atman and Brahman?",
                "philosophical_tradition": "vedanta",
                "language": "english"
            }
        }


class PhilosophyResponse(BaseModel):
    """Response model with citations"""
    answer: str = Field(..., description="Philosophical answer")
    tradition: str = Field(..., description="Philosophical tradition")
    citations: List[Citation] = Field(..., description="Source citations")
    confidence_score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence level of answer (0-1)"
    )
    source: Optional[str] = Field("Knowledge Base", description="Source of answer")
    method: Optional[str] = Field("Direct Match", description="How answer was generated")
    timestamp: Optional[str] = Field(None, description="Response timestamp")

    class Config:
        json_schema_extra = {
            "example": {
                "answer": "In Vedanta philosophy, Atman (individual soul)...",
                "tradition": "vedanta",
                "citations": [
                    {
                        "source": "Chandogya Upanishad",
                        "verse": "6.8.7",
                        "text": "Tat Tvam Asi",
                        "meaning": "Thou Art That"
                    }
                ],
                "confidence_score": 0.95,
                "source": "Knowledge Base (Verified)",
                "method": "Direct Match",
                "timestamp": "2024-01-15T10:30:00Z"
            }
        }


class SearchResult(BaseModel):
    """Search result model"""
    key: str
    question: str
    tradition: str
    match_score: float


class AllQuestionsResponse(BaseModel):
    """Response for all available questions"""
    total_questions: int
    traditions: List[str]
    questions: List[Dict]


class HealthCheckResponse(BaseModel):
    """Health check response"""
    status: str
    service: str
    version: str
    knowledge_base_size: int
    timestamp: str


# ============================================
# CORE LOGIC FUNCTIONS
# ============================================

def generate_philosophical_response(
    question: str,
    tradition: str = "general"
) -> Dict:
    """
    Generate response using knowledge base
    Handles exact matches, similar matches, and fallbacks
    
    Args:
        question: User's philosophical question
        tradition: Specific philosophical tradition (optional)
    
    Returns:
        Dictionary with answer, citations, confidence score
    """
    
    logger.info(f"Processing question: {question[:50]}... | Tradition: {tradition}")
    
    # Step 1: Search knowledge base for exact or similar match
    similar_answers = search_kb(question)
    
    if similar_answers:
        # Found relevant knowledge base entry
        kb_key = similar_answers[0]["key"]
        kb_data = get_answer_by_key(kb_key)
        
        logger.info(f"Knowledge Base Match Found: {kb_key}")
        
        # Convert citations to Citation objects
        citations = [
            Citation(
                source=cit["source"],
                verse=cit.get("verse"),
                text=cit.get("text"),
                meaning=cit.get("meaning"),
                context=cit.get("context")
            )
            for cit in kb_data["citations"]
        ]
        
        response = {
            "answer": kb_data["answer"],
            "tradition": kb_data["tradition"],
            "citations": citations,
            "confidence_score": kb_data["confidence"],
            "source": "Knowledge Base (Verified)",
            "method": "Direct Match",
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        return response
    
    # Step 2: If no exact match, check if tradition is specified
    if tradition and tradition in ["vedanta", "buddhism", "yoga", "samkhya", "nyaya", "mimamsa"]:
        # Find questions from that tradition
        tradition_questions = [q for q in get_all_questions() if q["tradition"] == tradition]
        
        if tradition_questions:
            logger.info(f"Suggesting {len(tradition_questions)} questions from {tradition}")
            
            fallback_answer = f"""
Your question about '{question}' is not directly in our knowledge base.

However, we specialize in {tradition.upper()} philosophy. Here are related topics we can address:

"""
            for i, q in enumerate(tradition_questions[:5], 1):
                fallback_answer += f"{i}. {q['question']}\n"
            
            fallback_answer += f"""
Please ask any of these questions directly, or rephrase your question to match our covered topics.

Available philosophical traditions:
- Vedanta (Non-dual philosophy, Atman, Brahman, Maya)
- Buddhism (Four Noble Truths, Emptiness, Dependent Origination)
- Yoga (Ashtanga Yoga, Samadhi, Chakras)
- Samkhya (Prakriti, Purusha, Gunas)
- Nyaya (Logic, Epistemology, Pramanas)
- Mimamsa (Dharma, Ritual, Karma)
            """
            
            response = {
                "answer": fallback_answer,
                "tradition": tradition,
                "citations": [
                    Citation(
                        source="Indian Knowledge System",
                        text=f"Knowledge base contains {len(tradition_questions)} verified answers on {tradition.upper()}",
                        context="Check /available-questions endpoint"
                    )
                ],
                "confidence_score": 0.65,
                "source": "Knowledge Base Redirect",
                "method": "Tradition Filter",
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
            return response
    
    # Step 3: Full fallback response
    logger.warning(f"No suitable match found for: {question}")
    
    all_questions = get_all_questions()
    
    fallback_answer = f"""
Thank you for your question: "{question}"

While this exact question isn't in our current knowledge base, we have comprehensive information on Indian philosophical traditions.

**Our Knowledge Base Contains:**
- {len([q for q in all_questions if q['tradition'] == 'vedanta'])} questions on Vedanta
- {len([q for q in all_questions if q['tradition'] == 'buddhism'])} questions on Buddhism  
- {len([q for q in all_questions if q['tradition'] == 'yoga'])} questions on Yoga
- {len([q for q in all_questions if q['tradition'] == 'samkhya'])} questions on Samkhya
- {len([q for q in all_questions if q['tradition'] == 'nyaya'])} questions on Nyaya
- {len([q for q in all_questions if q['tradition'] == 'mimamsa'])} questions on Mimamsa

**How to get answers:**
1. Visit /available-questions to see all topics we cover
2. Use /search?keyword=... to find related topics
3. Ask similar questions like: "What is Atman?", "What is Samadhi?", "What is Dharma?"

**Example Questions You Can Ask:**
- "What is Atman and Brahman?" (Vedanta)
- "Explain the Four Noble Truths" (Buddhism)
- "What is Samadhi?" (Yoga)
- "What is Maya?" (Vedanta)
- "Explain Dependent Origination" (Buddhism)

We're committed to providing accurate, citation-backed answers from classical Indian texts.
    """
    
    response = {
        "answer": fallback_answer,
        "tradition": "general",
        "citations": [
            Citation(
                source="Indian Knowledge System",
                text=f"Total verified answers in knowledge base: {len(all_questions)}",
                context="See /available-questions or /search endpoints"
            )
        ],
        "confidence_score": 0.50,
        "source": "Knowledge Base Fallback",
        "method": "General Guidance",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    return response


# ============================================
# API ENDPOINTS
# ============================================

@app.get("/", tags=["Info"])
async def root():
    """Root endpoint with API information"""
    return {
        "name": "Indian Philosophy Chatbot 🕉️",
        "version": "1.0.0",
        "description": "Advanced AI Chatbot on Indian Knowledge Systems",
        "endpoints": {
            "health": "/health",
            "all_questions": "/available-questions",
            "search": "/search?keyword=...",
            "specific_question": "/question/{question_key}",
            "chat": "/chat (POST)",
            "traditions": "/traditions"
        },
        "documentation": "/docs"
    }


@app.get("/health", response_model=HealthCheckResponse, tags=["Info"])
async def health_check():
    """Health check endpoint"""
    logger.info("Health check requested")
    return {
        "status": "healthy",
        "service": "Indian Philosophy Chatbot Backend",
        "version": "1.0.0",
        "knowledge_base_size": len(INDIAN_PHILOSOPHY_KB),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


@app.get("/traditions", tags=["Philosophy"])
async def get_traditions():
    """Get all available philosophical traditions"""
    traditions_info = {
        "vedanta": {
            "name": "Vedanta",
            "description": "Advaita, Dvaita, Vishishtadvaita - Non-dual philosophy from Upanishads",
            "key_concepts": ["Atman", "Brahman", "Maya", "Moksha", "Avidya"],
            "primary_texts": ["Upanishads", "Brahma Sutras", "Bhagavad Gita"]
        },
        "buddhism": {
            "name": "Buddhism",
            "description": "Buddhist philosophy - Four Noble Truths, Emptiness, Dependent Origination",
            "key_concepts": ["Dukkha", "Sunyata", "Anatman", "Nirvana", "Karma"],
            "primary_texts": ["Tripitaka", "Mahayana Sutras"]
        },
        "yoga": {
            "name": "Yoga",
            "description": "Yoga Sutras - Ashtanga Yoga, Samadhi, Prakriti-Purusha",
            "key_concepts": ["Asana", "Pranayama", "Samadhi", "Pratyahara", "Dharana"],
            "primary_texts": ["Yoga Sutras of Patanjali"]
        },
        "samkhya": {
            "name": "Samkhya",
            "description": "Enumeration philosophy - Prakriti (matter) and Purusha (consciousness)",
            "key_concepts": ["Prakriti", "Purusha", "Gunas", "Kaivalya", "Tattwas"],
            "primary_texts": ["Samkhya Karika"]
        },
        "nyaya": {
            "name": "Nyaya",
            "description": "Logic and epistemology - Valid means of knowledge (pramanas)",
            "key_concepts": ["Pramanas", "Logic", "Epistemology", "Inference", "Perception"],
            "primary_texts": ["Nyaya Sutras"]
        },
        "mimamsa": {
            "name": "Mimamsa",
            "description": "Ritual interpretation - Dharma, Karma, Ritual action",
            "key_concepts": ["Dharma", "Karma", "Ritual", "Duty", "Apurva"],
            "primary_texts": ["Purva Mimamsa Sutra"]
        }
    }
    
    logger.info("Traditions list requested")
    return {
        "total_traditions": len(traditions_info),
        "traditions": traditions_info
    }


@app.get("/available-questions", response_model=AllQuestionsResponse, tags=["Knowledge Base"])
async def available_questions():
    """Get all available questions in knowledge base"""
    all_qs = get_all_questions()
    traditions = sorted(list(set([q["tradition"] for q in all_qs])))
    
    logger.info(f"Available questions requested - Total: {len(all_qs)}")
    
    return {
        "total_questions": len(all_qs),
        "traditions": traditions,
        "questions": all_qs
    }


@app.get("/search", tags=["Knowledge Base"])
async def search(keyword: str = Query(..., min_length=2, max_length=100)):
    """
    Search knowledge base by keyword
    
    Args:
        keyword: Search term
    
    Returns:
        List of matching questions with match scores
    """
    if not keyword.strip():
        raise HTTPException(status_code=400, detail="Search keyword required (min 2 chars)")
    
    results = search_kb(keyword)
    logger.info(f"Search query: '{keyword}' - Results found: {len(results)}")
    
    return {
        "keyword": keyword,
        "results_found": len(results),
        "results": results,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


@app.get("/question/{question_key}", response_model=PhilosophyResponse, tags=["Knowledge Base"])
async def get_specific_question(question_key: str):
    """
    Get specific question and complete answer with citations
    
    Args:
        question_key: Key identifier for the question
    
    Returns:
        Complete philosophical answer with citations
    """
    data = get_answer_by_key(question_key)
    
    if not data:
        logger.warning(f"Question not found: {question_key}")
        raise HTTPException(
            status_code=404,
            detail=f"Question '{question_key}' not found. Use /available-questions to see all topics."
        )
    
    citations = [
        Citation(
            source=cit["source"],
            verse=cit.get("verse"),
            text=cit.get("text"),
            meaning=cit.get("meaning"),
            context=cit.get("context")
        )
        for cit in data["citations"]
    ]
    
    logger.info(f"Specific question retrieved: {question_key}")
    
    return PhilosophyResponse(
        answer=data["answer"],
        tradition=data["tradition"],
        citations=citations,
        confidence_score=data["confidence"],
        source="Knowledge Base (Verified)",
        method="Direct Retrieval",
        timestamp=datetime.utcnow().isoformat() + "Z"
    )


@app.post("/chat", response_model=PhilosophyResponse, tags=["Chat"])
async def chat(query: PhilosophyQuery):
    """
    Main chatbot endpoint - Process philosophical queries
    
    Args:
        query: PhilosophyQuery object with question and optional tradition
    
    Returns:
        PhilosophyResponse with answer, citations, and confidence score
    """
    
    if not query.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    logger.info(f"Chat query received: {query.question[:50]}...")
    
    # Generate response from knowledge base
    response_data = generate_philosophical_response(
        query.question,
        query.philosophical_tradition
    )
    
    return PhilosophyResponse(**response_data)


@app.post("/batch-chat", tags=["Chat"])
async def batch_chat(queries: List[PhilosophyQuery]):
    """
    Process multiple philosophical queries at once
    
    Args:
        queries: List of PhilosophyQuery objects
    
    Returns:
        List of PhilosophyResponse objects
    """
    
    if not queries:
        raise HTTPException(status_code=400, detail="At least one query required")
    
    if len(queries) > 10:
        raise HTTPException(status_code=400, detail="Maximum 10 queries per batch")
    
    logger.info(f"Batch chat request with {len(queries)} queries")
    
    responses = []
    for query in queries:
        response_data = generate_philosophical_response(
            query.question,
            query.philosophical_tradition
        )
        responses.append(PhilosophyResponse(**response_data))
    
    return {
        "total_queries": len(queries),
        "responses": responses,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


@app.get("/statistics", tags=["Info"])
async def statistics():
    """Get knowledge base statistics"""
    all_qs = get_all_questions()
    tradition_counts = {}
    
    for q in all_qs:
        tradition = q["tradition"]
        tradition_counts[tradition] = tradition_counts.get(tradition, 0) + 1
    
    logger.info("Statistics requested")
    
    return {
        "total_questions": len(all_qs),
        "total_traditions": len(tradition_counts),
        "questions_by_tradition": tradition_counts,
        "coverage": {
            "vedanta": "Advanced - 3 questions",
            "buddhism": "Advanced - 3 questions",
            "yoga": "Advanced - 2 questions",
            "samkhya": "Intermediate - 1 question",
            "nyaya": "Intermediate - 1 question",
            "mimamsa": "Intermediate - 1 question"
        },
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


# ============================================
# ERROR HANDLERS
# ============================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler"""
    logger.error(f"HTTP Exception: {exc.status_code} - {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """General exception handler"""
    logger.error(f"Unhandled Exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
    )
