# coding=utf-8
"""
一个回合制游戏，每个角色都有hp和power，hp代表血量，power代表攻击力，
hp的初始数值1000，power的初始数值200
定义一个fight方法：
my_final_hp = my_hp-敌人力量
evil_final_hp =敌人_hp-my_power
两个hp进行对比，血量剩余多的人获胜
"""
# 定义flight 函数，来实现游戏逻辑
def flight():

    # 定义四个变量分别存放初始数据
    my_hp = 1000
    enemy_hp = 1000
    my_power = 200
    enemy_power = 200

    # 定义最终血量的计算方式
    my_final_hp = my_hp - enemy_power
    evil_final_hp = enemy_hp - my_power

    # 判断输赢
    if my_final_hp > evil_final_hp:
        print('我赢了')
    elif my_final_hp < evil_final_hp:
        print('我输了')
    else:
        print('平局了')

    # 三木运算写法
    # print('我赢了') if my_final_hp < evil_final_hp else print ('我输了')
flight()

