from guardrails.pii_guardrail import redact_pii


sample = """
Email: john.doe@gmail.com
Phone: 9876543210
PAN: ABCDE1234F
AADHAAR: 1234 5678 9012
"""

print(redact_pii(sample))