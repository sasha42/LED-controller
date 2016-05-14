import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from Adafruit_PWM_Servo_Driver import PWM
import time, sys, os, getopt, json

# Initialise LED
pwm = PWM(0x40)
pwm.setPWMFreq(1000)

def parse_json(message):
    parameters = json.loads(message)
    for value in parameters:
        channel = int(value)
        brightness = (4095-int(parameters[value]))
        pwm.setPWM(channel, brightness)
    return

class WSHandler(tornado.websocket.WebSocketHandler):
  waiters = set()
  cache = []
  cache_size = 200

  def open(self):
    print ('user is connected.\n')
    WSHandler.waiters.add(self)
  
  @classmethod
  def update_cache(self, message):
        self.cache.append(message)
        if len(self.cache) > self.cache_size:
            self.cache = self.cache[-self.cache_size:]

  def on_message(self, message):
    print ('%s' %message)
    parse_json(message)
    self.write_message(message + ' OK')
    WSHandler.update_cache(message)
    for waiter in self.waiters:
        try:
            waiter.write_message(message)
        except:
            logging.error("Error sending message", exc_info=True)

  def on_close(self):
    print ('connection closed\n')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("led.html", messages=WSHandler.cache)

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

application = tornado.web.Application([
    (r"/", IndexHandler),
    (r'/ws', WSHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler,
     dict(path=settings['static_path'])),
], debug=True, **settings)

if __name__ == "__main__":
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(8000)
  tornado.ioloop.IOLoop.instance().start()
