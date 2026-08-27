import os

from hopx_ai import Sandbox

sandbox = Sandbox.create(
    template="code-interpreter",
    api_key=os.getenv("hopx_live_JOdRbWpHzHS0.1bX_Lckj-Nkl7nTWYDvSaDHtnec4mSEqDTngCylgBn0")
)

print(f"Sandbox ID: {sandbox.sandbox_id}")

# Execute code in the sandbox
result = sandbox.run_code("print('Hello from HopX!')")
print(result.stdout)  # "Hello from HopX!"

# Cleanup
sandbox.kill()
