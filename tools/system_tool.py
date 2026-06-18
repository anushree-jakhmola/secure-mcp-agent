"""
System Information Tool

Provides safe machine information.
"""

import platform
import sys


def get_system_info() -> dict:
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "python_version": sys.version,
    }