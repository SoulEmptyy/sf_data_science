import numpy as np

number = np.random.randint(1, 101) # загадываем рандомное число
def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число
     Args:
         number (int, optional): Загаданное число. Defaults to 1.
     Returns:
         int: Число попыток
     """
    a1 = 1 
    a2 = 101 
 
    count = 0 # счетчик попыток
    # находим число за 7 и менее попыток
    while True:
        count+=1
        b = (a1+a2) // 2

        if b > number:
            a2 = b

        elif b < number:
            a1 = b
 
        else:
            print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            break 
    return count    