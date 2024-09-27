def use_percent(team1_num, team2_num):

    print("\033[33mВ команде Мастера кода участников:"
          "\033[31m %s ! \033[0m" % team1_num)
    print("\033[33mИтого сегодня в командах участников:"
          "\033[31m %s\033[33m и\033[31m %s !\033[0m" % (team1_num, team2_num))
def use_format(score_2, team1_time):

    print("\033[33mКоманда Волшебники данных решила задач:"
          "\033[31m {0:13d} !\033[0m".format(score_2))
    print("\033[33mВолшебники данных решили задачи за:"
          "\033[31m {0:15.2f} с !\033[0m".format(team1_time))
def use_f_str(score_1, score_2, team1_time, team2_time):

    tasks_total = score_1 + score_2
    time_avg = (team1_time + team2_time) / tasks_total
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода !'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    challenge_result = result
    print(f'\033[33mКоманды решили \033[31m{score_1}'
          f'\033[0m\033[33m и\033[31m {score_2}\033[0m \033[33mзадачи.\033[0m')
    print(f'\033[33mРезультат битвы: \033[31m{challenge_result}\033[0m')
    print(f'\033[33mСегодня было решенно \033[31m{tasks_total}\033[33m задачи, \033[0m'
          f'\033[33mв среднем по \033[31m{time_avg:3.1f}\033[33m секунды на задачу!.\033[0m')
use_percent(5, 6)
use_format(42, 18015.2)
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
use_f_str(score_1, score_2, team1_time, team2_time)

