import discord
from discord import client
from constants import TOKEN

class TTHBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_voice_state_update(self, member, before, after):
        if member.id == self.user.id: # type: ignore
            return

        if self.voice_clients:
            await self.voice_clients[0].disconnect()

        if after.channel:
            await after.channel.connect()
            self.olha_ele_ae()

    def olha_ele_ae(self):
        if not self.voice_clients:
            return
        voice = self.voice_clients[0]
        voice.play(discord.FFmpegPCMAudio(source='audios/olha_ele_ae.mp3'))

client = TTHBot()
client.run(TOKEN)
