import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types

from aiogram import Bot,Dispatcher
from aiogram.enums import ParseMode
from config import TOKEN
from handlers.cmd_handlers import cmd_admin_router
from handlers.msg_handlers import msg_admin_router
from aiogram.types import Message
from aiogram.filters import CommandStart,Command


from aiogram import Router

async def main():
    bot=Bot(token=TOKEN, parse_mode=ParseMode.HTML,disable_web_page_preview=True)
    dp=Dispatcher()

    dp.include_routers(cmd_admin_router, msg_admin_router)

    await dp.start_polling(bot)



if __name__=='__main__':
    logging.basicConfig(level=logging.INFO,stream=sys.stdout)
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:


        print("Bot stop")





