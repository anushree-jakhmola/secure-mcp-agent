from agent.agent import SecureAgent

agent = SecureAgent()

response = agent.run(
    "What is prompt injection?"
)

print("\nResponse:\n")
print(response)