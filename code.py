#coded by md sharique
#simple triangle validator
#---*---MY first code in python---*---#
#input :simply just enter all sides and angles of the triangle one by one# 
print("\t\t\tWECOME,MASTER|")
s1=int(input("\nEnter lebgth of first side :>"))
s2=int(input("\nEnter length of second side :>"))
s3=int(input("\nEnter side of third side :.>"))
a1=int(input("\nEnter degree of frst angle :>>"))
a2=int(input("\nEnter degree of second angle :>>"))
a3=int(input("\nEnter degree of third angle :>>"))

if (s1+s2>s3) and (s1+s3>s2) and (s2+s3>s1) and ((a1+a2+a3)==180)  :
   print("\n\t\t\tVALID Dimensions of TRIANGLE")
else :
   print("\n\t\t\tINVALID Dimensions of TRIANGLE")
