from aiogram import Router,F
from aiogram.filters import and_f
from aiogram.types import Message, InputMediaPhoto
from keyboards.keyboar import *
from aiogram.types import FSInputFile
from states.states import *
from aiogram.fsm.context import FSMContext
from databse import tyutor_matematika1
from config import *
from aiogram import Bot

msg_admin_router=Router()
#---------------------------Bosh sahifa-------------------------------------------------------------------------------------------------------------


@msg_admin_router.message(and_f(F.text == "e-mustaqil ta'lim",Asosiy.Bosh_sahifa))
async def REKTOR(message: Message,state: FSMContext):
    await message.answer(text="Guruhni tanlang", reply_markup=Guruhlar)
    await state.set_state(Kurs.Birinchi_kurs)


#---------------------------- 1-guruh-------------------------------------------------------------------------------


@msg_admin_router.message(and_f(F.text == "23/1-guruh", Kurs.Birinchi_kurs))
async def REKTOR(message: Message, state: FSMContext):
    if message.from_user.id in admin_analiz:
        await message.answer(text="Mavzular bo'limiga o'tish uchun Mavzular tugmasini bosing", reply_markup=mustaqil_talim1_matanaliz)
        await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz)

        @msg_admin_router.message(and_f(F.text == "Mavzular", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Mavzuni tanglang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzular)

        @msg_admin_router.message(and_f(F.text == "Matematik analiz fanining predmeti. Haqiqiy sonlar to‘plami",
                                        Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzular))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Tanlang", reply_markup=admin())
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'limni tekshirish",
                                        Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="https://docs.google.com/forms/d/1urt1wclq38ABqzaXPq_49r2vJVMcgkkkG2n8FMlWRTE/edit#responses")
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1)



        @msg_admin_router.message(and_f(F.text == "Test natijalari",
                                        Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="https://docs.google.com/forms/d/19uFrS78-hhcwScqu2AcuM6BkGolHfddDniCTQ3ckaAE/edit#responses")
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'lim",
                                            Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Tanlang", reply_markup=mustaqil_talim)
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_Mustaqil)

        @msg_admin_router.message(and_f(F.text == "Ma'ruza matnini yuklash",
                                        Birinchi_guruhlar.Birinchi_guruh_Mustaqil))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="https://drive.google.com/drive/folders/1VwllhMW3JOFji4mtPhaPtfQUrfdWdOq6?usp=sharing")
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_Mustaqil)

        @msg_admin_router.message(and_f(F.text == "Amaliy mashg'ulotni yuklash",
                                        Birinchi_guruhlar.Birinchi_guruh_Mustaqil))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="https://drive.google.com/drive/folders/1FguX4jC0SXWt4JbzOMPdFcPjkpWxQ-zD")
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_Mustaqil)

        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'lim savollarini yuklash",
                                        Birinchi_guruhlar.Birinchi_guruh_Mustaqil))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="https://drive.google.com/drive/folders/18rRGFToE9VdhMWA4hBzClyhr5SLpAe6M")
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_Mustaqil)

        @msg_admin_router.message(and_f(F.text == "Video dars joylash",
                                        Birinchi_guruhlar.Birinchi_guruh_Mustaqil))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="https://t.me/matematik_analiz")
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_Mustaqil)







        @msg_admin_router.message(and_f(F.text == "Orqaga",
                                        Birinchi_guruhlar.Birinchi_guruh_Mustaqil))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Tanlang", reply_markup=mavzu1_admin)
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Talabalarni baholash",
                                        Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="https://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharing")
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Video dars joylash",
                                        Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(
                text="https://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharing")
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1)



        @msg_admin_router.message(and_f(F.text == "Mavzular ro'yhati",
                                        Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzular)

        @msg_admin_router.message(and_f(F.text == "Guruhlar",
                                        Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Guruhni tanlang", reply_markup=Guruhlar)
            await state.set_state(Kurs.Birinchi_kurs)
    else:
        await message.answer(text="Tanlang", reply_markup=guruh1)
        await state.set_state(Birinchi_guruhlar.Birinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Talabalar ro'yhati", Birinchi_guruhlar.Birinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    s=("1. Mamaraimova Sevinch Xamza qizi\n"
                    "2. Rimbayeva  Sevinch Ergashboy  qizi\n"
                    "3. Yo'ldoshev Otabek Shuhrat o'g'li\n"
                    "4. Amanov  Javlon Ulug'bek o'g'li\n"
                    "5. Nishonov  Sardor Ixtiyor o'g'li\n"
                    "6. Normirzayev Sardor Zayniddin o'g'li\n"
                    "7. Shokirova Saidabonu Narimon qizi\n"
                    "8. Ozodova Sarvinoz Laziz qizi\n"
                    "9. Abduraimova Muxlisa Ziyabiddin qizi\n"
                    "10. Boqiyeva Dilnavoz Dilmurod qizi\n"
                    "11. Muxammadiyeva E'zozoza  Maqsud qizi\n"
                    "12. Hikmatullayeva Latofat Zikrillo qizi\n"
                    "13. Amatov  Diyorbek Olloyor o'g'li\n"
                    "14. Ramazonova Nigora Ural qizi\n"
                    "15. Boltayeva  Marjona Olimjon qizi\n"
                    "16. Nuraliyeva Dauletgul Sherali qizi\n"
                    "17. Isroilova Nigora Iskandar qizi\n"
                    "18. Soipova Gulnora Hasan qizi\n"
                    "19. Fayzullayev Jasur Narimon o'g'li\n"
                    "20. Jalilova Sevinch Jasur qizi\n"
                    "21. Turdaliyeva Odina Ziyovuddin qizi\n"
                    "22. Jasanova  Aygerim  Fayzulla qizi\n"
                    "23. Agabekova Ak-Yerke Ulug'bek qizi\n"
                    "24. Kamolova Muhlisa Faxriddin qizi\n"
                    "25. Fayzullayeva Nodira Shuhrat qizi\n"
                    "26. Toliyev Rashid Rasul o'g'li\n"
                    "27. Kenjebayeva Maftuna Uktam qizi\n"
                    "28. Komiljonova Salomat Nurbek qizi\n"
                    "29. Ergashova Go'zal Elyor qizi")
                    await message.answer(text=s)
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Dars jadvali", Birinchi_guruhlar.Birinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    s=("<b>Dars jadvali</b>\n\n"
                       "<b>Seshanba</b>\n"
                       "1. Falsafa 120-xona\n"
                       "2. Umumiy  psixologiya 301-xona\n\n"
                       "<b>Chorshanba</b>\n"
                       "1. O'zbekistonning eng yangi tarixi 120-xona\n"
                       "2. O'zbekistonning eng yangi tarixi 312-xona\n\n"
                       "<b>Payshanba</b>\n"
                       "1. Algebra va sonlar nazariyasi 211-xona\n"
                       "2. Geometriya 305-xona\n"
                       "3. Matematik analiz 206-xona\n\n"
                       "<b>Juma</b>\n"
                       "1. Matematik analiz 201-xona\n"
                       "2. Geometriya 301-xona\n"
                       "3. Algebra va sonlar nazariyasi 201-xona\n\n"
                       "<b>Shanba</b>\n"
                       "1. Falsafa 206-xona\n"
                       "2. Axborot soati 211-xona\n"
                       "3. Umumiy psixologiya 310-xona"
                    )
                    await message.answer(text=s)
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh)

        @msg_admin_router.message(and_f(F.text == "Tyutor", Birinchi_guruhlar.Birinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    s = f"<b>{tyutor_matematika1[4]['ism']} :</b> \n" \
                        f"<b>Mutaxasisligi:</b> {tyutor_matematika1[4]['mutaxassisligi']} \n" \
                        f"<b>Biriktirilgan talabalari soni:</b> {tyutor_matematika1[4]['talabalar_soni']} nafar.\n" \
                        f"<b>Shundan: qizlar</b> - {tyutor_matematika1[4]['qiz']} nafar, o'g'il bolalar - {tyutor_matematika1[4]['yigit']} nafar.\n" \
                        f"<b>Davlat granti asosida o‘qiydiganlar</b> - {tyutor_matematika1[4]['grant']} nafar.\n" \
                        f"<b>To‘lov-kontrakt asosida o‘qiydiganlar</b> - {tyutor_matematika1[4]['kontrakt']} nafar.\n" \
                        f"<b>TTJ da yashaydiganlar</b> - {tyutor_matematika1[4]['ttj']} nafar.\n" \
                        f"<b>Ijarada yashaydiganlar</b> - {tyutor_matematika1[4]['ijara']} nafar.\n" \
                        f"<b>O'z uyida yashaydiganlar</b> - {tyutor_matematika1[4]['uyida']} nafar.\n" \
                        f"<b>Yaqin qarindoshinikida yashaydiganlar</b> - {tyutor_matematika1[4]['qarindosh']} nafar.\n" \
                        f"<b>Boquvchisi (otasi) ni yo‘qotganlar</b> - {tyutor_matematika1[4]['yetim']} nafar.\n" \
                        f"<b>Mehribonlik uyi tarbiyalanuvchilari</b> - {tyutor_matematika1[4]['mehribonlik']} nafar.\n" \
                        f"<b>Nogironligi bo‘lganlar</b> - {tyutor_matematika1[4]['nogiron']} nafar.\n" \
                        f"☎ {tyutor_matematika1[4]['tel']}"

                    await message.bot.send_media_group(chat_id=message.from_user.id, media=[InputMediaPhoto(
                        media=FSInputFile(r"D:\proyetlar\Proyektlar\1-kurs\img\MI nodir.png"), caption=s)])
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'lim", Birinchi_guruhlar.Birinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1)
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim)


        @msg_admin_router.message(and_f(F.text == "Matematik analiz", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz)
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz)


        @msg_admin_router.message(and_f(F.text == "Mavzular", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzular)


                #------------------------------------------ 1-mavzu-------------------------------------------------------------


        @msg_admin_router.message(and_f(F.text == "Matematik analiz fanining predmeti. Haqiqiy sonlar to‘plami", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzular))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=user())
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1)



        @msg_admin_router.message(
            and_f(F.text == "Ma'ruza", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="https://drive.google.com/drive/folders/1VwllhMW3JOFji4mtPhaPtfQUrfdWdOq6?usp=sharing"
            )
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Amaliyot", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="https://drive.google.com/drive/folders/1FguX4jC0SXWt4JbzOMPdFcPjkpWxQ-zD?usp=sharing")
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'lim misollari", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="https://drive.google.com/drive/folders/18rRGFToE9VdhMWA4hBzClyhr5SLpAe6M?usp=sharing")
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'limni yuklash", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Mustaqil ta'limni shu yerga joylang: \nhttps://forms.gle/W5cHUw3e9q4BpAaZA")
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "O'zlashtirish", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Siz quyidagi orqali matematik analiz fanidan o'zlashtirishingizni bilib oling: \nhttps://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharinghttps://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharing")
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Test savollari", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="1-mavzu uchun test savollari \nhttps://forms.gle/jEw8q1LdGaTKgy3X7")
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(
            and_f(F.text == "Video darslar", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="1-mavzu uchun test savollari \nhttps://forms.gle/jEw8q1LdGaTKgy3X7")
            await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1)







        '''
        @msg_admin_router.message(and_f(F.text == "Mavzular ro'yhati", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzular)


        @msg_admin_router.message(and_f(F.text == "Fanlar", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1)
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim)


        @msg_admin_router.message(and_f(F.text == "Guruh ma'lumotlari", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=guruh1)
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Guruh ma'lumotlari", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=guruh1)
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Guruhlar", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=Guruhlar)
                    await state.set_state(Birinchi_guruhlar.Birinchi_kurs)


        @msg_admin_router.message(and_f(F.text == "Video dars", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mavzu1_video)
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim_matanaliz_video1)


              '''







                #----------------------------------- 2-guruh-----------------------------------------------------------------------

@msg_admin_router.message(and_f(F.text == "23/2-guruh", Kurs.Birinchi_kurs))
async def REKTOR(message: Message, state: FSMContext):
    if message.from_user.id in admin_id:
        await message.answer(text="Mavzular bo'limiga o'tish uchun Mavzular tugmasini bosing",
                             reply_markup=mustaqil_talim1_matanaliz)
        await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz)

        @msg_admin_router.message(
            and_f(F.text == "Mavzular", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Mavzuni tanglang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
            await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzular)

        @msg_admin_router.message(and_f(F.text == "Matematik analiz fanining predmeti. Haqiqiy sonlar to‘plami",
                                        Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzular))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Tanlang", reply_markup=mavzu1_admin)
            await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'limni tekshirish",
                                        Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(
                text="https://docs.google.com/forms/d/1urt1wclq38ABqzaXPq_49r2vJVMcgkkkG2n8FMlWRTE/edit#responses")
            await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Test natijalari",
                                        Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(
                text="https://docs.google.com/forms/d/19uFrS78-hhcwScqu2AcuM6BkGolHfddDniCTQ3ckaAE/edit#responses")
            await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Talabalarni baholash",
                                        Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(
                text="https://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharing")
            await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Mavzular ro'yhati",
                                        Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
            await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzular)

        @msg_admin_router.message(and_f(F.text == "Guruhlar",
                                        Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Guruhni tanlang", reply_markup=Guruhlar)
            await state.set_state(Kurs.Birinchi_kurs)

    else:
        await message.answer(text="Tanlang", reply_markup=guruh1)
        await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh)

        @msg_admin_router.message(and_f(F.text == "Talabalar ro'yhati", Ikkinchi_guruhlar.Ikkinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    s=("1. Komiljonova Mehriniso O'tkirbek qizi\n"
                       "2. Mamaraimova Muborak Oloviddin qizi\n"
                       "3. Ro'zimurodov Farid Obid o'gli\n"
                       "4. Gadayev  Lazizbek Qahhar o'g'li\n"
                       "5. Abdijabborova Shodiyona To'lqin qizi\n"
                       "6. Temirova Momagul Erkin qizi\n"
                       "7. Kenjayeva  Xurshidabonu Tavakkal qizi\n"
                       "8. Rustamova Shahlobonu Adham qizi\n"
                       "9. Nematova Mahliyobonu Nurbek qizi\n"
                       "10. Shodmonova  Shahlobonu Bekzod qizi\n"
                       "11. Yangiboyev Sarvar Rahimjon o'g'li\n"
                       "12. Kulicheva  Charos Allaberdi qizi\n"
                       "13. Ravshanov  Shohruh Bahtiyor o'g'li\n"
                       "14. Sobirjonova Yoqutxon Xurshid qizi\n"
                       "15. Matyoqubova Munira Farid qizi\n"
                       "16. Akmalova Zebo Akmal qizi\n"
                       "17. Xaitbayeva Xusnida Xamid qizi\n"
                       "18. Jumabayeva Zuhra Baxtiyor qizi\n"
                       "19. Patillayev Ruslan Saydulla o'g'li\n"
                       "20. Normatova  Sevinch Baxtiyor qizi\n"
                       "21. Mexmonxo'jayeva Ruxshona Davron qizi\n"
                       "22. Jummurodova Iroda Ikrom qizi\n"
                       "23. Turisbekova Munira Nazarbek qizi\n"
                       "24. Qo'chqorov Bekzod Sherali o'g'li\n"
                       "25. Djangbayeva Muqaddas Saparbay qizi\n"
                       "26. Xudayberganova Ozoda Gulmirza qizi\n"
                       "27. Rajabova Olya Umidbek qizi\n"
                       "28. Umirbayeva Bonu Jamshid qizi\n"
                       "29. Jo'ldasbayev Aziz Mahmud o'gli\n"
                       "30. Berdibayeva Komila Botirbek qizi")
                    await message.answer(text=s)
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Dars jadvali", Ikkinchi_guruhlar.Ikkinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    s=("<b>Dars jadvali</b>\n\n"
                       "<b>Seshanba</b>\n"
                       "1. Falsafa 120-xona\n"
                       "2. Umumiy  psixologiya 301-xona\n\n"
                       "<b>Chorshanba</b>\n"
                       "1. O'zbekistonning eng yangi tarixi 120-xona\n"
                       "2. Axborot soati 208-xona\n"
                       "3. O'zbekistonning eng yangi tarixi 312-xona\n\n"
                       "<b>Payshanba</b>\n"
                       "1. Geometriya 305-xona\n"
                       "2. Algebra va sonlar nazariyasi 211-xona\n"
                       "3. Matematik analiz 208-xona\n\n"
                       "<b>Juma</b>\n"
                       "1. Matematik analiz 201-xona\n"
                       "2. Geometriya 301-xona\n"
                       "3. Algebra va sonlar nazariyasi 201-xona\n\n"
                       "<b>Shanba</b>\n"
                       "1. Umumiy psixologiya 310-xona\n"
                       "2. Falsafa 206-xona"
                    )
                    await message.answer(text=s)
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'lim", Ikkinchi_guruhlar.Ikkinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1)
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim)


        @msg_admin_router.message(and_f(F.text == "Matematik analiz", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz)
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz)


        @msg_admin_router.message(and_f(F.text == "Mavzular", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzular)


                #------------------------------------------ 1-mavzu-------------------------------------------------------------


        @msg_admin_router.message(and_f(F.text == "Matematik analiz fanining predmeti. Haqiqiy sonlar to‘plami", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzular))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mavzu1)
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Ma'ruza", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply_document(document=FSInputFile(path="D://proyetlar//1-kurs//Matanaliz//1-mavzu//1-maruza.pdf", filename="1-maruza.pdf"))

                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Amaliyot", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply_document(document=FSInputFile(path="D://proyetlar//1-kurs//Matanaliz//1-mavzu//1-maruza.pdf", filename="1-maruza.pdf"))
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'lim misollari", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply_document(document=FSInputFile(path="D://proyetlar//1-kurs//Matanaliz//1-mavzu//1-maruza.pdf", filename="1-maruza.pdf"))
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'limni yuklash", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Mustaqil ta'limni shu yerga joylang: \nhttps://forms.gle/W5cHUw3e9q4BpAaZA")
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "O'zlashtirish", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Siz quyidagi orqali matematik analiz fanidan o'zlashtirishingizni bilib oling: \nhttps://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharinghttps://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharing")
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Test savollari", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="1-mavzu uchun test savollari \nhttps://forms.gle/jEw8q1LdGaTKgy3X7")
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Mavzular ro'yhati", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzular)


        @msg_admin_router.message(and_f(F.text == "Fanlar", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1)
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim)


        @msg_admin_router.message(and_f(F.text == "Guruh ma'lumotlari", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=guruh1)
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh)



        @msg_admin_router.message(and_f(F.text == "Guruhlar", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=Guruhlar)
                    await state.set_state(Kurs.Birinchi_kurs)


        @msg_admin_router.message(and_f(F.text == "Video dars", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mavzu1_video)
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_video1)


        @msg_admin_router.message(and_f(F.text == "Telegram", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_video1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply("https://t.me/+2yLVqynxfSY2MDA6")


        @msg_admin_router.message(and_f(F.text == "You Tube", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_video1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply("https://t.me/CHDPUMIfakulteti")


        @msg_admin_router.message(and_f(F.text == "Orqaga", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_video1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mavzu1)
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz_mavzu1)





                #----------------------------------- 3-guruh-----------------------------------------------------------------------


@msg_admin_router.message(and_f(F.text == "23/3-guruh", Kurs.Birinchi_kurs))
async def REKTOR(message: Message, state: FSMContext):
    if message.from_user.id in admin_id:
        await message.answer(text="Mavzular bo'limiga o'tish uchun Mavzular tugmasini bosing",
                             reply_markup=mustaqil_talim1_matanaliz)
        await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz)

        @msg_admin_router.message(
            and_f(F.text == "Mavzular", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Mavzuni tanglang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
            await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzular)

        @msg_admin_router.message(and_f(F.text == "Matematik analiz fanining predmeti. Haqiqiy sonlar to‘plami",
                                        Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzular))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Tanlang", reply_markup=mavzu1_admin)
            await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'limni tekshirish",
                                        Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(
                text="https://docs.google.com/forms/d/1urt1wclq38ABqzaXPq_49r2vJVMcgkkkG2n8FMlWRTE/edit#responses")
            await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Test natijalari",
                                        Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(
                text="https://docs.google.com/forms/d/19uFrS78-hhcwScqu2AcuM6BkGolHfddDniCTQ3ckaAE/edit#responses")
            await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Talabalarni baholash",
                                        Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(
                text="https://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharing")
            await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Mavzular ro'yhati",
                                        Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
            await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzular)

        @msg_admin_router.message(and_f(F.text == "Guruhlar",
                                        Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Guruhni tanlang", reply_markup=Guruhlar)
            await state.set_state(Kurs.Birinchi_kurs)

    else:

        await message.answer(text="Tanlang", reply_markup=guruh1)
        await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Talabalar ro'yhati", Uchinchi_guruhlar.Uchinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    s=("1. Sattarova Maxsuda Anvarjon qizi\n"
                       "2. Kamiljanova Jayrona Oybek qizi\n"
                       "3. Fayzullayev Xursand Muzaffar o'g'li\n"
                       "4. Baltabayeva  Sohiba Anvarjon qizi\n"
                       "5. Shukrullayeva Guli Rustamboy qizi\n"
                       "6. Adamboyeva Marjona Qahramon qizi\n"
                       "7. Nosirov Muhammad Jumanazar o'g'li\n"
                       "8. Atoyeva Gulzoda Anvarjon qizi\n"
                       "9. Davletova  Selbi Shuhrat qizi\n"
                       "10. Abrayev Mirzohid Komil o'g'li\n"
                       "11. Bozorboyeva Guli Jo'rabek qizi\n"
                       "12. Azamatova Ruxsora Olimjon qizi\n"
                       "13. G'ofurova  Ruxshona Nodirjon qizi\n"
                       "14. O'ngboyev Dilshod Ahror o'gli\n"
                       "15. Muhsinova Durdona Mar'uf qizi\n"
                       "16. Ro'zimurodov Bexruz Farxod o'g'li\n"
                       "17. Qudratullayeva Sarvinoz Xikmatllo qizi\n"
                       "18. Hamdamova Durdona Shavkat qizi\n"
                       "19. Po'latova Feruza Nasriddin qizi\n"
                       "20. Xudoynazarova Kamola Umar qizi\n"
                       "21. Amirov  Samandar Husan o'g'li\n"
                       "22. Turdimatova Nozimaxon Ulug'bek qizi\n"
                       "23. Isomiddinova Gulira'no Zayniddin qizi\n"
                       "24. Anarov Bekmurod Dilmurod o'g'li\n"
                       "25. Aglamova Mahliyobonu Aziz qizi\n"
                       "26. Ahmadjonova E'zoza Xusan qizi\n"
                       "27. Abdiraximov  Abduqahhor Abdurahsid o'g'li\n"
                       "28. Bo'tayev Jamshid Agzam o'g'li\n"
                       "29. Suleymanova Dilshoda Saydulla qizi\n"
                       "30. Ibragimova Ozoda Ulug'bek qizi\n"
                       "31. Orazbayeva Nilufar Dariyabay qizi\n"
                       "32. Yo'ldahsev  Otaxon Hamid o'g'li")
                    await message.answer(text=s)
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Dars jadvali", Uchinchi_guruhlar.Uchinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    s=("<b>Dars jadvali</b>\n\n"
                       "<b>Seshanba</b>\n"
                       "1. Umumiy  psixologiya 301-xona\n"
                       "2. Falsafa 120-xona\n"
                       "3. Falsafa 206-xona\n"
                       "<b>Chorshanba</b>\n"
                       "1. Algebra va sonlar nazariyasi 301-xona\n"
                       "2. Geometriya 210-xona\n"
                       "3. Axborot soati 112-xona\n"
                       "4. O'zbekistonning eng yangi tarixi 313-xona\n\n"
                       "<b>Payshanba</b>\n"
                       "1. O'zbekistonning eng yangi tarixi 201-xona\n"
                       "2. Matematik analiz 208-xona\n"
                       "3. Algebra va sonlar nazariyasi 211-xona\n\n"
                       "<b>Juma</b>\n"
                       "1. Geometriya 301-xona\n"
                       "2. Matematik analiz 201-xona\n"
                       "3. Umumiy psixologiya 310-xona"
                    )
                    await message.answer(text=s)
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'lim", Uchinchi_guruhlar.Uchinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1)
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim)


        @msg_admin_router.message(and_f(F.text == "Matematik analiz", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz)
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz)


        @msg_admin_router.message(and_f(F.text == "Mavzular", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzular)


                #------------------------------------------ 1-mavzu-------------------------------------------------------------


        @msg_admin_router.message(and_f(F.text == "Matematik analiz fanining predmeti. Haqiqiy sonlar to‘plami", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzular))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mavzu1)
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Ma'ruza", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply_document(document=FSInputFile(path="D://proyetlar//1-kurs//Matanaliz//1-mavzu//1-maruza.pdf", filename="1-maruza.pdf"))

                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Amaliyot", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply_document(document=FSInputFile(path="D://proyetlar//1-kurs//Matanaliz//1-mavzu//1-maruza.pdf", filename="1-maruza.pdf"))
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'lim misollari", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply_document(document=FSInputFile(path="D://proyetlar//1-kurs//Matanaliz//1-mavzu//1-maruza.pdf", filename="1-maruza.pdf"))
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'limni yuklash", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Mustaqil ta'limni shu yerga joylang: \nhttps://forms.gle/W5cHUw3e9q4BpAaZA")
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "O'zlashtirish", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Siz quyidagi orqali matematik analiz fanidan o'zlashtirishingizni bilib oling: \nhttps://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharinghttps://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharing")
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Test savollari", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="1-mavzu uchun test savollari \nhttps://forms.gle/jEw8q1LdGaTKgy3X7")
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Mavzular ro'yhati", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzular)


        @msg_admin_router.message(and_f(F.text == "Fanlar", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1)
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim)


        @msg_admin_router.message(and_f(F.text == "Guruh ma'lumotlari", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=guruh1)
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh)



        @msg_admin_router.message(and_f(F.text == "Guruhlar", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=Guruhlar)
                    await state.set_state(Kurs.Birinchi_kurs)


        @msg_admin_router.message(and_f(F.text == "Video dars", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mavzu1_video)
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_video1)


        @msg_admin_router.message(and_f(F.text == "Telegram", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_video1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply("https://t.me/+2yLVqynxfSY2MDA6")


        @msg_admin_router.message(and_f(F.text == "You Tube", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_video1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply("https://t.me/CHDPUMIfakulteti")


        @msg_admin_router.message(and_f(F.text == "Orqaga", Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_video1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mavzu1)
                    await state.set_state(Uchinchi_guruhlar.Uchinchi_guruh_mustaqil_talim_matanaliz_mavzu1)





                #----------------------------------- 4-guruh-----------------------------------------------------------------------


@msg_admin_router.message(and_f(F.text == "23/4-guruh", Kurs.Birinchi_kurs))
async def REKTOR(message: Message, state: FSMContext):
    if message.from_user.id in admin_id:
        await message.answer(text="Mavzular bo'limiga o'tish uchun Mavzular tugmasini bosing",
                             reply_markup=mustaqil_talim1_matanaliz)
        await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz)

        @msg_admin_router.message(
            and_f(F.text == "Mavzular", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Mavzuni tanglang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
            await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzular)

        @msg_admin_router.message(and_f(F.text == "Matematik analiz fanining predmeti. Haqiqiy sonlar to‘plami",
                                        Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzular))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Tanlang", reply_markup=mavzu1_admin)
            await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'limni tekshirish",
                                        Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(
                text="https://docs.google.com/forms/d/1urt1wclq38ABqzaXPq_49r2vJVMcgkkkG2n8FMlWRTE/edit#responses")
            await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Test natijalari",
                                        Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(
                text="https://docs.google.com/forms/d/19uFrS78-hhcwScqu2AcuM6BkGolHfddDniCTQ3ckaAE/edit#responses")
            await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Talabalarni baholash",
                                        Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(
                text="https://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharing")
            await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Mavzular ro'yhati",
                                        Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
            await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzular)

        @msg_admin_router.message(and_f(F.text == "Guruhlar",
                                        Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Guruhni tanlang", reply_markup=Guruhlar)
            await state.set_state(Kurs.Birinchi_kurs)

    else:
        await message.answer(text="Tanlang", reply_markup=guruh1)
        await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Talabalar ro'yhati", Tortinchi_guruhlar.Tortinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    s=("1. Saidaliyeva  Nozanin Davlatboy qizi\n"
                       "2. Islamov Nurtilek Daulet o'g'li\n"
                       "3. Erkabayeva Shodiya Maxmud qizi\n"
                       "4. Qo'shanova Surayyo Olimboy qizi\n"
                       "5. Aralov O'tkir Erkin o'g'li\n"
                       "6. Abdusalimova Munisa Baxtiyor qizi\n"
                       "7. Xudoyberdiyev Davlat Dilmurod o'g'li\n"
                       "8. Toshboyeva Durdona Abdusodiq qizi\n"
                       "9. Ismoilova Ra'no Alisher qizi\n"
                       "10. Tojiyeva Durdona Panji qizi\n"
                       "11. Nomozova Zarina Akbar qizi\n"
                       "12. Usmonova Rayyona Yusufbek qizi\n"
                       "13. Qo'yliyeva Sarvara Ro'zimurod qizi\n"
                       "14. Tohirova Bahor Sherzod qizi\n"
                       "15. Ashurova Gulnoza Sattor qizi\n"
                       "16. Qurbonboyeva Sevara San'at qizi\n"
                       "17. Norquliyeva Sevinch Furqat qizi\n"
                       "18. Butanova Mardona Gulmirza qizi\n"
                       "19. Qadamboyeva Nafosat Ozodboy qizi\n"
                       "20. Asadullayeva Dilmira Avaz qizi\n"
                       "21. Tagayeva Aliya Daniyar qizi\n"
                       "22. Begmatova Bonu Bexzod qizi\n"
                       "23. Sobirjonova Sarvinoz Asqar qizi\n"
                       "24. Abdualiyeva Feruza Elmurod qizi\n"
                       "25. Achilov Jaxongir O'tkirbek o'g'li\n"
                       "26. Eshimbetova Kumushoy Shuhrat qizi\n"
                       "27. Gulimboyeva Shoira Quvvatboy qizi\n"
                       "28. Alimjanov  Ro'zmat Fahriddin o'g'li\n"
                       "29. Axmedov Maxmuddo'st To'lqin o'g'li\n"
                       "30. Muhammadiyev Mehriddin Vali o'g'li\n"
                       "31. Eshmurotova Quyonchoy  Qo'ziboy qizi")
                    await message.answer(text=s)
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Dars jadvali", Tortinchi_guruhlar.Tortinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    s=("<b>Dars jadvali</b>\n\n"
                       "<b>Seshanba</b>\n"
                       "1. Umumiy  psixologiya 301-xona\n"
                       "2. Falsafa 120-xona\n"
                       "3. Matematik analiz 208-xona\n"
                       "<b>Chorshanba</b>\n"
                       "1. Algebra va sonlar nazariyasi 301-xona\n"
                       "2. \n"
                       "3. Geometriya 210-xona\n\n"
                       "<b>Payshanba</b>\n"
                       "1. O'zbekistonning eng yangi tarixi 201-xona\n"
                       "2. O'zbekistonning eng yangi tarixi 206-xona\n"
                       "3. Algebra va sonlar nazariyasi 211-xona\n\n"
                       "<b>Juma</b>\n"
                       "1. Geometriya 301-xona\n"
                       "2. Matematik analiz 201-xona\n"
                       "3. Axborot soati 113-xona\n\n"
                       "<b>Shanba</b>\n"
                       "1. Algebra va sonlar nazariyasi 208-xona\n"
                       "2. Umumiy psixologiya 310-xona\n"
                       "3. Falsafa 206-xona"
                    )
                    await message.answer(text=s)
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'lim", Tortinchi_guruhlar.Tortinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1)
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim)


        @msg_admin_router.message(and_f(F.text == "Matematik analiz", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz)
                    await state.set_state(Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz)


        @msg_admin_router.message(and_f(F.text == "Mavzular", Ikkinchi_guruhlar.Ikkinchi_guruh_mustaqil_talim_matanaliz))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzular)


                #------------------------------------------ 1-mavzu-------------------------------------------------------------


        @msg_admin_router.message(and_f(F.text == "Matematik analiz fanining predmeti. Haqiqiy sonlar to‘plami", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzular))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mavzu1)
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Ma'ruza", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply_document(document=FSInputFile(path="D://proyetlar//1-kurs//Matanaliz//1-mavzu//1-maruza.pdf", filename="1-maruza.pdf"))

                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Amaliyot", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply_document(document=FSInputFile(path="D://proyetlar//1-kurs//Matanaliz//1-mavzu//1-maruza.pdf", filename="1-maruza.pdf"))
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'lim misollari", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply_document(document=FSInputFile(path="D://proyetlar//1-kurs//Matanaliz//1-mavzu//1-maruza.pdf", filename="1-maruza.pdf"))
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'limni yuklash", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Mustaqil ta'limni shu yerga joylang: \nhttps://forms.gle/W5cHUw3e9q4BpAaZA")
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "O'zlashtirish", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Siz quyidagi orqali matematik analiz fanidan o'zlashtirishingizni bilib oling: \nhttps://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharinghttps://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharing")
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Test savollari", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="1-mavzu uchun test savollari \nhttps://forms.gle/jEw8q1LdGaTKgy3X7")
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Mavzular ro'yhati", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzular)


        @msg_admin_router.message(and_f(F.text == "Fanlar", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1)
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim)


        @msg_admin_router.message(and_f(F.text == "Guruh ma'lumotlari", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=guruh1)
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh)




        @msg_admin_router.message(and_f(F.text == "Guruhlar", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=Guruhlar)
                    await state.set_state(Kurs.Birinchi_kurs)


        @msg_admin_router.message(and_f(F.text == "Video dars", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mavzu1_video)
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Telegram", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply("https://t.me/+2yLVqynxfSY2MDA6")


        @msg_admin_router.message(and_f(F.text == "You Tube", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply("https://t.me/CHDPUMIfakulteti")


        @msg_admin_router.message(and_f(F.text == "Orqaga", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mavzu1)
                    await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)




                #----------------------------------- 5-guruh-----------------------------------------------------------------------


@msg_admin_router.message(and_f(F.text == "23/5-guruh", Kurs.Birinchi_kurs))
async def REKTOR(message: Message, state: FSMContext):
    if message.from_user.id in admin_id:
        await message.answer(text="Mavzular bo'limiga o'tish uchun Mavzular tugmasini bosing",
                             reply_markup=mustaqil_talim1_matanaliz)
        await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz)

        @msg_admin_router.message(
            and_f(F.text == "Mavzular", Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Mavzuni tanglang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
            await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzular)

        @msg_admin_router.message(and_f(F.text == "Matematik analiz fanining predmeti. Haqiqiy sonlar to‘plami",
                                        Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzular))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Tanlang", reply_markup=mavzu1_admin)
            await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'limni tekshirish",
                                        Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(
                text="https://docs.google.com/forms/d/1urt1wclq38ABqzaXPq_49r2vJVMcgkkkG2n8FMlWRTE/edit#responses")
            await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Test natijalari",
                                        Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(
                text="https://docs.google.com/forms/d/19uFrS78-hhcwScqu2AcuM6BkGolHfddDniCTQ3ckaAE/edit#responses")
            await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Talabalarni baholash",
                                        Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(
                text="https://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharing")
            await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1)

        @msg_admin_router.message(and_f(F.text == "Mavzular ro'yhati",
                                        Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
            await state.set_state(Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzular)

        @msg_admin_router.message(and_f(F.text == "Guruhlar",
                                        Tortinchi_guruhlar.Tortinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
            await message.answer(text="Guruhni tanlang", reply_markup=Guruhlar)
            await state.set_state(Kurs.Birinchi_kurs)
    else:

        await message.answer(text="Tanlang", reply_markup=guruh1)
        await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Talabalar ro'yhati", Beshinchi_guruhlar.Beshinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    s=("1. Komiljonova Mehriniso O'tkirbek qizi\n"
                       "2. Mamaraimova Muborak Oloviddin qizi\n"
                       "3. Ro'zimurodov Farid Obid o'gli\n"
                       "4. Gadayev  Lazizbek Qahhar o'g'li\n"
                       "5. Abdijabborova Shodiyona To'lqin qizi\n"
                       "6. Temirova Momagul Erkin qizi\n"
                       "7. Kenjayeva  Xurshidabonu Tavakkal qizi\n"
                       "8. Rustamova Shahlobonu Adham qizi\n"
                       "9. Nematova Mahliyobonu Nurbek qizi\n"
                       "10. Shodmonova  Shahlobonu Bekzod qizi\n"
                       "11. Yangiboyev Sarvar Rahimjon o'g'li\n"
                       "12. Kulicheva  Charos Allaberdi qizi\n"
                       "13. Ravshanov  Shohruh Bahtiyor o'g'li\n"
                       "14. Sobirjonova Yoqutxon Xurshid qizi\n"
                       "15. Matyoqubova Munira Farid qizi\n"
                       "16. Akmalova Zebo Akmal qizi\n"
                       "17. Xaitbayeva Xusnida Xamid qizi\n"
                       "18. Jumabayeva Zuhra Baxtiyor qizi\n"
                       "19. Patillayev Ruslan Saydulla o'g'li\n"
                       "20. Normatova  Sevinch Baxtiyor qizi\n"
                       "21. Mexmonxo'jayeva Ruxshona Davron qizi\n"
                       "22. Jummurodova Iroda Ikrom qizi\n"
                       "23. Turisbekova Munira Nazarbek qizi\n"
                       "24. Qo'chqorov Bekzod Sherali o'g'li\n"
                       "25. Djangbayeva Muqaddas Saparbay qizi\n"
                       "26. Xudayberganova Ozoda Gulmirza qizi\n"
                       "27. Rajabova Olya Umidbek qizi\n"
                       "28. Umirbayeva Bonu Jamshid qizi\n"
                       "29. Jo'ldasbayev Aziz Mahmud o'gli\n"
                       "30. Berdibayeva Komila Botirbek qizi")
                    await message.answer(text=s)
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Dars jadvali", Beshinchi_guruhlar.Beshinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    s=("<b>Dars jadvali</b>\n\n"
                       "<b>Seshanba</b>\n"
                       "1. Umumiy  psixologiya 112-xona\n"
                       "2. Umumiy  psixologiya 206-xona\n"
                       "3. Algebra va sonlar nazariyasi 210-xona\n\n"
                       "<b>Chorshanba</b>\n"
                       "1. \n"
                       "2. Geometriya 310-xona\n"
                       "3. \n\n"
                       "<b>Payshanba</b>\n"
                       "1. Axborot soati 208-xona\n"
                       "2. Geometriya 310-xona\n\n"
                       "<b>Juma</b>\n"
                       "1. Falsafa 210-xona\n"
                       "2. Matematik analiz 206-xona\n"
                       "3. Matematik analiz 206-xona\n"
                       "4. Falsafa 206-xona\n\n"
                       "<b>Shanba</b>\n"
                       "1. Algebra va sonlar nazariyasi 210-xona\n"
                       "2. O'zbekistonning eng yangi tarixi 312-xona\n"
                       "3. O'zbekistonning eng yangi tarixi 312-xona"
                    )
                    await message.answer(text=s)
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'lim", Beshinchi_guruhlar.Beshinchi_guruh))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1)
                    await state.set_state(Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim)


        @msg_admin_router.message(and_f(F.text == "Matematik analiz", Birinchi_guruhlar.Birinchi_guruh_mustaqil_talim))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz)
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz)


        @msg_admin_router.message(and_f(F.text == "171", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzular)


                #------------------------------------------ 1-mavzu-------------------------------------------------------------


        @msg_admin_router.message(and_f(F.text == "Matematik analiz fanining predmeti. Haqiqiy sonlar to‘plami", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzular))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mavzu1)
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Ma'ruza", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply_document(document=FSInputFile(path="D://proyetlar//1-kurs//Matanaliz//1-mavzu//1-maruza.pdf", filename="1-maruza.pdf"))

                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Amaliyot", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply_document(document=FSInputFile(path="D://proyetlar//1-kurs//Matanaliz//1-mavzu//1-maruza.pdf", filename="1-maruza.pdf"))
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'lim misollari", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply_document(document=FSInputFile(path="D://proyetlar//1-kurs//Matanaliz//1-mavzu//1-maruza.pdf", filename="1-maruza.pdf"))
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Mustaqil ta'limni yuklash", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Mustaqil ta'limni shu yerga joylang: \nhttps://forms.gle/W5cHUw3e9q4BpAaZA")
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "O'zlashtirish", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Siz quyidagi orqali matematik analiz fanidan o'zlashtirishingizni bilib oling: \nhttps://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharinghttps://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharing")
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Test savollari", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="1-mavzu uchun test savollari \nhttps://forms.gle/jEw8q1LdGaTKgy3X7")
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1)


        @msg_admin_router.message(and_f(F.text == "Mavzular ro'yhati", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1_matanaliz_mavzular)
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzular)


        @msg_admin_router.message(and_f(F.text == "Fanlar", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mustaqil_talim1)
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim)


        @msg_admin_router.message(and_f(F.text == "Guruh ma'lumotlari", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=guruh1)
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh)




        @msg_admin_router.message(and_f(F.text == "Guruhlar", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=Guruhlar)
                    await state.set_state(Kurs.Birinchi_kurs)


        @msg_admin_router.message(and_f(F.text == "Video dars", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mavzu1_video)
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_video1)


        @msg_admin_router.message(and_f(F.text == "Telegram", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_video1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply("https://t.me/+2yLVqynxfSY2MDA6")



        @msg_admin_router.message(and_f(F.text == "You Tube", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_video1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.reply("https://t.me/CHDPUMIfakulteti")


        @msg_admin_router.message(and_f(F.text == "Orqaga", Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_video1))
        async def REKTOR(message: Message, state: FSMContext):
                    await message.answer(text="Tanlang", reply_markup=mavzu1)
                    await state.set_state(Beshinchi_guruhlar.Beshinchi_guruh_mustaqil_talim_matanaliz_mavzu1)
