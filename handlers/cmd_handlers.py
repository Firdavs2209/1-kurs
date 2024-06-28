from aiogram import Router
from aiogram.filters import CommandStart,Command
from  aiogram.types import Message

from aiogram.fsm.context import FSMContext
from keyboards.keyboar import *
from states.states import Asosiy
from aiogram.types import FSInputFile,InputFile,InputMediaPhoto
from config import *


cmd_admin_router=Router()


@cmd_admin_router.message(CommandStart())
async def cmd_start(message:Message,state:FSMContext):
    print(message.from_user.id)
    s=(f"Assalomu aleykum!\n"
       f"Chirchiq davlat pedagogika universitetining Matematika va informatika fakulteti\n"
       f"Matematika va informatika yo'nalishining e-mustaqil ta'lim telegram botiga xush kelibsiz.")
    await message.answer(text=s, reply_markup=Bosh)
    await state.set_state(Asosiy.Bosh_sahifa)


@cmd_admin_router.message(Command("about"))
async def cmd_about(message:Message,state:FSMContext):
    s=(f"Bu bot Chirchiq davlat pedagogika universiteti Matematika va informatika fakultetining talabalariga mustaqil ta'limni"
       f" raqamlashtirish")
    await message.answer(text=s)
    await state.set_state(Asosiy.Bosh_sahifa)


@cmd_admin_router.message(Command("authors"))
async def cmd_about(message:Message,state:FSMContext):
    s=(f"<b>G`aniyev Ilhom Dustnazarovich: </b> Yoshlar bilan ishlash bo`yicha dekan o`rinbosari\n"
       f"<b>Jo'rayev Firdavs Umed o'g'li: </b> Matematika va informatika fakulteti 3-kurs talabasi")
    await message.answer(text=s)
    await state.set_state(Asosiy.Bosh_sahifa)









