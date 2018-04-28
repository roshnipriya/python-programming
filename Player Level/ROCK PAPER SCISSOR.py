input1,input2=raw_input().split()
if(input1=="R" and input2=="P"):
  print ("P")
elif(input1=="R" and input2=="S"):
  print ("R")
elif(input1=="P" and input2=="R"):
  print ("P")
elif(input1=="P" and input2=="S"):
  print ("S")
elif(input1=="S" and input2=="P"):
  print ("S")
elif(input1=="S" and input2=="R"):
  print ("R")
else:
  print "D"
