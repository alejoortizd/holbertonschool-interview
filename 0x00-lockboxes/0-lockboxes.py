#!/usr/bin/python3


def canUnlockAll(boxes):
    """function that determines if we can open all boxes"""
    open_boxes = [0]
    for key in open_boxes:
        for box in boxes[key]:
            if box not in open_boxes and box < len(boxes):
                open_boxes.append(box)
    if len(open_boxes) == len(boxes):
        return True
    return False
