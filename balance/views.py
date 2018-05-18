import tornado.ioloop
import tornado.web
from jsonrpcserver.aio import methods
import balance_methods
import logging
import os
import sys


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        method = self.get_query_argument('method')
        params = {k: self.get_argument(k) for k in self.request.arguments if k != 'method'}
        print(params)
        response = await methods.dispatch({"jsonrpc": "2.0", "method": method, 'params': params, "id": "null"})
        self.write(response)

    async def post(self):
        data = self.request.body.decode()
        print(data)
        response = await methods.dispatch(data)
        self.write(response)
