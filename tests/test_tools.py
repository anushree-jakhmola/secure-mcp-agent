from guardrails.output_guardrails import (
    secure_output_pipeline,
)

sample_output = """
User email: john.doe@gmail.com
Phone: 9876543210
PAN: ABCDE1234F
AADHAAR: 1234 5678 9012
"""

result = secure_output_pipeline(
    sample_output
)

print(result)