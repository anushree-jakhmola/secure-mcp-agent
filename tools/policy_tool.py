from tools.rag_tool import (
    search_knowledge_base,
)


def lookup_policy(
    query: str,
):
    """
    Search security and policy documents.
    """

    return search_knowledge_base(
        query,
        top_k=1,
    )