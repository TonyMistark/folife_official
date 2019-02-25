from app.handlers.home import HomeHandler


urls = [
    (r"/", HomeHandler),
    (r"/home", HomeHandler),
]