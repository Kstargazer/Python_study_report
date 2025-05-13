print('Hi','Mike', sep=',', end='.\n')

print(2+2)

import math
#数学ツールを呼び出せる
result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

s = 'test'
print(s)
print("I don't know")
#ダブルクウォーテーションマークの中のシングルはそのまま出力
print("say\"I don't know\"")
#バックスラッシュ＝コマンドとして認識されなくなる

print('hello. \nHow are you?')
print(r'C: \name\name')
#\nが入ると改行とみなされてしまう→rawの頭文字rを入れる

print("""
line1
line2
line3
""")
#複数行書くときはトリプルダブルクウォーテーションマーク

print('############')
print("""\
line1
line2
line3\
""")
print('############\n')
#バックスラッシュで次の行から始める

print('Hi.' * 3 + 'Mike.')
print('Py''thon')
prefix = 'Py'
print(prefix + 'thon')
#変数とリテラルはそのまま連結させられない

s = ('aaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbb')
print(s)
#parenthesisを使わない場合はバックスラッシュでも記述できる
s = 'aaaa'\
    'bbbb'
print(s)

word = 'python'
print(word[0])
#0からカウントする
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
#頭と末尾は指定しなくてもいい
print(word[:2])
print(word[2:])

word = 'j' + word[1:]
print(word)
#文字を変更して代入したいときは変更するところ以外はスライスで指定する
word = 'al' + word[2:4] +'ugh'
print(word)

n = len(word)
print(n)
#lenで文字数をカウントする

print('#########################\n')

s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
#is_startという代数に変数sのstartswith関数を代入している
#startswith, endswith関数は前にstr型を持ってくる
print(is_start)
is_start = s.startswith('x')
print(is_start)

print(s.find('Mike'))
#11番目に頭の文字が出てくる
print(s.rfind('Mike'))
#rfind関数は後から探す
print(s.count('Mike'))
#count関数で文中に何回出てきたかカウントできる
print(s.capitalize())
#文頭をキャピタライズ
print(s.title())
#単語の頭をcapitalize
print(s.upper())
#all capitalized
print(s.lower())
#all lowercase
print(s.replace('Mike', 'Nancy'))
#replace
print('\n')

a = 'a'
print(f'I am {a}')
#f-stringを使うことで短い記述で文字列を埋め込める
x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')
first_name = 'Kazuto'
family_name = 'Oda'
print(f'My name is {first_name} {family_name}. Watashi ha {family_name} {first_name}')

