import tornado.web


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        return self.write('hello,folife!')
