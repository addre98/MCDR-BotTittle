import re
from mcdreforged.api.all import *

BOT_PATTERN = re.compile(r'^(\w+)\[local\] logged in with entity id')
TEAM_NAME = 'Bot'

bot_names = set()
config = {}


def on_load(server: PluginServerInterface, old):
    global bot_names, config
    if old is not None and hasattr(old, 'bot_names'):
        bot_names = old.bot_names
    config = server.load_config_simple('config.json', {
        'title_prefix': '§f[§aBot§f]'
    })
    server.logger.info('BotTittle loaded, {} bot(s) known'.format(len(bot_names)))


def on_server_startup(server: PluginServerInterface):
    prefix = config.get('title_prefix', '§f[§aBot§f]')
    server.execute(f'team add {TEAM_NAME}')
    server.execute(f'team modify {TEAM_NAME} prefix "{prefix}"')
    server.execute(f'team modify {TEAM_NAME} collisionRule never')
    for name in bot_names:
        server.execute(f'team join {TEAM_NAME} {name}')


def on_player_joined(server: PluginServerInterface, player: str, info: Info):
    if player in bot_names:
        server.execute(f'team join {TEAM_NAME} {player}')
        return
    m = BOT_PATTERN.match(info.content)
    if m:
        bot_names.add(m.group(1))
        server.execute(f'team join {TEAM_NAME} {player}')
