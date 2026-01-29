import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour


class HelloAgent(Agent):
    class HelloBehaviour(CyclicBehaviour):
        async def run(self):
            print("✅ Agent is running and alive...")
            await asyncio.sleep(5)

    async def setup(self):
        print("🚀 Agent starting...")
        self.add_behaviour(self.HelloBehaviour())


async def main():
    # 🔴 Replace with your real XMPP credentials
    jid = "your_username@xmpp.jp"
    password = "your_password"

    agent = HelloAgent(jid, password)
    await agent.start()

    print("🤖 Agent started successfully!")

    # Keep agent alive
    while agent.is_alive():
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
