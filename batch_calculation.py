from time import sleep


def do_sum(number1, number2):
    answer = number1 + number2
    if answer % 5 == 0:
        sleep(0.1)
    return answer


if __name__ == '__main__':
    for i in range(100):
        calc_answer = do_sum(i, i)
        print(calc_answer)
