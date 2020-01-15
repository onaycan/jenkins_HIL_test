import os
import datetime

calltime=datetime.datetime.now()
outfile=open("outputnow.out",'a')
outfile.write(str(calltime)+"\n")
