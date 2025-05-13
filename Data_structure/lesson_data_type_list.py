l = [1, 20, 4, 50, 2, 1, 2]
print(l)
print(l[0])
print(l[1])
print(l[-1])
print(l[0:2])
print(l[3:])
print(len(l))
print(type(l))
print(list('abcdefg'))

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
print(n[::2])
#2つ飛ばしで表示する
print(n[::-1])
#後ろから表示する
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
#ここのxはネストと言ってリストをリストの中に代入できる
print(x)
print(x[0])
print(x[1])
print(x[0][1])
#ネストの中の'b'を出力したい
print(x[1][2])
print('\n')

s = ['a','b','c','d','e','f','g']
print(s[0])
s[0] = 'X'
#文字列の時は直接データ変更できなかったが、データセットの時はできる
print(s[0])
print(s[2:5])
s[2:5] = ['C','D','E']
print(s)
s[2:5] = []
#指定範囲内のデータを消去
print(s)
s[:] = []
#s内のデータを全て消す
print(s, '\n')


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
n.append(100)
#データの最後に100を足す
print(n)
n.insert(0, 200)
#insert関数はコンマの左がインデックスを指定、右が追加するデータ
print(n)
print(n.pop())
#一番後ろのデータを取り出す
print(n)
print(n.pop(0))
print(n)
del n[0]
#deleteする
print(n)
del n
n = [1, 2, 3, 4, 4, 5]
n.remove(4)
#remove関数はインデックスではなく実際のデータ指定
print(n, '\n')

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x = a + b
print(x)
a += b
#aにbのデータを結合
print(a)
#以下の方法でもできる
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
#3が2番目のインデックスに入っているということを表示
print(r.index(3, 3))
#左が探している数値、右がどのインデックスから開始するかを指定している

print(r.count(3))
if 5 in r:
    print('exist')
if 100 in r:
    print('exist')
else:
    print('not found')

r.sort()
print(r)

r.sort(reverse=True)
print(r)
r.reverse() #reverse関数でも上と同じことができる
print(r)

s = 'My name is Mike.'
to_split = s.split (' ')
#split関数は''内で指定された文字でsplitする
print(to_split)

x = ' '.join(to_split)
#''内の文字を使って繋げてということ
print(x, '\n\n')

#print(help(list))でコマンドリスト見れる

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j=', j)
print('i=', i, '\n')

x = [1, 2, 3, 4, 5]
y = x.copy() #y = x[:]でも同様の作業ができる
y[0] = 11
print('y=', y)
print('x=', x)

#数字は値渡し、リストは参照渡し(参照後のデータを変更すると参照前のデータも変更されるのでバグに注意)

#値渡しの例
X = 20
Y = X
Y = 5
print(id(X))
print(id(Y)) #別の場所に保存されている　idタグで場所を表示できる
print(Y)
print(X)

#参照渡しの例
X = ['a', 'b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y)) #idが同じものを指している
print(X)
print(Y, '\n')

seat = []
min = 0
max = 5
print(min <= len(seat) < max)
seat.append('p')
print(min <= len(seat) < max)
print(len(seat))
seat.append('p')
print(min <= len(seat) < max)
print(len(seat))
seat.append('p')
seat.append('p')
seat.append('p')
print(min <= len(seat) < max)
print(len(seat))
seat.pop(0)
print(min <= len(seat) < max)
print(len(seat))
