# aio_qiwi_transactions
lib for working with qiwi for telegram async bots

# install:

#pip install git+https://github.com/RubbishCode/aio_qiwi_transactions.git#egg=aio_qiwi_transactions


# using:


#создаем класс AioQiwiTransactions
>>> qiwi = AioQiwiTransactions(
    phone='+79**********',
    token='***'
    )


#выставляем счет на 10руб
>>> key_qiwi = await qiwi.creating_invoice(amount=10)

>>> link_for_paymant = key_qiwi['link_for_paymant'] # ссылка на платеж
>>> individual_key = key_qiwi['individual_key'] # индивидуальный код платежа


#вернется False если нет платежа, сумма платежа - если платеж был совершен
#проверяем платеж по индивидуальному ключу плательщика
>>> amount = await qiwi.check_payments(individual_key=individual_key)


           







