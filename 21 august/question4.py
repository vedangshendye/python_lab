import math
ball1=(0,0,5)
ball2=(12,13,4)

def ball_collide(a,b):
    dist=(a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])
    dist=math.sqrt(dist)

    if dist>a[2]+b[2]:
        return False
    else:
        return True
    
answer=ball_collide(ball1,ball2)
print("the value of answer is: ",answer)
