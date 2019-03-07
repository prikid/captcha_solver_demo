import os
from captcha_solver import solve_captcha

if __name__ == '__main__':

    directory = os.path.dirname(os.path.realpath(__file__)) + '\\captchas\\'

    total = solved_count = 0

    for filename in os.listdir(directory):
        if filename.endswith(".jpeg"):
            filepath = directory + filename
            total += 1
            real_value = os.path.splitext(os.path.basename(filepath))[0]

            solved_value = solve_captcha(filepath, show_image=True)

            is_solved = real_value == solved_value
            if is_solved:
                solved_count += 1

            print("Real value = {}, solved value = {} - {}".format(real_value, solved_value,
                                                                   'Success' if is_solved else 'Failure'))

    accuracy = solved_count / total * 100

    print('Total count: {total}. Solved: {solved}. Not solved: {notsolved}. Accuracy: {accuracy:03.2f}%'.format(
        accuracy=accuracy, total=total, solved=solved_count, notsolved=total - solved_count))
