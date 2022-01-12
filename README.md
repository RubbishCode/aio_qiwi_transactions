# aio_qiwi_transactions
lib for working with qiwi for telegram async bots

# install:

#pip install git+https://github.com/RubbishCode/aio_qiwi_transactions.git#egg=aio_qiwi_transactions


# using:

from aiogram import Bot, Dispatcher, executor, types
from aio_qiwi_transactions import AioQiwiTransactions




#создаем класс AioQiwiTransactions
qiwi = AioQiwiTransactions(
    phone='+79**********',
    token='***'
    )


bot = Bot(token='*******:************')
dp = Dispatcher(bot)




@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message):


    key_qiwi = await qiwi.creating_invoice(amount=10) # выставляем счет на 10руб

    link_for_paymant = key_qiwi['link_for_paymant'] # ссылка на платеж
    individual_key = key_qiwi['individual_key'] # индивидуальный код платежа
    


    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text=f'💳 Оплатить: 10 RUB', url=link_for_paymant))
    keyboard.add(types.InlineKeyboardButton(text='✅ Подтвердить оплату', callback_data=f'checkUserPay{individual_key}'))

    await bot.send_message(chat_id=message.chat.id, text='Hello!\nPay it - 10 RUB', reply_markup=keyboard)




@dp.callback_query_handler(state='*')
async def callback(call: types.CallbackQuery):

    if 'checkUserPay' in call.data:
        individual_key = call.data.replace('checkUserPay', '')

        # вернется False если нет платежа, сумма платежа - если платеж был совершен
        amount = await qiwi.check_payments(individual_key=individual_key) # проверяем платеж по индивидуальному ключу плательщика


        if amount == 10:
            await bot.send_message(chat_id=call.from_user.id, text=f'thk for {amount} rub')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




