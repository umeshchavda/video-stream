"""
Video + Music Stream Telegram Bot
Copyright (c) 2022-present levina=lab <https://github.com/levina-lab>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but without any warranty; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/licenses.html>
"""


from pyrogram import Client
from program.utils.inline import markup
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
    InlineQuery,
)
from youtubesearchpython.__future__ import VideosSearch


@Client.on_inline_query()
async def inline_mode(client: Client, query: InlineQuery):
    answers = []
    request = query.query.strip().lower()
    if request.strip() == "":
        try:
            await client.answer_inline_query(
                query.id,
                results=markup,
                cache_time=10,
            )
        except Exception:
            return
    else:
        take = VideosSearch(request, limit=50)
        result = (await take.next()).get("result")
        for x in range(15):
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[0]
            channelurl = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            description = f"{views} | {duration} mins | {channel} | {published}"
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎬 watch on youtube",
                            url=link,
                        )
                    ],
                ]
            )
            results_text = f"""
🗂 **Title:** [{title}]({link})
⏱ **Duration:** `{duration}` mins
👀 **Views:** `{views}`
⏰ **Published:** {published}
📣 **Channel:** [{channel}]({channelurl})"""
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=results_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await client.answer_inline_query(
                query.id, results=answers
            )
        except Exception:
            return
