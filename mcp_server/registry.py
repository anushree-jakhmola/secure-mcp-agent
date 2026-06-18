"""
Tool Registry

Central place for tool registration.
"""

from tools.system_tool import get_system_info


TOOL_REGISTRY = {
    "system_info": get_system_info,
}