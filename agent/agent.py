from langchain_ollama import ChatOllama

from guardrails.input_guardrails import (
    secure_input_pipeline,
)
from guardrails.output_guardrails import (
    secure_output_pipeline,
)

from mcp_server.server import execute_tool


class SecureAgent:

    def __init__(self):

        self.llm = ChatOllama(
            model="llama3.2:3b"
        )

    def run(
        self,
        user_query: str,
    ) -> str:

        allowed, processed_input = (
            secure_input_pipeline(
                user_query
            )
        )

        if not allowed:
            return processed_input

        query_lower = (
            processed_input.lower()
        )

        if (
            "prompt injection" in query_lower
            or "policy" in query_lower
            or "security" in query_lower
        ):

            results = execute_tool(
                "knowledge_base",
                processed_input,
            )

            context = results[0]["content"]

            prompt = f"""
Answer the user's question
using the provided context.

Context:
{context}

Question:
{processed_input}
"""

        else:

            prompt = processed_input

        response = self.llm.invoke(
            prompt
        )

        final_response = (
            secure_output_pipeline(
                response.content
            )
        )

        return final_response