import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  
  """
  print (conn.root.exposed_value())
  conn.root.exposed_append(5)       # Call an exposed operation,
  conn.root.exposed_append(6)       # and append two elements
  print (conn.root.exposed_value())   # Print the result
  """

  print(conn.root.exposed_sum(2,7))
  print(conn.root.exposed_sub(6,9))
  print(conn.root.exposed_mult(8,4))
