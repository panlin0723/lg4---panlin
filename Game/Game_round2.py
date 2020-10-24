# coding=utf-8

# 定义一个 flight 函数，来实现游戏逻辑
def flight():
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    # 使用 while 循环，让游戏可以进行多伦
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        # 判断谁的血量会最先小于等于 0
        if my_hp <= 0:
            print('我输了')
            break

        elif enemy_hp <= 0:
            print ('我赢了')
            break


flight()
