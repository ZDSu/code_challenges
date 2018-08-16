# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem


def height(root):
    if root:
        return 1 + max(height(root.left), height(root.right))
    else:
        return -1


# doesn't quite work...
def height(root):
    height = -1
    queue = [root]
    while queue:
        current = queue.pop(0)
        if not queue:
            height += 1
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return height