# Secure MCP Agent

A security-focused AI agent framework built using LangChain, FastMCP, Ollama, FAISS, and multiple guardrail layers.

The project demonstrates secure tool execution, prompt injection defense, retrieval-augmented generation (RAG), audit logging, and secure MCP tool integration.

---

## Features

### Security

* Prompt Injection Detection
* PII Detection and Redaction
* Tool Authorization
* Secure Tool Execution
* Audit Logging
* Restricted File Access

### MCP

* FastMCP Integration
* Tool Discovery
* Tool Registration
* Secure Tool Invocation

### Retrieval-Augmented Generation (RAG)

* Sentence Transformers
* FAISS Vector Search
* Security Knowledge Base
* Policy Retrieval

### Agent Framework

* LangChain Integration
* Ollama Integration
* Llama 3.2 Support
* Secure Agent Orchestration

---

## Architecture

User Query
↓
Input Guardrails
↓
Secure Agent (LangChain + Ollama)
↓
Secure Executor
↓
Tool Authorization
↓
MCP Tools
├── system_info
├── knowledge_base
├── policy_lookup
└── file_access
↓
FAISS Knowledge Base
↓
Output Guardrails
↓
Response

Audit logging operates across all security-sensitive operations.

---

## MCP Tools

### system_info

Returns platform and Python runtime information.

### knowledge_base

Performs retrieval from the FAISS knowledge base.

### policy_lookup

Retrieves information from security policy documents.

### file_access

Provides restricted file access to approved directories.

---

## Security Controls

### Prompt Injection Protection

Blocked examples:

* Ignore previous instructions
* Reveal system prompt
* Disable guardrails
* Bypass restrictions

### PII Protection

Supported redactions:

* Email Addresses
* Phone Numbers
* PAN Numbers
* Aadhaar Numbers

### File Access Protection

Path traversal attacks are blocked.

Example:

../../../secret.txt

Result:

Access Denied

---

## Knowledge Base

Current documents:

* AI Safety Policy
* MCP Security Policy
* Data Protection Policy
* Prompt Injection Guide

---

## Installation

```bash
git clone <repository-url>

cd secure-mcp-agent

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## Running

Build the FAISS index:

```bash
python knowledge_base/build_index.py
```

Run tests:

```bash
python -m tests.test_agent
```

---

## Test Results

Total Tests Executed: 11

Passed: 11

Failed: 0

Pass Rate: 100%

See:

docs/results.md

for detailed validation results.

---

## Threat Model

See:

docs/threat_model.md

for the complete threat analysis.

---

## Future Enhancements

* Advanced prompt injection classification
* Risk scoring engine
* Role-based access control
* Multi-document retrieval
* Neo4j knowledge graph integration
* Remote MCP deployment

---

## Technology Stack

* Python 3.14
* LangChain
* FastMCP
* Ollama
* Llama 3.2
* Sentence Transformers
* FAISS
* Pydantic

---

## Author

Developed as part of the Bharat Electronics Limited (BEL) AI/ML Internship Project.
