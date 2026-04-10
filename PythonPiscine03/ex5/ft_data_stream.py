

import random


def gen_event():
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run", "eat", "sleep", "move", "grab", "climb",
        "swim", "release", "use"]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events):
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events.pop(index)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    # Create a Generator
    generator = gen_event()
    # Printing 1000 events
    for i in range(1000):
        event = next(generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    # Build list of 10 events
    events_list = []
    for _ in range(10):
        events_list.append(next(generator))
    print(f"Built list of 10 events: {events_list}")
    # Consume the events created
    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")
