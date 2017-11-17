import discord
import utils.data as data
from utils.roles import get_role, get_next_role, roles
from discord.ext import commands
import asyncio


class Secret:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def test(self, ctx):
        print(ctx.message.author.roles)

    @commands.command(pass_context=True)
    async def secret(self, ctx, channel_name):
        server = ctx.message.server

        # Setup initial permissions
        permissions = discord.PermissionOverwrite(read_messages=False)
        mine = discord.PermissionOverwrite(read_messages=True)
        # Create secret channel
        channel = await self.bot.create_channel(ctx.message.server, channel_name,
                                                (server.default_role, permissions), (server.me, mine))
        initial_message = await self.bot.send_message(channel,
                                                      '**{}** created. Now I\'ll invite users ordered by rank...'
                                                      .format(channel_name))

        # Initialize
        invited_message = None
        count_invited = 0

        # All members
        members = server.members
        members = list(filter(lambda x: not (x.roles.__len__() == 1 or x.bot), members))
        count_members = members.__len__()
        # Info data
        remanining_message = await self.bot.send_message(channel, '**Members remaining:** {}'
                                                         .format(count_members - count_invited))

        invites_keys = roles.keys()
        invites_keys = sorted(invites_keys, reverse=True)
        for invites_needed in invites_keys:
            rank = roles[invites_needed]
            role = discord.utils.get(server.roles, name=rank)
            rank_message = await self.bot.send_message(channel, '{} now!'.format(role.mention))

            # Current rank members
            members_role = list(filter(lambda x: role in x.roles, members))
            # 10 members of current rank members are invited
            members_role_count = 10
            count = 0
            out_message = ''
            for member in members_role:
                count += 1
                if count >= members_role_count:
                    if invited_message is not None:
                        await self.bot.delete_message(invited_message)
                    invited_message = await self.bot.send_message(channel, out_message + 'invited!')
                    out_message = ''
                    await asyncio.sleep(15)
                permissions = discord.PermissionOverwrite(read_messages=True)
                await self.bot.edit_channel_permissions(channel, member, permissions)
                out_message += '<@{}> '.format(member.id)
                count_invited += 1
            if invited_message is not None:
                await self.bot.delete_message(invited_message)
                invited_message = None
            if not out_message == '':
                invited_message = await self.bot.send_message(channel, out_message + 'invited!')

            await self.bot.edit_message(remanining_message, '**Members remaining:** {}'
                                        .format(count_members - count_invited))
            await asyncio.sleep(5)
            if invited_message is not None:
                await self.bot.delete_message(invited_message)
                invited_message = None
            if rank_message is not None:
                await self.bot.delete_message(rank_message)
        # Final clean up
        await self.bot.delete_message(remanining_message)
        await self.bot.edit_message(initial_message, 'Finished!')


def setup(bot: commands.Bot):
    bot.add_cog(Secret(bot))
