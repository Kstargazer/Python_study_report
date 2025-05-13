# コマンドライン引数
# import sys
# print(sys.argv)
# for i in sys.argv:
#     print(i)

# import lesson_package.utils
# from lesson_package import utils
# from lesson_package import utils as u #これもあまり推奨されていない
from lesson_package.utils import say_twice


# r = lesson_package.utils.say_twice('hello')
# r = utils.say_twice('hello')
# r = u.say_twice('hello')
r = say_twice('hello') #あまりこの書き方は好まれていない、上の2つはutilsがつくのでモジュール内とわかる
print(r)