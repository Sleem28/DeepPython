import asyncio
import time
from datetime import datetime
import pandas as pd
from keys import api_key, api_secret
from binance import AsyncClient, BinanceSocketManager
from DataGetter import DataGetter
import logging


class FindBigOrders:
    __async__client: AsyncClient
    __data_getter: DataGetter
    __bm: BinanceSocketManager
    __TASKS = []
    __SYMBOLS = []
    __FORMAT = '{levelname:<8} - Time:{asctime}. In the module {name} ' \
               'in line {lineno:03d} method "{funcName}()" ' \
               'in {created} seconds was wrote a message {msg}'
    __ORDERS = './logs/big_orders.log'

    def __init__(self):
        logging.basicConfig(filename=self.__ORDERS,
                            filemode='a',
                            encoding='utf-8',
                            level=logging.WARNING)
        self.__logger = logging.getLogger(__name__)

    async def __task(self, symbol: str, req_period: int, min_limit_order: float):
        control_time = 0
        print(f'{symbol} initialized. OK.')

        async with self.__bm.futures_depth_socket(symbol=symbol, depth='20') as fd:
            while True:
                cur_time = time.time()
                req = await fd.recv()
                try:
                    df_bids = pd.DataFrame(req['data']['b'])
                    df_asks = pd.DataFrame(req['data']['a'])
                    df_bids.columns = ['price', 'qty']
                    df_asks.columns = ['price', 'qty']
                    df_bids = df_bids.astype(float)
                    df_asks = df_asks.astype(float)
                    df_bids = df_bids.loc[df_bids.price * df_bids.qty > min_limit_order]
                    df_asks = df_asks.loc[df_asks.price * df_asks.qty > min_limit_order]
                    df_bids = df_bids.set_index('price')
                    df_asks = df_asks.set_index('price')
                    bids = df_bids.qty.to_dict()
                    asks = df_asks.qty.to_dict()

                except ValueError as e:
                    self.__logger.error(f'ValueError during reading order book by {symbol}.\n {req = } {e}')
                    continue
                except KeyError as e:
                    self.__logger.error(f'KeyError during reading order book by {symbol}.\n {req = } {e}')
                    continue
                if len(bids) > 0:
                    print(f'WSS data:{symbol}, BIDS order more than {min_limit_order} USDT: {bids}' \
                                       f'Time: {datetime.now()}')
                if len(asks) > 0:
                    print(f'WSS data:{symbol}, ASKS order more than {min_limit_order} USDT: {bids}' \
                                       f'Time: {datetime.now()}')
# TODO Доделать логирование и сдать
                if cur_time >= control_time:
                    control_time = cur_time + req_period

                    result = await self.__data_getter.get_large_applications(symbol=symbol, min_vol_order=min_limit_order)
                    if len(result['bids']) > 0:
                        self.__logger.warning(f"HTTPS data: {symbol} BIDS: {result['bids']} Time: {datetime.now()}")
                        print(f"HTTPS data: {symbol} BIDS: {result['bids']}")
                    if len(result['asks']) > 0:
                        self.__logger.warning(f"HTTPS data: {symbol} ASKS: {result['asks']} Time: {datetime.now()}")
                        print(f"HTTPS data: {symbol} ASKS: {result['asks']}")

    async def run(self, req_period: int, min_limit_order: float):
        self.__async__client = await AsyncClient.create(api_key=api_key, api_secret=api_secret)
        self.__data_getter = DataGetter(self.__async__client)
        await self.__data_getter.get_exchange_info()
        self.__SYMBOLS = await self.__data_getter.get_all_futures()
        self.__bm = BinanceSocketManager(self.__async__client)

        for symbol in self.__SYMBOLS:
            task = asyncio.create_task(self.__task(symbol, req_period, min_limit_order))
            self.__TASKS.append(task)
        print('All tasks are completed')

        for task in self.__TASKS:
            await task

        await self.__async__client.close_connection()

