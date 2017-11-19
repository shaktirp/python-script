from datetime import datetime

file = open('test.txt','a') 
file.write('\n' + str(datetime.now())) 