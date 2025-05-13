

"""
複数行のコメントはこうやって書くと
その中の行は全て無視される
"""

#変数の説明はコードの上に書くのがpythonの暗黙のルール
some_value = 100



"""
\を使うと改行して続けられる、80文字で改行のルール
()でもいい
"""


s = 'aaaaaaaaaaaaaa' \
    + 'bbbbbbbbbbbbb'
print(s)

x = -10
#if文ではインテンドをつける
#上から見ていって引っかかるところで出力される
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print("positive")

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0: #このifは家と同じインテンドを使う
        print('b is positive')

a = 1
b = 1
#aがbと等しい
print(a == b)
#aがbと異なる
print(a != b)
#aがbよりも小さい
print(a < b)
#aがbよりも大きい
print(a > b)
#aがb以下である
print(a <= b)
#aがb以上である
print(a >= b)
#aもbも真であれば真
print(a > 0 and b > 0)
#aかbが真であれば真
print(a > 0 or b > 0)
if a > 0 or b > 0:
    print('a or b is positive')

y = [1, 2, 3]
x = 1
if x in y:
    print('in')

if 100 not in y:
    print('not in')
a = 1
b = 2
#notを数字で使うのにはあまりお勧めされていない
if not a == b:
    print('Not equal')
#こちらを使う
if a != b:
    print('Not equal')

#boolen型の時にはnotを使う
is_ok = True
if not is_ok :
    print('hello')

is_ok = 1 #値が入っている = True
if is_ok:
    print('OK!')
else:
    print('No!')

is_ok = 0 # 0、値が入っていない = False
if is_ok:
    print('OK!')
else:
    print('No!')

is_empty = None #オブジェクトが存在していない
# print(help(is_empty))
if is_empty is None:
    print('None!!!')

print(1 == True)
#以下はオブジェクト同士が違う
#print(1 is True)




count = 0
#while count < 5:
  #  print(count)
  #  count += 1

while True:
    if count >= 5:
        break #終わらせる

    if count == 2:
        count += 1
        continue #下の文を無視して次のループに行く

    print(count)
    count += 1



count = 0
while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done')



while True:
    word = input('Enter:') #input関数でコンソールに入力できる
    num = int(word) #str型になるのでint型を入れたい時は変数宣言する
    if num == 100:
        break
    print('next')



some_list = [1, 2, 3, 4, 5]

#i = 0
#while i < len(some_list):
#    print(some_list[i])
#    i += 1

for i in some_list: #反復処理(イテレーター)で次々に情報を入力していく時はforを使う
    print(i)

for s in 'abcde':
    print(s)

for word in ['my', 'name', 'is', 'mike']:
    if word == 'name':
        continue
    print(word)



for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating!')
        break
    print(fruit)
else:
    print('I ate all')



#num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#for i in num_list:
 #   print(i)

#for i in range(2, 10, 3):
 #   print(i)

for _ in range(10): #iは_でもいい、レンジの数字を使わないということを示す
    print('hello')

for i, fruit in enumerate(['apple', 'banana', 'orange']): #enumerate関数でインデックスに数字を割り振り
    print(i, fruit)


days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee','tea','beer']

#for i in range(len(days)):
 #   print(days[i],fruits[i], drinks[i])

#zip関数を使うと初めのデータから順番に取ってきて、それぞれの変数に入れる
for day, fruit, drink in zip(days,fruits,drinks):
    print(day, fruit, drink)


d = {'x':100, 'y':200}
#print(d.items())
for k, v in d.items():
    print(k, ":", v)



def say_something(): #関数定義
    print('hi')
say_something()

print(type(say_something()))
f = say_something
f()


def say_something(): #関数定義
    s = 'hi'
    return s

result = say_something()
print(result)



def what_is_this(color):
    if color =='red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "i don't know"

print('what vegetable is it?')
result = what_is_this(input('color:'))
print(result)


#num: int = 0

