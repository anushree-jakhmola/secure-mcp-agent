from tools.system_tool import get_system_info
from tools.rag_tool import search_knowledge_base


TOOL_REGISTRY = {
    "system_info": get_system_info,
    "knowledge_base": search_knowledge_base,
}