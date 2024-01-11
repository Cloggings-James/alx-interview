#!/usr/bin/python3

def canUnlockAll(boxes):
    opened = [0]
    for key in opened:
        for box_key in boxes[key]:
            if box_key not in opened and box_key < len(boxes):
                opened.append(box_key)
    return len(opened) == len(boxes)
