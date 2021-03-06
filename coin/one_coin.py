# import logging
import sys
from time import sleep
from daemon import Daemon
from Parsing import ParsingBlock

import settings

from_block = 217717
db_host = settings.dbhost
db_name = settings.BALANCE
coinid = settings.QTUM


def server_w(from_i):
    while True:
        try:
            data = ParsingBlock(db_host=db_host, db_name=db_name)
            best_block = data.get_block_count()
            if best_block >= from_i:
                print(from_i)
                pars = ParsingBlock(from_block=from_i, db_host=db_host, db_name=db_name)
                # logging.critical(from_i)
                decode_raw_transaction = pars.decode_raw_transaction()
                from_i += 1
            else:
                sleep(1)
        except Exception as e:
            print(e)
            # logging.warning("\n[+] -- Error while connecting to blockchain.\n")
            sleep(10)


server_w(from_block)

'''
class MyDaemon(Daemon):
    def run(self):
        # main program for demonizing
        server_w(from_block)


if __name__ == "__main__":
    # initiation command for work from daemon
    daemon = MyDaemon('/tmp/daem_coin.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)
'''
