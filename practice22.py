###구명보트###
#필요한 구명보트의 갯수 최소값을 구하시오##

people = [70,50,80,50]
limit = 100  ## 구명보트에는 최대 두명까지만 탈 수 있음.

people = sorted(people,reverse=True)
answer = 0
print(people)

start = 0
end = len(people)-1
while start <= end:
    if people[start] + people[end] > limit:
        start +=1
    else:
        start +=1
        end -=1
    answer += 1

print(answer)

##del 때문에 오류가 난 듯 함.
while people:
    first = people[0]
    people.pop(0)

    for i in range(len(people)):
        if first + people[i] <= limit:
            del people[i]

    answer += 1

print(answer)

