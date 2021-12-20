#!/usr/bin/python3
import time, socket, subprocess, fileinput, os

inign = ''  #variable to store gain setting before start of test
iniadr = '' #variable to store adaptive gain setting before start of test
x = fileinput.input(files='/etc/default/dump1090-fa')
for line in x:
    if line.startswith('RECEIVER_GAIN='):
        inign = line
    if line.startswith('ADAPTIVE_DYNAMIC_RANGE='):
        iniadr = line
x.close()
print (" ")
print ("READING AND SAVING SETTINGS BEFORE STARTING THE TEST")
print ("THESE SETTINGS WILL BE RESTORRED AT THE END OF THE TEST")
print (" ")
print(inign + iniadr)


measure_duration = 62  #duration of one pass, seconds
ntests = 3   #number of tests
gains = "20.7 22.9 25.4 28.0 29.7 32.8 33.8 36.4 37.2 38.6 40.2 42.1 43.4 43.9 44.5 48.0 49.6".split()
#gains = "20.7 22.9 25.4 28.0 29.7 32.8 33.8 36.4".split()
#gains = "36.4 38.6 40.2 42.1 44.5 48.0 49.6".split()

gains.reverse()
results = {}

x = fileinput.input(files='/etc/default/dump1090-fa', inplace=1)
for line in x:
    if line.startswith('ADAPTIVE_DYNAMIC_RANGE='):
        line = 'ADAPTIVE_DYNAMIC_RANGE=no \n'
    print(line, end="")
x.close()



for i in range(ntests):
  print ("test", i+1, "of", ntests)
  for g in gains:
   if g not in results:
      results[g] = [0,0,{}] #msgs, positions, aircraft


   x = fileinput.input(files='/etc/default/dump1090-fa', inplace=1)
   for line in x:
       if line.startswith('RECEIVER_GAIN='):
           line = 'RECEIVER_GAIN='+g+'\n'
       print(line, end="")
   x.close()

   os.system("sudo systemctl restart dump1090-fa")
   time.sleep(2)
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect(('localhost',30003))
   t = time.time()
   c = ''
   d = ''
   while 1:
      c = (s.recv(32)).decode()
      d += c
      if time.time() - t > measure_duration:
         break
   s.close()

   #print(d)

   messages = 0
   positions = 0
   planes = {}
   for l in d.split('\n', -1):
      a = l.split(',')
      messages += 1
      if len(a) > 4:
         if a[1] == '3':
            positions += 1
         planes[a[4]] = 1
   print ("gain=",g, "messages=", messages, "positions=", positions, "planes=", len(planes.keys()))
   results[g][0] += messages
   results[g][1] += positions
   for hex in planes.keys():
      results[g][2][hex] = 1

print ("\n===Totals===")
print ("Gain, Messages, Positions, Aircraft")
for g in gains:
   (messages,positions,planes) = results[g]
   print (g, messages, positions, len(planes.keys()))


#RESTORE ORIGINAL GAIN SETTINGS
x = fileinput.input(files='/etc/default/dump1090-fa', inplace=1)
for line in x:
    if line.startswith('RECEIVER_GAIN='):
        line = inign
    print(line, end="")
x.close()

x = fileinput.input(files='/etc/default/dump1090-fa', inplace=1)
for line in x:
    if line.startswith('ADAPTIVE_DYNAMIC_RANGE='):
        line = iniadr
    print(line, end="")
x.close()

os.system("sudo systemctl restart dump1090-fa")

print ("SETTINGS RESTORED AT END OF TEST:")
x = fileinput.input(files='/etc/default/dump1090-fa')
for line in x:
    if line.startswith('RECEIVER_GAIN='):
        inign = line
    if line.startswith('ADAPTIVE_DYNAMIC_RANGE='):
        iniadr = line
x.close()
print(inign + iniadr)



