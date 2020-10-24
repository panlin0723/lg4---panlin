# coding=utf-8
import random


def flight(enemy_hp, enemy_power):
    my_hp = 1000
    my_power = 200

    # 打印敌人的血量和攻击力
    print(f'敌人的血量为:{enemy_hp}),敌人的力量为：{enemy_power}')

    # 使用 while 循环，让游戏多进行几轮
    while True:

        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        if  my_hp <= 0:
            print('我输了')
            break
        elif enemy_hp <= 0:
            print('我赢了')
            break

if __name__ == '__main__':
    # 利用列表推导式生成 hp
    hp = [x for x in range(990,1010)]
    enemy_hp = random.choice(hp)

    enemy_power = random.randint(190,210)

    flight(enemy_hp,enemy_power)

