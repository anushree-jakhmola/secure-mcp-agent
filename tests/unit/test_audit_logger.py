from guardrails.audit_logger import log_event


log_event(
    "TEST_EVENT",
    "Audit logging operational"
)

print(
    "Audit event written successfully."
)