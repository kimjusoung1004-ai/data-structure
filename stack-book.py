#스택 초기화
#index   0     1    2    3    4
stack = [None,None,None,None,None]
top = -1 

# push 연산
top += 1 #top = 0
stack[top] = "커피"
top += 1 #top = 1
stack[top] = "녹차"
top += 1 #top = 2
stack[top] = "꿀물"

#스택 출력
#range(start, stop, stack)
print("==스택 상태==")
for i in range(len(stack)-1,-1,-1):
    print(stack[i])


#print_stack()

#pop()
#print_stack()