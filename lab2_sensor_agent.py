import asyncio
import random
from datetime import datetime
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour


# -----------------------------
# Simulated Disaster Environment
# -----------------------------
class DisasterEnvironment:
    def __init__(self):
        self.severity_levels = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

    def get_disaster_status(self):
        severity = random.choice(self.severity_levels)
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "severity": severity
        }


# -----------------------------
# Sensor Behaviour
# -----------------------------
class SensorBehaviour(CyclicBehaviour):
    async def run(self):
        status = self.agent.environment.get_disaster_status()

        print("\n[Sensor Report]")
        print("Time:", status["timestamp"])
        print("Disaster Severity:", status["severity"])

        # Log to file
        with open("disaster_log.txt", "a") as file:
            file.write(f"{status['timestamp']} - {status['severity']}\n")

        await asyncio.sleep(5)


# -----------------------------
# Sensor Agent
# -----------------------------
class SensorAgent(Agent):
    async def setup(self):
        print("Sensor Agent Started...")
        self.environment = DisasterEnvironment()
        self.add_behaviour(SensorBehaviour())


# -----------------------------
# Main
# -----------------------------
async def main():
    agent = SensorAgent(
        "russell21@xmpp.jp",
        "russell",
        verify_security=False
    )

    await agent.start()
    await asyncio.sleep(30)
    await agent.stop()

asyncio.run(main())
