""" inline markup section """


from pyrogram.types import (
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  InlineQueryResultArticle,
  InputTextMessageContent,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="• Mᴇɴᴜ", callback_data=f'stream_menu_panel | {user_id}'),
      InlineKeyboardButton(text="• Cʟᴏsᴇ", callback_data=f'set_close'),
    ],
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="⏹", callback_data=f'set_stop | {user_id}'),
      InlineKeyboardButton(text="⏸", callback_data=f'set_pause | {user_id}'),
      InlineKeyboardButton(text="▶️", callback_data=f'set_resume | {user_id}'),
      InlineKeyboardButton(text="⏭", callback_data=f'set_skip | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔇", callback_data=f'set_mute | {user_id}'),
      InlineKeyboardButton(text="🔊", callback_data=f'set_unmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔙 Go Back", callback_data='stream_home_panel'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🗑 Close", callback_data="set_close"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 Go Back", callback_data="stream_menu_panel"
      )
    ]
  ]
)


markup = []

markup.extend(
  [
    InlineQueryResultArticle(
      title="pause stream",
      description="pause the current track being played.",
      thumb_url="https://telegra.ph/file/6a9ae463fa10ceddac220.png",
      input_message_content=InputTextMessageContent("/vpause"),
    ),
    InlineQueryResultArticle(
      title="resume stream",
      description="play the previously paused track.",
      thumb_url="https://telegra.ph/file/a105311b41b12b8ef3072.png",
      input_message_content=InputTextMessageContent("/vresume"),
    ),
    InlineQueryResultArticle(
      title="mute stream",
      description="mute the streamer userbot on group call.",
      thumb_url="https://telegra.ph/file/b120099ed5e01850ba9bc.png",
      input_message_content=InputTextMessageContent("/vmute"),
    ),
    InlineQueryResultArticle(
      title="unmute stream",
      description="unmute the streamer userbot on group call.",
      thumb_url="https://telegra.ph/file/c9436ea693039422db3e4.png",
      input_message_content=InputTextMessageContent("/vunmute"),
    ),
    InlineQueryResultArticle(
      title="skip stream",
      description="goes to the next track of song in queue.",
      thumb_url="https://telegra.ph/file/2ea38e9b8c4ed6a654b24.png",
      input_message_content=InputTextMessageContent("/vskip"),
    ),
    InlineQueryResultArticle(
      title="stop stream",
      description="stop playback of the track and clears the queue.",
      thumb_url="https://telegra.ph/file/61e7d76a7d6ca76eceb77.png",
      input_message_content=InputTextMessageContent("/vstop"),
    ),
  ]
)
