# python.exe -m pip install --upgrade pip
# pip install --upgrade pip
# pip install tinkoff-investments

# TODO: Надо получить список открытых позиций тикеры открытых инструментов и их количество открытых позиций
import mlb
import os
from tinkoff.invest import Client

# os.environ['INVEST_TOKEN'] = ''
# TOKEN = os.environ["INVEST_TOKEN"]

TOKEN = mlb.read_text_from_file(os.path.join('C:\\', 'keys', 'invest.txt'))  # Мой токен реального счета

def main():
    with Client(TOKEN) as client:
        response = client.users.get_accounts()
        accounts = [account.id for account in response.accounts]
        for response in client.operations_stream.positions_stream(accounts=accounts):
            print('response=', response)


if __name__ == "__main__":
    main()
