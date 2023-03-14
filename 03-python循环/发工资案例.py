"""
总账户 10000元,
员工编号1~20,从1号开始发工资,每人1000元,
领工资时,财务判断员工绩效分(1~10)随机生成,小于5则不发,直接下一位
若总账户发完,则结束
"""

# 总资金
import random

total_funds = 10000
for n in range(1, 21):
    if total_funds == 0:
        print("总余额已经发完")
        break
    r = random.randint(1, 11)
    if r >= 5:
        total_funds -= 1000
        print(f"员工{n},绩效分{r},发放工资1000元,账户余额还有{total_funds}")
    else:
        print(f"员工{n},绩效分{r},小于5,不发工资,下一位")
