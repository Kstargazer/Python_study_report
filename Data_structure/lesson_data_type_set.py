a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a)
print(type(a))
b = {2, 3, 3, 6, 7}
print(b)
print(a - b) #aからbを引いたものが出力される
print(b - a)
print(a & b) #a,bの共通部分
print(a | b) #aまたはb
print(a ^ b) #排他部分

s = {1, 2, 3, 4, 5}
#s[0] リストのようにインデックスがない
s.add(6)
print(s)
s.remove(6)
print(s)
s.clear()
print(s)
#help(set)

my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f) #型をリストからセットに変える
print(kind)