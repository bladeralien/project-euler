#Recursive Approach.
#def noroutes(a, b):
#    print('call noroutes ' + str(a) + ' ' + str(b))
#    if a == 0 or b == 0:
#        return 1
#    return noroutes(a - 1, b) + noroutes(a, b - 1)
#print(noroutes(20, 20))

#Dynamic Programming Rocks.
def noroutes(a, b, memory):
    print('call noroutes ' + str(a) + ' ' + str(b))
    if a == 0 or b == 0:
        return 1
    if (a, b) in memory:
        return memory[(a, b)]
    else:
        result = noroutes(a - 1, b, memory) + noroutes(a, b - 1, memory)
        memory[(a, b)] = result
        return result
print(noroutes(20, 20, {}))
