from enum import Enum
from enum import IntEnum,unique
#创建一个枚举
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

@unique
class VIP1(IntEnum):
    YELLOW = 1
    GREEN = 2


print(VIP.GREEN)
print(VIP.GREEN.name)
print(VIP.GREEN.value)
