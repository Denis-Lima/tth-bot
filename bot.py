import discord
from discord import client
from constants import TOKEN

class TTHBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_voice_state_update(self, member, before, after):
        if member.id == self.user.id: # type: ignore
            return

        voice = None
        if self.voice_clients:
            voice = self.voice_clients[0]

        # someone quit from the voice channel
        if after.channel is None:
            members = voice.channel.members # type: ignore
            if voice and len(members) == 1 and members[0].id == self.user.id: # type: ignore
                await self.voice_clients[0].disconnect()
                return

        need_connect = True
        if voice:
            if after.channel is not None and voice.channel.id != after.channel.id:
                await voice.disconnect()
            else:
                need_connect = False

        if after.channel:
            if need_connect:
                await after.channel.connect()
            #self.olha_ele_ae()

    def olha_ele_ae(self):
        if not self.voice_clients:
            return
        voice = self.voice_clients[0]
        voice.play(discord.FFmpegPCMAudio(source='audios/olha_ele_ae.mp3'))

client = TTHBot()
client.run(TOKEN)
