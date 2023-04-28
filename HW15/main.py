from FindBigOrders import FindBigOrders
import asyncio
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find all big order by futures contracts from the cripto stock Binance.')
    parser.add_argument('-s', metavar='s', type=int, help='Enter the quantity of seconds to set the requests frequency', default=60)
    parser.add_argument('-l', metavar='l', type=int, help='Enter the limit for finding big orders', default=1_000_000)
    args = parser.parse_args()
    fbo = FindBigOrders()
    asyncio.run(fbo.run(args.s, args.l))


# To run insert to the command line:      python ./HW15/main.py -s 50 -l 500000

