def load_file():
    filepath=input("Enter the path of the file to load:")

    file=open(filepath,"r", encoding="utf-8")
    lines=file.readlines()
    file.close()
    return lines


def set_envieroment(raw_file):
    env=[]
    for line in raw_file:
        line=line.strip()
        env.append([int(c)for c in line])
    
    return env

my_file= load_file()
env=set_envieroment(my_file)
print(env)

def print_env(env):
    for row in env:
        for cell in row:
            if cell==1:
                print("■", end="")
            else:
                print(" ",end="")
        print()

print(print_env(env))

def check_neighbors(env,x,y):
    count=0
    L1=[x-1,x,x+1]
    L2=[y-1,y,y+1]
    for i in L1:
        for j in L2:
            if x==i and y==j:
                continue
        if env[i][j]==1:
            coutn +=1
    return count

print(check_neighbors(env,5,4))