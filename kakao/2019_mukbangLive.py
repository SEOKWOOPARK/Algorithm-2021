def solution(food_times, k):
    answer = 0
    food = []
    idx = 0
    
    for i in range(len(food_times)):
        food.append([i + 1, food_times[i]])
    
    for i in range(k):
        if len(food) == 0:
            return - 1
        food[idx][1] -= 1
        if (i != k - 1):
            if food[idx][1] == 0:
                food = food[:idx] + food[idx + 1:] 
            else:    
                if idx == len(food) - 1:
                    idx = 0
                else:
                    idx += 1
        else:
            if food[idx][1] == 0:
                food = food[:idx] + food[idx + 1:]            
            
    if len(food) == 1:
        return food[0][0]
    else:
        if idx == len(food) - 1:
            return food[0][0]
        else:
            return food[idx + 1][0]
        