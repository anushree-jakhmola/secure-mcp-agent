# Secure MCP Agent

A security-focused AI agent framework that demonstrates how **Model Context Protocol (MCP)** based AI systems can be protected using layered security guardrails.

The project integrates **LangChain**, **Ollama**, **FastMCP**, **FAISS**, and multiple security mechanisms to defend against prompt injection, protect sensitive information, authorize tool execution, secure file access, and provide Retrieval-Augmented Generation (RAG) using a trusted knowledge base.

---

# Project Overview

Large Language Models (LLMs) are increasingly connected to external tools and enterprise data through the **Model Context Protocol (MCP)**. While this enables powerful AI agents, it also introduces several security risks such as:

- Prompt Injection
- Prompt Leakage
- Personally Identifiable Information (PII) Exposure
- Unauthorized Tool Execution
- File Path Traversal
- Information Leakage

This project demonstrates a **layered security architecture** that mitigates these risks before and after LLM execution.

---

# Key Features

## Input Security

- Input Normalization
- Prompt Injection Detection
- PII Detection & Redaction
- Multi-layer Input Validation

---

## Secure AI Agent

- LangChain Integration
- Ollama Integration
- Llama 3.2 Model
- Secure Agent Orchestration
- Retrieval-Augmented Generation (RAG)

---

## Retrieval-Augmented Generation (RAG)

- FAISS Vector Database
- Sentence Transformers
- Knowledge Base Search
- Policy Retrieval
- Grounded Responses

---

## MCP Tool Security

- FastMCP Integration
- Tool Registration
- Tool Authorization
- Secure Tool Invocation
- Restricted Tool Access

---

## File Security

- Directory Whitelisting
- Path Traversal Protection
- Unauthorized File Blocking

---

## Output Security

- PII Redaction
- Prompt Leakage Prevention
- Internal Path Redaction
- Output Sanitization

---

## Audit Logging

Security-sensitive events are logged including:

- Prompt Injection Attempts
- Unauthorized Tool Requests
- Output Sanitization Events
- File Access Violations

---

# System Architecture


                           User
                             │
                             ▼
                  Input Guardrails
                             │
      ┌────────────────────────────────┐
      │ • Input Normalization          │
      │ • Prompt Injection Detection   │
      │ • PII Redaction                │
      └────────────────────────────────┘
                             │
                             ▼
                    Secure AI Agent
               (LangChain + Ollama)
                             │
                             ▼
                    Tool Authorization
                             │
        ┌──────────────┬───────────────┬──────────────┐
        ▼              ▼               ▼              ▼
 Knowledge Base   Policy Lookup   File Access   System Info
        │
        ▼
     FAISS Vector Database
        │
        ▼
      Llama 3.2 Response
        │
        ▼
                 Output Guardrails
        ┌────────────────────────────────┐
        │ • PII Redaction                │
        │ • Prompt Leakage Protection    │
        │ • File Path Sanitization       │
        └────────────────────────────────┘
                             │
                             ▼
                       Final Response
```

---

# Project Structure

```text
secure-mcp-agent/

├── agent/
├── docs/
├── guardrails/
├── knowledge_base/
├── mcp_server/
├── tools/

├── tests/
│   ├── integration/
│   ├── security/
│   └── unit/

├── demo.py
├── main.py
├── requirements.txt
├── README.md
```

---

# Implemented Security Layers

| Security Layer | Purpose |
|---------------|---------|
| Input Normalization | Standardizes user input before validation |
| Prompt Injection Detection | Blocks malicious instruction override attempts |
| PII Detection & Redaction | Removes sensitive user information |
| Tool Authorization | Allows execution of approved MCP tools only |
| Secure File Guardrails | Prevents directory traversal attacks |
| Output Guardrails | Sanitizes AI responses before returning them |
| Audit Logging | Records all security-sensitive operations |

---

# Available MCP Tools

| Tool | Description |
|------|-------------|
| knowledge_base | Searches the FAISS knowledge base |
| policy_lookup | Retrieves security policy information |
| file_access | Provides secure access to approved documents |
| system_info | Returns system and runtime information |

---

# Knowledge Base

The FAISS knowledge base currently contains:

- AI Safety Policy
- MCP Security Policy
- Data Protection Policy
- Prompt Injection Guide

These documents are retrieved during RAG-based question answering.

---

# Security Demonstration

The project includes a comprehensive demonstration showcasing:

- Input Security Pipeline
- Prompt Injection Prevention
- PII Redaction
- Retrieval-Augmented Generation
- Secure File Access
- Tool Authorization
- Output Guardrails
- Secure AI Agent

Run the demonstration:

```bash
python demo.py
```

---

# Security Test Suite

The project contains organized automated test suites.

## Security Tests

- Input Normalization
- Prompt Injection Detection
- PII Detection
- File Guardrails
- Tool Authorization
- Output Guardrails
- Input Security Integration

Run all security tests:

```bash
python tests/security/run_security_tests.py
```

---

## Integration Tests

Tests complete interaction between:

- LangChain
- Ollama
- MCP Server
- Secure Agent

---

## Unit Tests

Individual validation of:

- Policy Tools
- Audit Logger
- File Access
- MCP Tools
- Embeddings

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project:

```bash
cd secure-mcp-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Build the FAISS knowledge base:

```bash
python knowledge_base/build_index.py
```

---

# Running the Project

Start the interactive demonstration:

```bash
python demo.py
```

Run the Secure AI Agent:

```bash
python main.py
```

Run the complete security validation suite:

```bash
python tests/security/run_security_tests.py
```

---

# Security Scope

This project demonstrates layered, rule-based security controls for AI agents. It is intended as a learning and engineering project and does **not** claim to provide absolute protection against every possible attack.

Current protections include:

- Prompt Injection Detection
- PII Protection
- Tool Authorization
- File Access Restrictions
- Prompt Leakage Prevention
- Output Sanitization

---

# Future Improvements

- Machine Learning-based Prompt Injection Detection
- Risk Scoring Engine
- Role-Based Access Control (RBAC)
- Multi-Agent Security
- Neo4j Knowledge Graph Integration
- Remote MCP Deployment
- JWT Authentication
- Human Approval Workflow

---

# Technology Stack

- Python 3.14
- LangChain
- Ollama
- Llama 3.2
- FastMCP
- FAISS
- Sentence Transformers
- Pydantic

---

# Author

Developed as part of the **Bharat Electronics Limited (BEL)** AI/ML Internship Project.

Focus Areas:

- AI Security
- Model Context Protocol (MCP)
- Retrieval-Augmented Generation (RAG)
- Secure AI Agents
- Guardrails for LLM Applications