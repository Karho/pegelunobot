#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from telegram import ParseMode
from telegram.ext import CommandHandler

from utils import _, send_async, user_locale
from shared_vars import dispatcher

help_text = ("Follow these steps:\n\n"
             "1. Add this bot to a group\n"
             "2. In the group, start a new game with /new or join an already"
             " running game with /join\n"
             "3. After at least two players have joined, start the game with"
             " /start\n"
             "4. Type <code>@mau_mau_bot</code> into your chat box and hit "
             "<b>space</b>, or click the <code>via @mau_mau_bot</code> text "
             "next to messages. You will see your cards (some greyed out), "
             "any extra options like drawing, and a <b>?</b> to see the "
             "current game state. The <b>greyed out cards</b> are those you "
             "<b>can not play</b> at the moment. Tap an option to execute "
             "the selected action.\n"
             "Players can join the game at any time. To leave a game, "
             "use /leave. If a player takes more than 90 seconds to play, "
             "you can use /skip to skip that player.\n\n"
             "Other commands (only game creator):\n"
             "/close - Close lobby\n"
             "/open - Open lobby\n\n"
             "<b>Experimental:</b> Play in multiple groups at the same time. "
             "Press the <code>Current game: ...</code> button and select the "
             "group you want to play a card in.\n"
             "If you enjoy this bot, "
             "<a href=\"https://telegram.me/storebot?start=mau_mau_bot\">"
             "rate me</a>, join the "
             "<a href=\"https://telegram.me/unobotupdates\">update channel</a>"
             " and buy an UNO card game.")

source_text = ("This bot is Free Software and licensed under the AGPL. "
               "The code is available here: \n"
               "https://github.com/jh0ker/mau_mau_bot")


@user_locale
def help(bot, update):
    """Handler for the /help command"""
    send_async(bot, update.message.chat_id, text=_(help_text),
               parse_mode=ParseMode.HTML, disable_web_page_preview=True)


@user_locale
def source(bot, update):
    """Handler for the /help command"""
    send_async(bot, update.message.chat_id, text=_(source_text),
               parse_mode=ParseMode.HTML, disable_web_page_preview=True)


@user_locale
def news(bot, update):
    """Handler for the /news command"""
    send_async(bot, update.message.chat_id,
               text=_("All news here: https://telegram.me/unobotupdates"),
               disable_web_page_preview=True)


dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('source', source))
dispatcher.add_handler(CommandHandler('news', news))
