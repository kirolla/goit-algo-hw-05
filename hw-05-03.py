import timeit
# Алгоритм пошуку підрядка Boyer-Moore
def boyer_moore(pattern, text):
    m = len(pattern)
    n = len(text)
    
    # Побудова таблиці зсувів
    shift_table = {}
    for i in range(m - 1):
        shift_table[pattern[i]] = m - i - 1
        
    i = m - 1  # Індекс останнього символу зразка
    j = i  # Індекс останнього символу тексту
    
    while j < n:
        if text[j] == pattern[i]:
            if i == 0:
                return j
            else:
                i -= 1
                j -= 1
        else:
            if text[j] in shift_table:
                j += shift_table[text[j]]
            else:
                j += m
            i = m - 1
            
    return -1


# Алгоритм пошуку підрядка Knuth-Morris-Pratt
def knuth_morris_pratt(pattern, text):
    m = len(pattern)
    n = len(text)
    
    # Побудова префікс-функції
    prefix = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix[i] = j
    
    i = 0  # Індекс символу зразка
    j = 0  # Індекс символу тексту
    
    while j < n:
        if pattern[i] == text[j]:
            if i == m - 1:
                return j - i
            else:
                i += 1
                j += 1
        else:
            if i > 0:
                i = prefix[i - 1]
            else:
                j += 1
    
    return -1


# Алгоритм пошуку підрядка Rabin-Karp
def rabin_karp(pattern, text):
    m = len(pattern)
    n = len(text)
    
    for i in range(0, n - m + 1):
        if text_hash == pattern_hash:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            # Оновлення хеш-значення для наступного фрагмента тексту
            text_hash = text_hash - ord(text[i]) + ord(text[i+m])
    
    return -1

    # Вимірюємо час виконання для кожного алгоритму та підрядка в кожному текстовому файлі
for text_file in ["article_1.txt", "article_2.txt"]:
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Функція для вимірювання часу виконання певної функції пошуку підрядка
    def measure_time(func, text, pattern):
        return min(timeit.repeat(lambda: func(text, pattern), repeat=3, number=100))

    existing_pattern = "існуючий_підрядок"
    fictional_pattern = "вигаданий_підрядок"

    print(f"Результати для файлу {text_file}:")
    
    # Для кожного алгоритму вимірюємо час для існуючого та вигаданого підрядків
    for algorithm in [boyer_moore, knuth_morris_pratt, rabin_karp]:
        time_existing = measure_time(algorithm, text, existing_pattern)
        time_fictional = measure_time(algorithm, text, fictional_pattern)
        
        print(f"Алгоритм {algorithm.__name__}:")
        print(f"Час для існуючого підрядка: {time_existing}")
        print(f"Час для вигаданого підрядка: {time_fictional}")