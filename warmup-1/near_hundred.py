def near_hundred(n):
    """Return True if absolute answer is between 0 and 10"""
  if abs(100 - n) <= 10:
    return True
  elif abs(200-n) <= 10:
    return True
  else:
    return False

result = near_hundred(15)
print (result)
