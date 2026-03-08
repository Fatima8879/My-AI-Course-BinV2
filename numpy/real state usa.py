import numpy as np

broked_by,price,street,zip_code,house_size=np.genfromtxt("RealEstate-USA.csv",delimiter=",",usecols=(0,2,6,9,10),unpack=True,dtype=float,skip_header=1)

print(broked_by)
print(price)
print(street)
print(zip_code)
print(house_size)

print("RealEstate-USA price mean:",np.mean(price))
print("RealEstate-USA price average:",np.average(price))
print("RealEstate-USA price std:",np.std(price))
print("RealEstate-USA price mod:",np.median(price))
print("RealEstate-USA price percentile-25:",np.percentile(price,25))
print("RealEstate-USA price percentile-75:",np.percentile(price,75))
print("RealEstate-USA price percentile-3:",np.percentile(price,3))
print("RealEstate-USA price min:",np.min(price))
print("RealEstate-USA price max:",np.max(price))

print("RealEstate-USA price square:",np.square(price))
print("RealEstate-USA price sqrt:",np.sqrt(price))
print("RealEstate-USA price power:",np.power(price,price))
print("RealEstate-USA price abs:",np.abs(price))

addition= broked_by+broked_by
subtracted=street-house_size
multiplication=broked_by*price
division=broked_by/price

print("RealEstate-USA addition:",addition)
print("RealEstate-USA sub:", subtracted)
print("RealEstate-USA mul:",multiplication)
print("RealEstate-USA division:",division)

pricepie=(price/np.pi)+1

sine_value=np.sin(pricepie)
cosine_value=np.cos(pricepie)
tangent_values=np.tan(pricepie)

print("RealEstate-USA sin values:",sine_value)
print("RealEstate-USA cos value:",cosine_value)
print("RealEstate-USA tangent value:",tangent_values)

print("RealEstate-USA exponential value:",np.exp(pricepie))


log_array=np.log(pricepie)
log10_array=(np.log10(pricepie))
print("RealEstate-USA natural log:",log_array)
print("RealEstate-USA base 10 log",log10_array)



sinh_values=np.sinh(pricepie)
print("RealEstate-USA hyperbolic sin values",sinh_values)



cosh_values=np.cosh(pricepie)
print("RealEstate-USA hyperbolic cosine values:",cosh_values)


tanh_values=np.tanh(pricepie)
print("RealEstate-USA hyperbolic tangent value:",tanh_values)


asinh_values=np.arcsinh(pricepie)
print("RealEstate-USA inverse hyperbolic:", asinh_values)


acosh_value=np.arccosh(pricepie)
print("RealEstate-USA inverse hyperbolic cosine:",acosh_value)


D2broked_byprice=np.array([broked_by,
                           price])

print("RealEstate-USA broked plus price - 2 dimentional array",D2broked_byprice)

print("RealEstate-USA broked plus price - 2 dimentional array - dimention",D2broked_byprice.ndim)

print("RealEstate-USA broked plus price - 2 dimentional array - total number of elements",D2broked_byprice.size)

print("RealEstate-USA broked plus price -2 dimentional array - give size of array in each dimention",D2broked_byprice.shape)

print("RealEstate-USA broked plus price - 2 dimentional array -data type",D2broked_byprice.dtype)

D2broked_bypriceslice=D2broked_byprice[:1,:5]
print("RealEstate-USA broked plus price - 2 dimentional array - splicing array - D2brockedprice[:1,:5]")

D2broked_bypriceslice2= D2broked_byprice[:1,4:15:4]
print("RealEstate-USA broked plus price - 2 dimentional array - splicing array - D2broked-byprice[:1,4:15:4] ",D2broked_bypriceslice2)

D2broked_bypriceSliceitenonly= D2broked_bypriceslice[0,1]
print("RealEstate-USA broked plus price - 2 dimentional array - Index array - D2broked_bypriceslice[1,5]",D2broked_bypriceSliceitenonly)

D2broked_bypriceSliceitenonly= D2broked_bypriceslice2[0,2]
print("RealEstate-USA broked plus price - 2 dimentional array - index array - d2broked_bypriceslice2[0,2]")

for elem in np.nditer(D2broked_byprice):
    print(elem)

for index, elem in np.ndenumerate(D2broked_byprice):
   print(index,elem)




D2broked_byprice1to400=np.reshape(D2broked_byprice, (1,400))
print("RealEstate-USA broked plus price - 2 dimentional array - np.reshape(D2broked_byprice,(1,400)):",D2broked_byprice1to400)
print("RealEstate-USA broked plus price - 2 dimentional array - np.reshape(D2broked_byprice,(1,400)):size",D2broked_byprice1to400.size)
print("RealEstate-USA broked plus price - 2 dimentional array - np.reshape(D2broked_byprice,(1,,400)):ndim",D2broked_byprice1to400.ndim)
print("RealEstate-USA broked plus price - 2 dimentional array - np.reshape(D2broked_byprice,(1,400)):shape",D2broked_byprice1to400.shape)
print("RealEstate-USA broked plus price - 2 dimentional array - np.reshape(D2broked_byprice,(1,400)):ndim",D2broked_byprice1to400.ndim)


print()