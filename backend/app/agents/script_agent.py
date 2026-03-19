from app.agents.base_agent import BaseAgent

class ScriptAgent(BaseAgent):
    name = "script-agent"

    async def run(self, input_data: str):
        return {
            "agent": self.name,
            "script": f"#!/bin/bash\n# Generated script\n{input_data}"
        }
