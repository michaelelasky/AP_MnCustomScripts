# Author(s) Mike Elasky
# Date 7/30/2018
# Title ScientificRounding
# Used to round scientifically
# Code version 1.00
# Type (Python Custom Module)

def scientific_rounding(num, precision = 0):
    numstr = '0' + str(num)
    if numstr.count('.') == 0:
      return num
 
    splistprec = numstr.index('.') + 1 + precision
    if len(numstr) <= (splistprec + 2):
      numstr += '0' * (splistprec + 2 - len(numstr))
 
    roundnums = numstr[splistprec:splistprec+2]
    result = numstr[:splistprec]
 
    next_sig = result[-1] if result[-1] != '.' else result[-2]
    if int(roundnums) >= (51 - (int(next_sig) % 2)):
      if result[-1] == '.':
        result = str(int(result[:-1]) + 1)
      else:
        idx = result.index('.')
        tmp = result[idx+1:]
        dec = str(int(tmp) + 1)
        if len(tmp) > len(dec):
          dec = '0' * (len(tmp) - len(dec)) + dec
        if len(tmp) < len(dec):
          result = str(int(result[:idx]) + 1) + '.' + dec[1:]
        else:
          result = result[:idx] + '.' + dec
 
    return float(result)