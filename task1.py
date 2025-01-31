import heapq

def min_connection_cost(cables):
    heapq.heapify(cables)  # Перетворюємо список у мін-купу
    total_cost = 0
    
    while len(cables) > 1:
        first = heapq.heappop(cables)  # Витягуємо найкоротший кабель
        second = heapq.heappop(cables)  # Витягуємо наступний найкоротший
        cost = first + second  # Витрати на їх об'єднання
        total_cost += cost  # Додаємо до загальних витрат
        heapq.heappush(cables, cost)  # Додаємо новий кабель назад у купу
    
    return total_cost

# Приклад використання
cables = [13, 2, 24, 15]
print(min_connection_cost(cables))  


# Цей алгоритм працює за жадібним принципом: завжди об'єднує два найменші кабелі, що мінімізує сумарні витрати. Використання heapq дозволяє ефективно отримувати та додавати елементи, підтримуючи купу.