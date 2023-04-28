import pandas as pd
from binance import AsyncClient
import asyncio
from asyncio.exceptions import TimeoutError
import logging


class DataGetter:
    """Get a different data form binance servers."""
    __WEIGHT = 0
    __WEIGHT_LIMIT = 1150  # Requests limit per a minute
    __FORMAT = '{levelname:<8} - Time:{asctime}. In the module {name} ' \
               'in line {lineno:03d} method "{funcName}()" ' \
               'in {created} seconds was wrote a message {msg}'
    __LOG_PATH = './logs/data_getter_warnings.log'
    __exchange_info = {}

    def __init__(self, client: AsyncClient):
        self.__client = client
        logging.basicConfig(filename=self.__LOG_PATH,
                            filemode='a',
                            encoding='utf-8',
                            format=self.__FORMAT,
                            style='{',
                            level=logging.WARNING)
        self.__logger = logging.getLogger(__name__)


    async def get_exchange_info(self):
        """
        Get an exchange info from a server
        :return: - json with the full exchange info
        """
        req_limit = 10
        req_counter = 0
        loop = asyncio.get_running_loop()
        while req_counter < req_limit:
            try:
                req = await self.__client.futures_exchange_info()
                loop.call_soon(asyncio.create_task, self.__set_weight())
                self.__exchange_info = req
                return
            except TimeoutError as e:
                self.__logger.error(f'Error during getting an exchange info. {e}')
                req_counter += 1
                continue

    async def get_all_futures(self, ) -> list:
        """
        This method finds symbol names from client.futures_exchange_info()
        @return: the list with the futures names
        """
        try:
            df = pd.DataFrame(self.__exchange_info['symbols'])
            df = df[df.symbol.str.contains('USDT')]
            lst = list(df['symbol'])
            return lst
        except pd.errors.DataError as e:
            self.__logger.error(f'Error during getting symbol names {e}')
            return []

    async def __set_weight(self) -> None:
        """
        Add a weight to the weight counter and get this weight out in a minute
        """
        weight = 5

        DataGetter.__WEIGHT += weight
        await asyncio.sleep(60)
        DataGetter.__WEIGHT -= weight

    async def __get_order_book(self, symbol: str):
        """
        Get order book by symbol between the level's boards
        :param symbol: futures pair name
        :return: json order book
        """
        limit = 100

        req_limit = 10
        req_counter = 0
        loop = asyncio.get_running_loop()

        while req_counter < req_limit:
            if DataGetter.__WEIGHT >= DataGetter.__WEIGHT_LIMIT:
                self.__logger.error(f'Requests weight is more than limit {DataGetter.__WEIGHT}')
                await asyncio.sleep(60)
                continue
            try:
                req = await self.__client.futures_order_book(symbol=symbol, limit=limit)
                loop.call_soon(asyncio.create_task, self.__set_weight())
                return req
            except TimeoutError as e:
                self.__logger.error(f'{symbol} The error during getting an order book data from the server.')
                await asyncio.sleep(1)
                req_counter += 1
                if req_counter == req_limit:
                    await asyncio.sleep(300)
                    req_counter = 0
                    continue
                continue

    async def get_large_applications(self, symbol: str,
                                     min_vol_order: float) -> dict:
        book_dict = {}
        while True:
            try:
                book = await self.__get_order_book(symbol)

                book_df_bids = pd.DataFrame(book['bids'])
                book_df_bids.columns = ['price', 'qty']
                book_df_bids = book_df_bids.astype(float)
                book_df_bids = book_df_bids.loc[book_df_bids.price * book_df_bids.qty > min_vol_order]
                book_df_bids = book_df_bids.set_index('price')
                book_dict['bids'] = book_df_bids.qty.to_dict()

                book_df_asks = pd.DataFrame(book['asks'])
                book_df_asks.columns = ['price', 'qty']
                book_df_asks = book_df_asks.astype(float)
                book_df_asks = book_df_asks.loc[book_df_asks.price * book_df_asks.qty > min_vol_order]
                book_df_asks = book_df_asks.set_index('price')
                book_dict['asks'] = book_df_asks.qty.to_dict()
                return book_dict
            except ValueError as e:
               # self.__logger.error(e)
                await asyncio.sleep(1)
                continue

