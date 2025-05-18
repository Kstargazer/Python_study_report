# from lesson_package.tools import utils
from ..tools import utils #..だと階層を一個上がるということ、あまり勧められてはいない

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')