arr=np.array([10,23,43,32,54,32,43])
print(arr)



num=np.array(([12,32,43],
             [32,43,32] ))
print(num)



num=np.array([12,32,43,121,3254,4,3,2,6,2])
print(num[2])
print(len(num))
print(num[:9])



ar1=np.array(([12,23,43,2143,34],
              [12,43,21,43,212,])
              )
print(ar1[1,4])



num=np.array([21,32,34122,33,12,34,312,2,6])
print(num.reshape(3,3))



num1=np.array([12,32,21,32,12])
num2=np.array([21,32,4332,21,23])
print("ADDITION: ",num1+num2)
print("SUBTRACTION: ",num1-num2)
print("MULTIPLICATION: ",num1*num2)
print("DIVISION: ",num1/num2)



num=np.array([21,3,43,12,34,412,433,54])
print("max",np.max(num))
print("min",np.min(num))
print("mean",np.mean(num))
print("avg",np.average(num))

