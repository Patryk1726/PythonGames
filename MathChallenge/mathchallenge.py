import random
import time

total_operations = 10

def generator():
    operators = random.choice(['+', '-', '*', '/'])
    l_r = random.randint(3, 13)
    exercise = str(l_r) + ' ' + operators + ' ' + str(l_r)
    result = eval(exercise)
    return exercise, result

input('Press enter to start!')
print('----------------------')
start_time = time.time()

fail = 0
for i in range(total_operations):
    exercise, result = generator()
    while True:
        guess = input('Solution #' + str(i + 1) + ': ' + exercise + ' = ')
        if int(guess) == result:
            print('Correct!')
            break
        else:
            print('Try again.')
            fail += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
print(f'\n----------------------------')
print('Total time: ' + str(total_time))
print('Total failures: ' + str(fail))