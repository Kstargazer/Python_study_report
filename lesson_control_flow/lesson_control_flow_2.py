from operator import truediv


def add_num(a: int, b: int) ->int: #値の型を指定できる
    return a + b

r = add_num(10, 20)
print(r)

def menu(entree, drink, dessert): #=でデフォルトの引数を指定することも可能
    print(entree)
    print(drink)
    print(dessert)

menu(entree='beef', dessert='ice', drink='beer') #引数にキーワードを指定できる



def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)

y = [1, 2, 3]
r = test_func(200, y)
print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)

#前のデータに加わってしまう→バグに繋がる、pythonで参照渡しのものはは引数に入れるべきではないとされている
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l #このようにNoneをデフォルト引数にする


def say_something(word, *args): #*argsでタプルにすることができる
    print('word =', word)
    for arg in args:
        print(arg)

say_something('Hi!', 'Mike', 'Nancy')


t = ('Mike', 'Nancy')
say_something('Hi!', *t)


def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

#menu(entree='beef', drink='coffee')

d = {
    'entreee': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
menu(**d)


def example_func(param1, param2):
    """Example function with types documented in the docstring
    bla bla bla
    """
    print(param1)
    print(param2)
    return True

#これで関数の説明を出力できる
print(example_func.__doc__)


def outer(a, b):
    def plus(c, d):
        return c+d    #特定の関数内だけで使う場合
    r = plus(a, b)
    print(r)

outer(1, 2)


#クロージャー
def outer(a, b):
    def inner():
        return a+b
    return inner #実行する関数を返しているのではなくファンクションのみを返している

#後から関数内のものを計算させたいときに使う
f = outer(1, 2)
r = f()
print(r)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

cal1 = circle_area_func(3.14)
cal2 = circle_area_func(2.141592)

print(cal1(10))
print(cal2(10))

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info #デコレーター、1度記載すれば他の関数でも事前処理をまとめてできる
def add_num(a, b):
    return a + b

r = add_num(10,20)
print(r)

# f = print_info(add_num)
# r = f(10, 20)
# print(r)

# print('start')
# r = add_num(10,20)
# print('end')
#
# print(r)

l = ('Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun')

def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()
# sample_func = lambda word: word.capitalize()

#lambdaでその場限りの関数を作る
change_words(l, lambda word:word.capitalize())
change_words(l, lambda word:word.lower())


#generator
l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print('####################')
def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

# for g in greeting():
#     print(g)

g = greeting()
c = counter()
print(next(c))
print(next(g))
print(next(c))
print('@@@@')
print(next(g))
print('@@@@')
print(next(g))


# リスト内包表記
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)
r = []
for i in t:
    if i % 2 ==0:
        r.append(i)

print(r) #これを１行でやる


r = [i for i in t if i % 2 ==0]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print (r)

r = [i * j for i in t for j in t2]
print(r)


#辞書内包表記
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y, in zip(w, f):
    d[x] = y
print(d)

d = {x: y for x, y in zip(w, f)}
print(d)

# 集合内包表記
s = set()
for i in range(10):
    if i % 2 ==0:
        s.add(i)

print(s)

s = {i for i in range(10) if i % 2 ==0}
print(s)

# ジェネレーター内包表記
def g():
    for i in range(10):
        yield i

g = g()

g = (i for i in range(10) if i % 2 ==0) #tupleをつけないとgenerator型になる
# print(type(g))
# print(next(g))

for x in g:
    print(x)


# 名前空間とスコープ
animal = ('cat')
def f():
    # global animal #これによって関数を書き換えている
    # animal = 'dog' #ローカル変数
    # print('after', animal)
    animal = 'dog'
    print('local:', locals()) #ローカル関数にanimalが入っているということを辞書型で伝えてくれる


f()
# print('global:', animal)
# print('global:', globals())


# 例外処理
l = [1, 2, 3]
i = 5
#try except文、tryのなかでエラーが起きたらexceptを実行する
del l

try:
    l[i]
except IndexError as ex:
    print('dont worry: {}'.format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
else:
    print('done')
finally:
    print('clean up') #try-exceptで何が起こっても必ず実行される

print('last')

raise IndexError('test error')
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)
try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')

check()