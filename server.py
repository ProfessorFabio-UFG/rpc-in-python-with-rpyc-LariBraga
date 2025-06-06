import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

"""
class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value
"""

class Operations(rpyc.Service):
    resp = ""

    def exposed_sum(self, num1, num2):
      self.resp = str(num1) + " + " + str(num2) + " = " + str(num1+num2)
      return self.resp
    
    def exposed_sub(self, num1, num2):
      self.resp = str(num1) + " - " + str(num2) + " = " + str(num1-num2)
      return self.resp
    
    def exposed_mult(self, num1, num2):
      self.resp = str(num1) + " * " + str(num2) + " = " + str(num1*num2)
      return self.resp

if __name__ == "__main__":
  #server = ThreadedServer(DBList(), port = PORT)
  server = ThreadedServer(Operations(), port = PORT)
  server.start()
  