# Threat Model

## Project

Secure MCP Agent: A Multi-Layer Guardrail Framework for Safe Tool Invocation Using LangChain

---

## Threat 1: Prompt Injection

### Description

An attacker attempts to override system instructions and manipulate the agent into performing unauthorized actions.

### Examples

* Ignore previous instructions
* Reveal system prompt
* Act as root user
* Bypass all restrictions

### Mitigation

Input Guardrails

---

## Threat 2: PII Exposure

### Description

Sensitive information may be exposed through user input or generated responses.

### Examples

* Email addresses
* Phone numbers
* PAN numbers
* Aadhaar-like identifiers

### Mitigation

PII Detection and Redaction Middleware

---

## Threat 3: Unauthorized Tool Usage

### Description

An attacker attempts to invoke tools outside approved access policies.

### Examples

* Reading arbitrary files
* Accessing restricted paths
* Retrieving secrets

### Mitigation

Tool Authorization Layer

---

## Threat 4: Sensitive Output Leakage

### Description

Tool outputs may expose confidential information.

### Examples

* Internal prompts
* User identifiers
* Restricted data

### Mitigation

Output Guardrails

---

## Security Objectives

SO-1 Prompt Injection Resistance

SO-2 PII Protection

SO-3 Tool Access Control

SO-4 Safe Output Generation
