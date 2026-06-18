from tools.system_tool import get_system_info
from tools.rag_tool import search_knowledge_base
from tools.policy_tool import (
    lookup_policy,
)
from tools.file_tool import (
    read_allowed_file,
)
TOOL_REGISTRY = {
    "system_info": get_system_info,
    "knowledge_base": search_knowledge_base,
    "policy_lookup": lookup_policy,
    "file_access": read_allowed_file,
}