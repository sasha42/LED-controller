import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import time, sys, os, getopt, json, urllib

def initialise_led():
  global pwm
  from Adafruit_PWM_Servo_Driver import PWM

  # Set LED parameters
  pwm = PWM(0x40)
  pwm.setPWMFreq(1000)
  print("LEDs are initialised")

def parse_json(message):
    parameters = json.loads(message)
    for value in parameters:
        channel = int(value)
        brightness = 4095-int(parameters[value])
        pwm.setPWM(channel, brightness)
    return

class WSHandler(tornado.websocket.WebSocketHandler):
  waiters = set()
  cache = ['{"0":0,"1":0,"2":0}']
  cache_size = 200

  def check_origin(self, origin):
    parsed_origin = urllib.parse.urlparse(origin)
    return parsed_origin.netloc.endswith(".fixme.ch")

  def open(self):
    print ('user is connected.\n')
    WSHandler.waiters.add(self)
    self.write_message(str(self.cache[-1]))

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
    WSHandler.waiters.remove(self)
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
], debug=False, **settings)

if __name__ == "__main__":
  # See if there is hardware, initialise LEDs
  initialise_led()

  # Start the server
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(80)
  print("Server is listening")
  tornado.ioloop.IOLoop.instance().start()
