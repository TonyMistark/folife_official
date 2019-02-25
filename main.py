import tornado.ioloop
import tornado.web
from app.urls import urls
from app.settings import settings


print("settings: ", settings)


def make_app():
    return tornado.web.Application(urls, **settings)


if __name__ == "__main__":
    port = 8910
    address = "0.0.0.0"
    print("start server %s:%s" % (address, port))
    app = make_app()
    app.listen(port=port, address=address)
    tornado.ioloop.IOLoop.current().start()