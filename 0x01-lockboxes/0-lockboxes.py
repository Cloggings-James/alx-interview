#!/usr/bin/python3

def canUnlockAll(boxes):
    total_boxes = len(boxes)
    unlocked_boxes = [False] * total_boxes
    unlocked_boxes[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < total_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)
