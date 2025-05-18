import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value
  
class Operations(rpyc.Service):

    def sum(num1, num2):
        return num1 + num2
    
    def sub(num1, num2):
       return num1 - num2
    
    def mult(num1, num2):
       return num1 * num2

if __name__ == "__main__":
  #server = ThreadedServer(DBList(), port = PORT)
  server = ThreadedServer(Operations(), port = PORT)
  server.start()

