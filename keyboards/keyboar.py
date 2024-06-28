from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram import types

Bosh=ReplyKeyboardMarkup(

    keyboard=[
    [KeyboardButton(text="e-mustaqil ta'lim")]
],
resize_keyboard=True)


Guruhlar=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="23/1-guruh"),
         KeyboardButton(text="23/2-guruh")],
        [KeyboardButton(text="23/3-guruh"),
         KeyboardButton(text="23/4-guruh")],
        [KeyboardButton(text="23/5-guruh")]

    ],
resize_keyboard=True
)

guruh1=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Talabalar ro'yhati"),
         KeyboardButton(text="Tyutor")],
         [KeyboardButton(text="Dars jadvali"),
          KeyboardButton(text="Mustaqil ta'lim")],
         [KeyboardButton(text="Orqaga")]
    ],
resize_keyboard=True
)



mustaqil_talim1=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Matematik analiz"),
         KeyboardButton(text="Algebra va sonlar nazariyasi")],
        [KeyboardButton(text="Geometriya"),
         KeyboardButton(text="Orqaga")],
        [KeyboardButton(text="Bosh sahifa")]
    ],
resize_keyboard=True
)

mustaqil_talim1_matanaliz=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Mavzular")]
    ],
    resize_keyboard=True
)

mustaqil_talim1_matanaliz_mavzular=ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="Matematik analiz fanining predmeti. Haqiqiy sonlar to‘plami"),
             KeyboardButton(text="Yaqinlashuvchi ketma-ketliklar ularning xossalari")],
            [KeyboardButton(text="Yaqinlashish prinsipi"),
             KeyboardButton(text="Bir o‘zgaruvchili funksiya va uning xossalari")],
            [KeyboardButton(text="Funksiyaning limitining ta’riflari"),
             KeyboardButton(text="Limitga ega bo‘lgan funksiyaning xossalari")],
            [KeyboardButton(text="Uzluksiz funksiya va uning xossalari"),
             KeyboardButton(text="Kesmada uzluksiz bo‘lgan funksiyalarning  xossalari")],
            [KeyboardButton(text="Bir o‘zgaruvchili funksiyaning hosilasi"),
             KeyboardButton(text="Hosilani hisoblash qoidalari")],
            [KeyboardButton(text="Funksiyaning differensiali"),
             KeyboardButton(text="Yuqori tartibli hosila va differensiallar")],
            [KeyboardButton(text="Differensial hisobning asosiy teoremalari"),
             KeyboardButton(text="Hosilaning tatbiqlari")],
            [KeyboardButton(text="Hosila yordamida funksiyani to‘la tekshirish"),
             KeyboardButton(text="Aniqmas integral va uni topishning sodda usullari")],
            [KeyboardButton(text="Ratsional funksiyalarni integrallash"),
             KeyboardButton(text="Sodda irratsional va transsendent funksiyalarni integrallash")],
            [KeyboardButton(text="Aniq integralning  ta’rifi.  Aniq integral mavjud bo‘lishining zaruriy va yetarli shartlari"),
             KeyboardButton(text="Integrallanuvchi funksiyalar sinfi.  Aniq integralning xossalari")],
            [KeyboardButton(text="Aniq integralni  hisoblash usullari"),
             KeyboardButton(text="Chegaralari cheksiz  xosmas integrallar")],
            [KeyboardButton(text="Chegaralanmagan funksiyaning xosmas integrali"),
             KeyboardButton(text="Aniq integralning geometrik kattaliklarni hisoblashga  tatbiqlari. Aniq integralning mexanika va fizikaga tatbiqlari")],
            [KeyboardButton(text="Yaqinlashuvchi sonli qatorlar va ularning xossalari"),
             KeyboardButton(text="Musbat hadli qatorlar")],
            [KeyboardButton(text="Ixtiyoriy hadli qatorlar"),
             KeyboardButton(text="Funksional ketma-ketliklar. Tekis yaqinlashuvchi funksional ketma-ketliklarning xossalari")],
            [KeyboardButton(text="Funksional qatorlar. Tekis yaqinlashuvchi funksional qatorlarning  xossalari"),
             KeyboardButton(text="Darajali qatorlar. Teylor qatori")]
    ],
    resize_keyboard=True
)

mavzu1=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ma'ruza"),
         KeyboardButton(text="Amaliyot")],
        [KeyboardButton(text="Video dars"),
         KeyboardButton(text="Mustaqil ta'lim misollari")],
        [KeyboardButton(text="Mustaqil ta'limni yuklash"),
         KeyboardButton(text="O'zlashtirish")],
        [KeyboardButton(text="Test savollari"),
         KeyboardButton(text="Mavzular ro'yhati")],
        [KeyboardButton(text="Fanlar"),
         KeyboardButton(text="Guruh ma'lumotlari")],
        [KeyboardButton(text="Guruhlar")]
    ],
    resize_keyboard=True
)

def user():
    button1=[InlineKeyboardButton(text="Ma'ruza",url="https://drive.google.com/drive/folders/1VwllhMW3JOFji4mtPhaPtfQUrfdWdOq6?usp=sharing"),
        InlineKeyboardButton(text="Amaliyot",url="https://drive.google.com/drive/folders/1FguX4jC0SXWt4JbzOMPdFcPjkpWxQ-zD?usp=sharing")
    ]
    button2=[InlineKeyboardButton(text="Mustaqil ta'lim misollari",url="https://drive.google.com/drive/folders/18rRGFToE9VdhMWA4hBzClyhr5SLpAe6M?usp=sharing"),
        InlineKeyboardButton(text="Mustaqil ta'limni yuklash",url="https://forms.gle/W5cHUw3e9q4BpAaZA")
    ]

    button3 = [InlineKeyboardButton(text="O'zlashtirish",
                                    url="https://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharinghttps://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharing"),
               InlineKeyboardButton(text="Test savollari", url="https://forms.gle/jEw8q1LdGaTKgy3X7")
               ]

    button4=[InlineKeyboardButton(text="Video darslar", url="https://t.me/matematik_analiz/5")]

    buttons=[button1,button2,button3,button4]

    markup=InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return markup


def admin():
    button1 = [InlineKeyboardButton(text="Mustaqil ta'limni tekshirish",
                                    url="https://docs.google.com/forms/d/1urt1wclq38ABqzaXPq_49r2vJVMcgkkkG2n8FMlWRTE/edit#responses"),
               InlineKeyboardButton(text="Test natijalari",
                                    url="https://docs.google.com/forms/d/19uFrS78-hhcwScqu2AcuM6BkGolHfddDniCTQ3ckaAE/edit#responses")
               ]
    button2 = [InlineKeyboardButton(text="Ma'ruza matnini yuklash",
                                    url="https://drive.google.com/drive/folders/1VwllhMW3JOFji4mtPhaPtfQUrfdWdOq6"),
               InlineKeyboardButton(text="Amaliy mashg'ulotni yuklash", url="https://drive.google.com/drive/folders/1FguX4jC0SXWt4JbzOMPdFcPjkpWxQ-zD")
               ]

    button3 = [InlineKeyboardButton(text="Mustaqil ta'lim savollarini yuklash",
                                    url="https://drive.google.com/drive/folders/18rRGFToE9VdhMWA4hBzClyhr5SLpAe6M"),
               InlineKeyboardButton(text="Talabalarni baholash", url="https://docs.google.com/spreadsheets/d/1G7o6khX9Di9yGcaha8ehGr1OcRnL74xLqZyw7DwuNSA/edit?usp=sharing")
               ]

    button4=[InlineKeyboardButton(text="Video dars joylash", url="https://t.me/matematik_analiz")]

    buttons = [button1, button2, button3,button4]

    markup = InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return markup


mavzu1_video=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Telegram"),
         KeyboardButton(text="You Tube")],
        [KeyboardButton(text="Orqaga")]
    ],
    resize_keyboard=True
)

guruh1=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Talabalar ro'yhati"),
         KeyboardButton(text="Tyutor")],
         [KeyboardButton(text="Dars jadvali"),
          KeyboardButton(text="Mustaqil ta'lim")],
         [KeyboardButton(text="Orqaga")]
    ],
resize_keyboard=True
)



mustaqil_talim1=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Matematik analiz"),
         KeyboardButton(text="Algebra va sonlar nazariyasi")],
        [KeyboardButton(text="Geometriya"),
         KeyboardButton(text="Orqaga")],
        [KeyboardButton(text="Bosh sahifa")]
    ],
resize_keyboard=True
)

mustaqil_talim1_matanaliz=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Mavzular")]
    ],
    resize_keyboard=True
)

mustaqil_talim1_matanaliz_mavzular=ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="Matematik analiz fanining predmeti. Haqiqiy sonlar to‘plami"),
             KeyboardButton(text="Yaqinlashuvchi ketma-ketliklar ularning xossalari")],
            [KeyboardButton(text="Yaqinlashish prinsipi"),
             KeyboardButton(text="Bir o‘zgaruvchili funksiya va uning xossalari")],
            [KeyboardButton(text="Funksiyaning limitining ta’riflari"),
             KeyboardButton(text="Limitga ega bo‘lgan funksiyaning xossalari")],
            [KeyboardButton(text="Uzluksiz funksiya va uning xossalari"),
             KeyboardButton(text="Kesmada uzluksiz bo‘lgan funksiyalarning  xossalari")],
            [KeyboardButton(text="Bir o‘zgaruvchili funksiyaning hosilasi"),
             KeyboardButton(text="Hosilani hisoblash qoidalari")],
            [KeyboardButton(text="Funksiyaning differensiali"),
             KeyboardButton(text="Yuqori tartibli hosila va differensiallar")],
            [KeyboardButton(text="Differensial hisobning asosiy teoremalari"),
             KeyboardButton(text="Hosilaning tatbiqlari")],
            [KeyboardButton(text="Hosila yordamida funksiyani to‘la tekshirish"),
             KeyboardButton(text="Aniqmas integral va uni topishning sodda usullari")],
            [KeyboardButton(text="Ratsional funksiyalarni integrallash"),
             KeyboardButton(text="Sodda irratsional va transsendent funksiyalarni integrallash")],
            [KeyboardButton(text="Aniq integralning  ta’rifi.  Aniq integral mavjud bo‘lishining zaruriy va yetarli shartlari"),
             KeyboardButton(text="Integrallanuvchi funksiyalar sinfi.  Aniq integralning xossalari")],
            [KeyboardButton(text="Aniq integralni  hisoblash usullari"),
             KeyboardButton(text="Chegaralari cheksiz  xosmas integrallar")],
            [KeyboardButton(text="Chegaralanmagan funksiyaning xosmas integrali"),
             KeyboardButton(text="Aniq integralning geometrik kattaliklarni hisoblashga  tatbiqlari. Aniq integralning mexanika va fizikaga tatbiqlari")],
            [KeyboardButton(text="Yaqinlashuvchi sonli qatorlar va ularning xossalari"),
             KeyboardButton(text="Musbat hadli qatorlar")],
            [KeyboardButton(text="Ixtiyoriy hadli qatorlar"),
             KeyboardButton(text="Funksional ketma-ketliklar. Tekis yaqinlashuvchi funksional ketma-ketliklarning xossalari")],
            [KeyboardButton(text="Funksional qatorlar. Tekis yaqinlashuvchi funksional qatorlarning  xossalari"),
             KeyboardButton(text="Darajali qatorlar. Teylor qatori")],
            [KeyboardButton(text="Orqaga")]
    ],
    resize_keyboard=True
)

mavzu1=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ma'ruza"),
         KeyboardButton(text="Amaliyot")],
        [KeyboardButton(text="Video dars"),
         KeyboardButton(text="Mustaqil ta'lim misollari")],
        [KeyboardButton(text="Mustaqil ta'limni yuklash"),
         KeyboardButton(text="O'zlashtirish")],
        [KeyboardButton(text="Test savollari"),
         KeyboardButton(text="Mavzular ro'yhati")],
        [KeyboardButton(text="Fanlar"),
         KeyboardButton(text="Guruh ma'lumotlari")],
        [KeyboardButton(text="Guruhlar")]
    ],
    resize_keyboard=True
)


mavzu1_admin=ReplyKeyboardMarkup(
    keyboard=[
       [KeyboardButton(text="Mustaqil ta'limni tekshirish"),
         KeyboardButton(text="Test natijalari")],
        [ KeyboardButton(text="Mavzular ro'yhati"),
          KeyboardButton(text="Talabalarni baholash")],
        [ KeyboardButton(text="Mustaqil ta'lim"),
            KeyboardButton(text="Guruhlar")]
    ],
    resize_keyboard=True
)


mustaqil_talim=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ma'ruza matnini yuklash"),
         KeyboardButton(text="Amaliy mashg'ulotni yuklash")],
        [KeyboardButton(text="Mustaqil ta'lim savollarini yuklash"),
         KeyboardButton(text="Orqaga")]
    ],
    resize_keyboard=True

)


mavzu1_video=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Telegram"),
         KeyboardButton(text="You Tube")],
        [KeyboardButton(text="Orqaga")]
    ],
    resize_keyboard=True
)


admin1=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Test javoblarini ko'rish")]
    ]
)
