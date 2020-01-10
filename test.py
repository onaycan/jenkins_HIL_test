import os
import datetime

calltime=datetime.datetime.now()
outfile=open("output.out",'a')
outfile.write(str(calltime)+"\n")
