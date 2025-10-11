
'''
#37
def is_prime(n):
  if n==1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

def is_truncatable(n):
  n=str(n)
  for x in range(len(n)):
    if is_prime(int(n))==False:
      return False
    else:
      n=n[:-1]
  return True

def is_rev_truncatable(n):
  n=str(n)
  for x in range(len(n)):
    if is_prime(int(n))==False:
      return False
    else:
      n=n[1:]
  return True

n=10

str_n=str(n)
rev_n=str_n[::-1]

trunc_list=[]


while len(trunc_list)<11:
  if is_truncatable(n)==True and is_rev_truncatable(n)==True:
    trunc_list.append(n)
  n+=1

print(sum(trunc_list))

#22

import csv

with open("C:\\Users\\amtha\\Music\\0022_names.txt", "r") as file:
    reader = csv.reader(file)
    name_list = next(reader)  # reads the first (and only) line as a list


def alphabetical_value(word):
    value=0
    for i in word:
        value += ord(i.upper())-ord("A")+1
    return int(value)

name_list=sorted(name_list)

total=0
for index in range(len(name_list)):
    total += alphabetical_value(name_list[index])*(index+1)


print(total)   


#9

data_set=[]

for a in range(1,1000):
    for b in range(1,1000):
        semi_set=[]
        if a**2 + b**2 == (1000-a-b)**2 and (1000-a-b)>0:
            semi_set.append(a)
            semi_set.append(b)
            semi_set.append(1000-a-b)
            data_set.append(semi_set)
    
product=data_set[0][0]*data_set[0][1]*data_set[0][2]

print(product)

            

#48
s=0
for i in range(1,1000):
    s=s+(i**i)


print(s)


#25
fibs=[1,1]
i=0
while True:
    a=fibs[i]+fibs[i+1]
    fibs.append(a)
    
    if len(str(a))==1000:
        break
    i+=1

print(i+3)



#14
p=0
n_max=0
for n in range(1,1000000):
    i=0
    m=n
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        i+=1
    if p<i:
        p=i
        n_max=m
    else:
        p=p
        n_max=n_max

print(p+1)
print(n_max)

#29
set=[]
for i in range(2,6):
    for j in range(2,6):
        a=i**j
        if a not in set:
            set.append(a)

print(len(set))

#21
def divisor_sum(n):
    divisor_list=[]
    for i in range(1,int(n/2)+1):
        if n%i==0:
            divisor_list.append(i)

    return(sum(divisor_list))

amicable_list=[]
        
for j in range(1,10000):
    if j==divisor_sum(divisor_sum(j)):
        amicable_list.append(j)



result=[]
for k in amicable_list:
    if divisor_sum(k)!=k:
        result.append(k)
       
print(sum(result))

#40
s="0."
for i in range(1,100000+200000):
    s+=str(i)

multi=1

for i in [1+1,10+1,100+1,1000+1,10000+1,100000+1,1000000+1]:
    multi=multi*int(s[i])


print(multi)

#3

import math

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    else:
        return True
    return

n=int(input(":- "))

factor_list=[]

while n%2==0:
    n=n/2
    factor_list.append(2)

 
for i in range(3,int(math.sqrt(n))+1,2):
    while is_prime(i)==True and n%i==0:
        factor_list.append(i)
        n=n/i

if n>2:
    factor_list.append(int(n))


print(max(factor_list))

#8
data_list = (
    "73167176531330624919225119674426574742355349194934"
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450"
)

str_number=""
for i in data_list:
    str_number+=i


max_product=0

for i in range(len(str_number.strip())-12):
    product=1 
    for j in range(i,i+13):
        product=product*int(str_number[j])
    if max_product<product:
        max_product=product

print(max_product)

'''

