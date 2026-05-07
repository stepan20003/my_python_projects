import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    person = ('charlie', 'dylan', 'alice', 'bob')
    action = ('move', 'grab', 'use', 'swim', 'run', 'climb', 'release')
    while True:
        x = random.choice(person)
        y = random.choice(action)
        yield (x, y)


def consume_event() -> None:
    print("=== Game Data Stream Processor ===")
    x = gen_event()
    for i in range(1000):
        event = next(x)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    lst1 = []
    for i in range(10):
        event = next(x)
        lst1 += [event]
    print(f"Built list of 10 events: {lst1}")
    for i in range(10):
        k = random.randint(0, len(lst1)-1)
        print(f"Got event from list: {lst1[k]}")
        lst1 = lst1[:k]+lst1[k+1:]
        print(f"Remains in list: {lst1}")


if __name__ == "__main__":
    consume_event()
