n = [10,20,40,80,100,500,1000]

def maxList(n):
    max = n[0]
    for i in range(len(n)):
        if n[i]> max:
            max = n[i]
    print('This is a maximum number ', max)
maxList(n)
