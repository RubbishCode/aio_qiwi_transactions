# aio_qiwi_transactions
lib for working with qiwi for telegram async bots

# install:

#pip install git+https://github.com/RubbishCode/aio_qiwi_transactions.git#egg=aio_qiwi_transactions


# using:


Создаем класс AioQiwiTransactions

    qiwi = AioQiwiTransactions(
        phone='+79**********',
        token='***' # (https://qiwi.com/api)
        )


Выставляем счет на 10руб

    key_qiwi = await qiwi.creating_invoice(amount=10)

    link_for_paymant = key_qiwi['link_for_paymant'] # ссылка на платеж
    individual_key = key_qiwi['individual_key'] # индивидуальный код платежа


Проверяем платеж по индивидуальному ключу плательщика. Вернется False если нет платежа, сумма платежа - если платеж был совершен

    amount = await qiwi.check_payments(individual_key=individual_key)


           







