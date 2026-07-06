# Secure MCP Agent — Office Deployment Runbook

## Deployment Status

- Fresh GitHub clone validated successfully
- Fresh isolated virtual environment validated successfully
- Dependencies installed successfully
- FAISS index regenerated successfully
- All five demos passed end-to-end on macOS
- Windows automation prepared; first Windows runtime validation pending

## Deployment Sequence

**CLONE → PRE-FLIGHT → SETUP → PRE-FLIGHT → RUN**

---

## 1. Clone the Repository

Open Command Prompt or PowerShell:

```powershell
git clone https://github.com/anushree-jakhmola/secure-mcp-agent.git
cd secure-mcp-agent
```

## 2. Run Pre-Flight Diagnostics

```powershell
preflight_windows.bat
```

This checks:

- Python
- Git
- required project files
- virtual environment
- FAISS artifacts
- Ollama
- `llama3.2:3b`

Before first setup, the virtual environment and FAISS artifacts may not exist. This is expected.

## 3. Perform First-Time Setup

```powershell
setup_windows.bat
```

The setup script:

- checks Python
- creates an isolated virtual environment
- upgrades pip
- installs project dependencies
- rebuilds the FAISS knowledge-base index
- checks Ollama availability

## 4. Run Pre-Flight Again

```powershell
preflight_windows.bat
```

After setup, verify:

- virtual environment is READY
- FAISS artifacts exist
- Ollama is READY for the complete demo
- `llama3.2:3b` is available for Demo 5

## 5. Run the Demonstration

```powershell
run_demo.bat
```

## Demo Sequence

1. PII Redaction
2. Prompt Injection Protection
3. Security Policy Retrieval
4. Secure File Access and Path Traversal Blocking
5. RAG-Grounded AI Agent

---

## If Something Fails

Do not randomly reinstall packages.

Run:

```powershell
preflight_windows.bat
```

Identify the first component reported as `MISSING` or `NOT SET UP`.

### Check Python

```powershell
py --version
```

### Check Git

```powershell
git --version
```

### Re-run Project Setup

```powershell
setup_windows.bat
```

### Check Ollama

```powershell
ollama --version
```

### Check the Required Model

```powershell
ollama list
```

Required model:

```text
llama3.2:3b
```

Use only the organization-approved installation or model-transfer process.

---

## 30-Second Technical Explanation

The deployment is automated for reproducibility. The pre-flight script performs environment diagnostics without modifying the machine. The setup script creates an isolated Python environment, installs the declared dependencies, and rebuilds the FAISS vector index from the tracked policy documents. The launcher validates the local Ollama runtime and required model before executing the unified five-part security demonstration.

## Architecture

```text
User Input
→ Input Guardrails
→ Secure Agent
→ Tool Authorization
→ MCP Tool Execution
→ RAG / Secure Resource Access
→ Local LLM
→ Output Guardrails
→ Final Response
```

## Validation Record

The project was validated from a fresh GitHub clone using:

- a newly created isolated virtual environment
- a clean dependency installation
- fresh FAISS index generation from the tracked policy documents
- successful execution of all five demos

Fresh-clone end-to-end validation passed on macOS. The Windows automation workflow has been prepared and statically reviewed; the first Windows deployment will serve as the Windows runtime validation.