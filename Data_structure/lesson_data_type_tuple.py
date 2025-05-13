t = (1, 2, 3, 4, 1, 2)
#tuple型はparenthesisで囲む
print(t)
print(type(t))
#t[0] = 100 ←エラーになる、データを変更できない
print(t[0])
print(t[-1])
print(t[2:5])
print(t.index(1))
print(t.index(1, 1))
print(t.count(1))
#help(tuple)
#値を代入したいが後からデータを書き換えられたくない時、読み込み専用で使う
t = ([1, 2, 3],[4, 5, 6])
#tuple型の中にリスト型のネストを入れることができる
print(t)

t[0][0] = 100
#tuple型の中であってもネストに入っているリスト型のデータは変更できる
print(t)

t = 1, 2, 3
#parenthesisで囲まなくてもtuple型になる
print(type(t))
print(t)

t = 1, #カンマがつくとtuple型になるのでint型、str型の時のエラー注意
print(type(t))

num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

min, max = 0, 100
print (min, max)

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)
#この数値の入れ替えをtupleのアンパッキングで簡単にやる
a = 100
b = 200
a, b = b, a
print(a, b)

choose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(choose_from_two)
print(answer)