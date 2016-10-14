from os.path import isfile
import sys

# Decorators
def valid_files(func):
   from functools import wraps

   @wraps(func)
   def decorator(*args, **kwargs):
      for filename in args:
         if isinstance(filename, str) and not isfile(filename):
            print("%s is not a valid file" % filename)
            sys.exit(1)
      return func(*args, **kwargs)

   return decorator