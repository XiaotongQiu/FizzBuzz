# Fizz Buzz Demo
## 开发语言
Python

## 题目说明
有一名体育老师，在某次离下课还有五分钟时，决定玩一个报数游戏。此时有100名学生在上课，游戏的规则如下：
1. 老师先说出两个不同的特殊数(都是个位数)，比如3, 5；让所有学生拍成一队，然后按顺序报数；
2. 学生报数时，如果所报数字是「第一个特殊数(3)」的倍数，或者包含「第一个特殊数(3)」，那么不能说该数字，而要说Fizz；
3. 学生报数时，如果所报数字是「第二个特殊数(5)」的倍数，或者包含「第二个特殊数(5)」，那么不能说该数字，而要说Buzz；
4. 如果所报数字同时是「两个特殊数」的倍数，也要特殊处理。例如，如果是「第一个(3)」和「第二个(5)」特殊数的倍数，那么也不能说该数字，而是要说FizzBuzz
5. 学生报数时，如果所报数字包含了「特殊数」，那么也不能说该数字，而是要说对应的英文单词（见规则1和规则2）。例如，要报13的同学应该说Fizz；要报52的同学应该说Buzz。
6. 如果在一次报数中，匹配上述多个规则，Fizz和Buzz都只能出现一次。
7. 否则，直接说出要报的数字。

## 程序说明
### 主程序：fizzbuzz.py
该主程序可以按照题目要求，打印出 从1~100所报的内容。每行打印一个报数内容。

运行指令如下：
```
python fizzbuzz.py
```

### 单元测试：test_fzbz.py
运行单元测试会先对报数结果进行打印，并根据测试样例进行自动测试。该单元测试总共含有6个测试样例，分别对题目中所提到的各类情况结果进行验证，具体如下：
1. 3的倍数
特殊数：3，5；报数：9；输出：Fizz
2. 包含3的数
特殊数：3，5；报数：13；输出：Fizz
3. 5的倍数
特殊数：3，5；报数：70；输出：Buzz
4. 包含5的数
特殊数：3，5；报数：52；输出：Buzz
5. 3和5的公倍数
特殊数：3，5；报数：90；输出：FizzBuzz
6. 含有3和5的数
特殊数：3，5；报数：53；输出：FizzBuzz

运行指令如下：
```
python test_fzbz.py
```
