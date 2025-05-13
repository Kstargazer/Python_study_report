d = {'x':10, 'y':20}
print(d)
print(type(d))
print(d['x'])
print(d['y'])
d['x'] = 100
print(d['x'])
d['y'] = 'YYYY'
print(d)
d['z'] = 200
print(d)
d[1] = 10000
print(d)
#以下の方法でもdictを作れる
print(dict(a = 1000, b = 2000))
#リストにする
print(dict([('a', 10), ('b',  20)]),'\n')

d = {'x': 10, 'y': 20}
print(d)
#print(help(d))

print(d.keys()) #左に与えたものだけ表示
print(d.values()) #右の値だけ表示
d2 = {'x': 1000, 'j':500}
print(d)
print(d2)

d.update(d2) #d2でdをアップデート
print(d)
#以下のどちらかで情報を取って来れる
print(d['x'])
print(d.get('x')) #getを使うと数値が与えられていない時はエラーではなくnoneで返ってくる

d.pop('x') #popで取り出しもできる
print(d)
del d['y']
print(d)
d.clear()
print(d)

d = {'a':100, 'b': 200}
print('a' in d)
print('j' in d)

x = {'a':1}
y = x
y['a'] = 1000
print(x)
print(y)
#参照わたしになる

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300
}
print(fruits['apple'])
#リスト型でも作れるが、どの文字列にどのデータがあるかを取ってくるコードを書く必要がある
