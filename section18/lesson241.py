import enum


class Status(enum.Enum):
    PENDING = 1
    RENAME_PENDING = 1
    RUNNING = 2
    COMPLETED = 3


print(Status.PENDING)
print(Status.RENAME_PENDING)

print(repr(Status.PENDING))
print(Status.PENDING.name)
print(Status.PENDING.value)

for s in Status:
    print(s)
    print(type(s))

print(Status(1))


db = {
    "stack1": 1,
    "stack2": 2,
}

STATUS_ACTIVE = 1
STATUS_INACTIVE = 2

if db["stack1"] == STATUS_ACTIVE:
    print("stack1 is active")
elif db["stack1"] == STATUS_INACTIVE:
    print("stack1 is inactive")


@enum.unique
class DbStatus(enum.IntEnum):
    ACTIVE = 1
    INACTIVE = 2


print(DbStatus.ACTIVE)
print(type(DbStatus.ACTIVE))
print(DbStatus.ACTIVE == 1)

if db["stack2"] == DbStatus.ACTIVE:
    print("stack2 is active")
elif db["stack2"] == DbStatus.INACTIVE:
    print("stack2 is inactive")


class Perm(enum.IntFlag):
    R = 4
    W = 2
    X = 1


print(Perm.R | Perm.W)
print(type(Perm.R | Perm.W))
RW = Perm.R | Perm.W
print(Perm.R in RW)
print(Perm.X in RW)
