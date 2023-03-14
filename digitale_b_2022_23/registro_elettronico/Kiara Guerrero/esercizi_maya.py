from datetime import *

fine_mondo = date(2012, 12, 21)
oggi = date.today()

cont = 0 

while fine_mondo <= oggi:
     giornisett = fine_mondo.weekday()
     if giornisett == 5 or giornisett == 6:
          cont = cont + 1
     fine_mondo = fine_mondo + timedelta(days=1)

print(cont)

    



