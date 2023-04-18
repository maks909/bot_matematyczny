import telebot 
import re 
from telebot import types

p = open("TOKEN.ini", "r", encoding="UTF-8")
TOKEN = p.read()
bot = telebot.TeleBot(TOKEN)
p.close()

digits_pattern = re.compile(r'^[0-9]+ [0-9]+$', re.MULTILINE)

@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    try:
        matches = re.match(digits_pattern, query.query)
    except AttributeError as ex:
        return

    if matches:
        num1, num2 = matches.group().split()
    else:
        pass
    try:
        m_sum = int(num1) + int(num2)
        r_sum = types.InlineQueryResultArticle(
            id=1, title="Suma",
            description=(f"Wynik: {m_sum}"),
            input_message_content=types.InputTextMessageContent(
                message_text=f"{num1} + {num2} = {m_sum}")
        )
        m_sub = int(num1) - int(num2)
        r_sub = types.InlineQueryResultArticle(
            id="2", title="Różnica",
            description=f"Wynik: {m_sub}",
            input_message_content=types.InputTextMessageContent(
                message_text=f"{num1} - {num2} = {m_sub}")
        )

        if num2 != "0":
            m_div = int(num1) / int(num2)
            r_div = types.InlineQueryResultArticle(
                id="3", title="iloraz",
                description=f"Wynik: {round(m_div, 2)}",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"{num1} / {num2} = {round(m_div, 2)}")
            )
        else:
            r_div = types.InlineQueryResultArticle(
                id="3", title="iloraz",
                description="Nie można dzielić przez zero!",
                input_message_content=types.InputTextMessageContent(
                    message_text="Jestem złą osobą i dzielę przez zero!")
            )
        m_mul = int(num1) * int(num2)
        r_mul = types.InlineQueryResultArticle(
            id=4, title="Iloczyn",
            description=f"Wynik: {m_mul}",
            input_message_content=types.InputTextMessageContent(
                message_text=f"{num1} * {num2} = {m_mul}")
        )
        bot.answer_inline_query(query.id, [r_sum, r_sub, r_div, r_mul])
    except Exception as e:
        print(f"{type(e)}\n{str(e)}")

bot.polling()