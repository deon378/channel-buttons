#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#basic version

import asyncio
import os
import sqlite3
import time

from sample_config import Config
from translation import Translation

import pyrogram
from pyrogram import Client, Filters, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait


@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_MSG,
    )
   


@pyrogram.Client.on_message(pyrogram.Filters.document)
async def old(client, message):
    await client.edit_message_reply_markup(
        chat_id=message.chat.id,
        message_id=message.message_id,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('⭕️ѕнαяє ϲнαииєℓ⭕️', url='https://t.me/share/url?url=join%20our%20channels%20to%20get%20a%20collection%20of%20channels%20with%20daily%20updates%20https://t.me/qMp_Links')],
            ]  
        )
    )
    
  
        
    
                          
