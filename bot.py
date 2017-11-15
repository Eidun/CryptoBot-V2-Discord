import sys
import traceback
import discord
from discord.ext import commands
import utils.roles


description = '''Ironman-Bot'''

modules = {'cogs.roles_management', 'cogs.secret_channel', 'cogs.roles_config'}

bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Iron-man Bot starting...')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name='with you'))

    print('Loading cogs...')
    if __name__ == '__main__':
        modules_loaded = 0
        for module in modules:
            try:
                bot.load_extension(module)
                print('\t' + module)
                modules_loaded += 1
            except Exception as e:
                traceback.print_exc()
                print(f'Error loading the extension {module}', file=sys.stderr)
        print(str(modules_loaded) + '/' + str(modules.__len__()) + ' modules loaded')
        print('Systems 100%')
    print('------')


@bot.event
async def on_member_join(member:discord.Member):
    greet = 'Welcome, <@{}>!\n- Please, read the <@380203802969505792>.\n' \
            'Pump announcements and signals are posted in <@380204258529771532>.\n' \
            '- To get ranks in affiliate system, start from generating referral link,' \
            ' this is how you do it <@380203911329480714>'.format(member.id)
    channel = bot.get_channel('380206015024594956')
    await bot.send_message(channel, greet)

# Test bot
bot.run('MzgwMDUyNTc3NDU2MzU3Mzc2.DOy_HA.xIika7xdqcpt2zcT8PT1GoXTFM4')
