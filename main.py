import telebot 
import re 
from telebot import types

p = open("TOKEN.ini", "r", encoding="UTF-8")
TOKEN = p.read()
bot = telebot.TeleBot(TOKEN)
p.close()

digits_pattern = re.compile(r'^[0-9]+\.?[0-9]* [0-9]+\.?[0-9]*$', re.MULTILINE)

plus_icon = "https://telegra.ph/file/20d0840ae8fb72cbfab7f.png"
minus_icon = "https://telegra.ph/file/7d6cbd996df81528764a9.png"
multiply_icon = "https://telegra.ph/file/bc870950d5d7a12cd891a.png"
divide_icon = "https://telegra.ph/file/17b42fe493579e8cbb4cb.png"
exp_icon = "https://telegra.ph/file/457ff895f5c09c893bb76.png"
warring_icon = "https://telegra.ph/file/915e0e15a96084d7d4962.png"

@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    #try:
    matches = re.match(digits_pattern, query.query)
    #except AttributeError as ex:
    #    return

    if matches:
        num1, num2 = matches.group().split()
    #else:
    #    pass
    #try:
        m_sum = float(num1) + float(num2)
        r_sum = types.InlineQueryResultArticle(
            id=1, title="Suma",
            description=(f"Wynik: {round(m_sum, 2)}"),
            input_message_content=types.InputTextMessageContent(
                message_text=f"{num1} + {num2} = {round(m_sum, 2)}"),
            thumb_url=plus_icon, thumb_width=48, thumb_height=48    
        )
        m_sub = float(num1) - float(num2)
        r_sub = types.InlineQueryResultArticle(
            id=2, title="Różnica",
            description=f"Wynik: {round(m_sub, 2)}",
            input_message_content=types.InputTextMessageContent(
                message_text=f"{num1} - {num2} = {round(m_sub, 2)}"),
            thumb_url=minus_icon, thumb_width=48, thumb_height=48
        )

        if float(num2) != float(0):
            m_div = float(num1) / float(num2)
            r_div = types.InlineQueryResultArticle(
                id=3, title="iloraz",
                description=f"Wynik: {round(m_div, 2)}",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"{num1} / {num2} = {round(m_div, 2)}"),
                thumb_url=divide_icon, thumb_width=48, thumb_height=48
            )
        else:
            r_div = types.InlineQueryResultArticle(
                id=4, title="iloraz",
                description="Nie można dzielić przez zero!",
                input_message_content=types.InputTextMessageContent(
                    message_text="Jestem złą osobą i dzielę przez zero!"),
                thumb_url=warring_icon, thumb_width=48, thumb_height=48,
                url="https://pl.wikipedia.org/wiki/Dzielenie_przez_zero",
                hide_url=True
            )
        m_mul = float(num1) * float(num2)
        r_mul = types.InlineQueryResultArticle(
            id=5, title="Iloczyn",
            description=f"Wynik: {round(m_mul, 2)}",
            input_message_content=types.InputTextMessageContent(
                message_text=f"{num1} * {num2} = {round(m_mul, 2)}"),
            thumb_url=multiply_icon, thumb_width=48, thumb_height=48
        )
        m_exp = float(num1) ** float(num2)
        r_exp = types.InlineQueryResultArticle(
            id=6, title="Potęgowanie",
            description=f"Wynik: {round(m_exp, 2)}",
            input_message_content=types.InputTextMessageContent(
                message_text=f"{num1} ** {num2} = {round(m_exp, 2)}"),
            thumb_url=exp_icon, thumb_width=48, thumb_height=48
        )

        bot.answer_inline_query(query.id, [r_sum, r_sub, r_div, r_mul, r_exp])
    #except Exception as e:
    #    print(f"{type(e)}\n{str(e)}")

@bot.inline_handler(func=lambda query: len(query.query) == 0)
def empty_query(query):
    hint = "Musisz wpisać dwie liczby zmiennoprzecinkowe (np. 10.3 23.56), żeby otrzymać odpowiedź."
    try:
        r = types.InlineQueryResultArticle(
            id=1,
            title="Bot matematyczny",
            description=hint,
            input_message_content=types.InputTextMessageContent(
            message_text="Niestety nie wpisałem dwóch liczb :()",
            parse_mode="Markdown") 
        )
        bot.answer_inline_query(query.id, [r])
    except Exception() as e:
        print(e)

bot.polling()