import requests_async as requests
import string
import random


async def key_generator(size=8, chars=string.ascii_uppercase + string.digits) -> str:
        """creating a random private key"""

        return ''.join(random.choice(chars) for _ in range(size))
    
    
    

class AioQiwiTransactions:
    """
    class for composing and processing asynchronous qiwi transactions
    phone: must start with country code
    token: get site (https://qiwi.com/api)
    """

    def __init__(self, phone: str, token: str):
        self.phone = phone
        self.token = token



    async def creating_invoice(self, amount: float) -> dict:
        """
        creating a payment link with an individual key for further
        identification of the payment by this key
        """

        individual_key = await key_generator()

        href = f'https://qiwi.com/payment/form/99?extra%5B%27account%27%5D={self.phone}&comment={individual_key}&amount={amount}'

        return {
            'link_for_paymant': href,
            'individual_key': individual_key,
        }
    


    async def check_payments(self, individual_key: str) -> float:
        """
        if a top-up by an individual key is found in the history of qiwi payments,
        the top-up amount will be returned, otherwise a lie will be returned
        """
        req = await requests.get('https://edge.qiwi.com/payment-history/v2/persons/' + self.phone + '/payments',
                          params={'rows': 50}, headers={'authorization': 'Bearer ' + self.token})
        
        data_json = req.json()
        pays_user_key = [data_json['data'][x]['comment'] for x in range(len(data_json['data']))]
        sum_pays_user = [float((data_json['data'][x]['sum']['amount'])) for x in range(len(data_json['data']))]

                
        sum_paymants = False
        if individual_key in pays_user_key:
            sum_paymants = sum_pays_user[pays_user_key.index(individual_key)]
        

        return sum_paymants
