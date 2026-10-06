import random
import string

def id_generator():

  s_str = ""
  data = string.ascii_letters + '0123456789'


  for i in range(5):
    s_str += random.choice(data)

  return s_str