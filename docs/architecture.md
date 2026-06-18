# Secure MCP Agent Architecture

## Overview

The Secure MCP Agent is a security-focused AI agent built using LangChain, FastMCP, Ollama, FAISS, and multiple guardrail layers.

The system is designed to demonstrate secure tool execution, prompt-injection defense, PII protection, audit logging, and retrieval-augmented generation (RAG) through MCP tools.

---

## High-Level Architecture

User Query
↓
Input Guardrails
↓
Secure Agent (LangChain + Ollama)
↓
Secure Tool Executor
↓
Tool Authorization Layer
↓
Tool Registry
↓
MCP Tools
├── system_info
└── knowledge_base
↓
FAISS Knowledge Base
↓
Output Guardrails
↓
Response

All security-relevant events are recorded in the audit logging system.

---

## Components

### Input Guardrails

Responsibilities:

* Prompt injection detection
* PII detection
* PII redaction

Examples of blocked attacks:

* Ignore previous instructions
* Reveal system prompt
* Bypass restrictions
* Disable guardrails

---

### Secure Agent

The Secure Agent serves as the orchestration layer.

Responsibilities:

* Process user requests
* Invoke security controls
* Select appropriate MCP tools
* Interact with the local LLM through Ollama
* Apply output security controls

---

### Secure Tool Executor

All tool invocations pass through a centralized execution layer.

Responsibilities:

* Tool authorization
* Tool lookup
* Secure execution
* Audit logging

This prevents direct tool access and enforces least-privilege principles.

---

### Tool Registry

The registry maintains all approved tools.

Registered tools:

* system_info
* knowledge_base

Only registered tools can be executed.

---

### MCP Layer

FastMCP is used to expose tools through the Model Context Protocol.

Capabilities:

* Tool discovery
* Tool invocation
* Standardized tool interface

---

### Knowledge Base

The knowledge base contains security and policy documents.

Current documents:

* AI Safety Policy
* MCP Security Policy
* Data Protection Policy
* Prompt Injection Guide

---

### Retrieval-Augmented Generation (RAG)

The RAG subsystem uses:

* Sentence Transformers
* FAISS Vector Search

Workflow:

Documents
→ Embeddings
→ FAISS Index
→ Similarity Search
→ Retrieved Context

Retrieved context is supplied to the LLM for grounded responses.

---

### Output Guardrails

Responsibilities:

* PII redaction
* Output sanitization

Protected entities:

* Email addresses
* Phone numbers
* PAN identifiers
* Aadhaar identifiers

---

### Audit Logging

Security-relevant events are recorded in audit.log.

Examples:

* PROMPT_INJECTION_BLOCKED
* TOOL_AUTHORIZED
* TOOL_DENIED
* TOOL_EXECUTED

This enables traceability and post-event analysis.

---

## Security Principles

The system follows:

* Least Privilege
* Defense in Depth
* Secure Tool Access
* Retrieval Grounding
* Auditability
* Data Protection

---

## Future Enhancements

* Advanced prompt injection classification
* Risk scoring engine
* Role-based access control
* Multi-document retrieval
* Neo4j knowledge graph integration
* Remote MCP deployment
