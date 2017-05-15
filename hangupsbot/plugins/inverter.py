import asyncio, logging

import hangups

import plugins

logger = logging.getLogger(__name__)

enabled_conversations = []

def _initialise(bot):
    plugins.register_handler(_handle_incoming_message, type="message")
    plugins.register_user_command(["tob"])


@asyncio.coroutine
def _handle_incoming_message(bot, event, command):
    """Handle random message intercepting"""

    if event.conv_id not in enabled_conversations:
        return

    if event.text.startswith('##') or event.text.startswith('/bot') or event.text.startswith('http'):
    	return

    if not event.text:
        return

    text = event.text[::-1]
    if text:
        yield from bot.coro_send_message(event.conv_id, text)

def tob(bot, event, *args):
    if event.conv_id in enabled_conversations:
        enabled_conversations.remove(event.conv_id)
        text = "Deactivating text inverter..."
    else:
        enabled_conversations.append(event.conv_id)
        text = "Activating text inverter..."[::-1]

    yield from bot.coro_send_message(event.conv_id, text)
