import asyncio

from instances import bot


async def main():
    await bot.start()


if __name__ == "__main__":
    asyncio.run(main())
