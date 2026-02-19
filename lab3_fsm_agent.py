
import asyncio
import random
from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State


# ---------------------------
# Simulated Severity Generator
# ---------------------------
def get_severity():
    return random.choice(["LOW", "MEDIUM", "HIGH", "CRITICAL"])


# ---------------------------
# FSM States
# ---------------------------
class MonitoringState(State):
    async def run(self):
        severity = get_severity()
        print(f"\n[Monitoring] Severity detected: {severity}")

        if severity == "MEDIUM":
            self.set_next_state("PREPARING")
        elif severity == "HIGH":
            self.set_next_state("RESPONDING")
        elif severity == "CRITICAL":
            self.set_next_state("RESCUING")
        else:
            self.set_next_state("MONITORING")


class PreparingState(State):
    async def run(self):
        print("[Preparing] Emergency team on standby...")
        await asyncio.sleep(2)
        self.set_next_state("MONITORING")


class RespondingState(State):
    async def run(self):
        print("[Responding] Deploying response units...")
        await asyncio.sleep(2)
        self.set_next_state("MONITORING")


class RescuingState(State):
    async def run(self):
        print("[Rescuing] Rescue mission activated!")
        await asyncio.sleep(3)
        self.set_next_state("MONITORING")


# ---------------------------
# Agent Definition
# ---------------------------
class RescueAgent(Agent):
    async def setup(self):
        print("Rescue Agent with FSM Started...")

        fsm = FSMBehaviour()

        fsm.add_state(name="MONITORING", state=MonitoringState(), initial=True)
        fsm.add_state(name="PREPARING", state=PreparingState())
        fsm.add_state(name="RESPONDING", state=RespondingState())
        fsm.add_state(name="RESCUING", state=RescuingState())

        fsm.add_transition("MONITORING", "PREPARING")
        fsm.add_transition("MONITORING", "RESPONDING")
        fsm.add_transition("MONITORING", "RESCUING")
        fsm.add_transition("MONITORING", "MONITORING")

        fsm.add_transition("PREPARING", "MONITORING")
        fsm.add_transition("RESPONDING", "MONITORING")
        fsm.add_transition("RESCUING", "MONITORING")

        self.add_behaviour(fsm)


async def main():
    agent = RescueAgent("russell21@xmpp.jp", "russell", verify_security=False)
    await agent.start()
    await asyncio.sleep(30)
    await agent.stop()

asyncio.run(main())

