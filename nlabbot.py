#!/usr/bin/env python3.8
import os

import discord
from dotenv import load_dotenv

def build_client():
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f"{client.user} is alive! Also, it speaks of itself in the third person.")

    return client


def main():
    client = build_client()
    load_dotenv()
    client.run(os.getenv('DISCORD_TOKEN'))


if __name__ == '__main__':
    main()
