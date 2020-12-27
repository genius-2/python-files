x=int(input("кол-во игр "))
for i in range(x):
    k=int(input("№ черной мишени"))
    n=int(input("число секторов"))
    score=[]
    max=-1
    if (k == -1):
       for i in range(n):
           score.append(int(input()))
       for i in range(n):
           sum = 0
           for j in range(n):
               d=i+j
               if d > n-1:
                   d=d-n
               sum = sum + score[d]
               if sum > max:
                    max=sum
       print(max)
    else:
        for i in range(n):
            score.append(int(input()))
        score[k]=min(score)
        if score[k]>0:
            score[k]=0
        for i in range(n):
            sum = 0
            for j in range(n):
                d = i + j
                if d > n - 1:
                    d = d - n
                sum = sum + score[d]
                if sum > max:
                    max = sum
        print(max)