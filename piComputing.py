#!/usr/bin/python3.5
i = 2
pi = 3
while i != 1000000+2:
	pi+=4/(i*(i+1)*(i+2))-4/((i+2)*(i+3)*(i+4))
	i+=4
print(pi)
