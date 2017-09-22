import asyncio
import logging
import plugins

flood_id = ""
flood_flag = False

def _initialize(bot):
    plugins.register_handler(_handle_message, type="message")
    plugins.register_user_command(["mememan", "flood"])


@asyncio.coroutine
def mememan(bot, event, *args):
    img = yield from bot.call_shared("image_validate_and_upload_single", "https://i.imgur.com/8Tniy4S.jpg")
    yield from bot.coro_send_message(event.conv_id, "", image_id=img)

def flood(bot, event, *args):
    flood_flag = not flood_flag

@asyncio.coroutine
def _handle_message(bot, event, command):
    if not event.text:
        return
    if event.user_id == flood_id:
        yield from mememan(bot, event)
