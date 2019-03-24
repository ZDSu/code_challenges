# https://leetcode.com/problems/n-ary-tree-level-order-traversal/


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# runtime 104 ms, 47%; memory 17.5 MB, 5%
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.children:
                    queue += curr.children
                level.append(curr.val)
            res.append(level)
        return res


# runtime 124 ms, 14%; memory 17.6 MB, 5.5%
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        traverse = []
        queue = [root]

        while queue:
            level = kids = []
            for _ in range(len(queue)):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.children:
                    kids.append(children)
            traverse.append(level)
            queue = kids
        return traverse


# runtime 108 ms, 28%; memory 17.7 MB, 5.5%
# ran again after solutions below and got:
# runtime 100 ms, 50%; memory 17.6 MB, 5.5%
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        traverse = []
        queue = [root]

        while queue:
            level = []
            kids = []
            for node in queue:
                level.append(node.val)
                if node.children:
                    kids += node.children
            traverse.append(level)
            queue = kids
        return traverse


# test cases:
# null
# {"$id":"1","children":[],"val":44}


# other solutions that are supposedly faster but are not:
# sample 88 ms submission; when I ran this code, I got:
# runtime 120 ms, 18.5%; memory 17.9 MB, 5.5%
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        base = [root]
        while base:
            nb = []
            cur = []
            for i in base:
                if i:
                    cur.append(i.val)
                    nb += i.children
            if cur:
                ans.append(cur)
            base = nb
        return ans

# sample 96 ms submission; when I ran this code, I got:
# runtime 100 ms, 50%; memory 17.4 MB, 5.5%
# then I got: runtime 100 ms, 50%; memory 17.7 MB, 5.5%
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        cur = [root]

        while cur:
            res.append([node.val for node in cur])
            tmp = []
            for node in cur:
                tmp += node.children
            cur = tmp

        return res

# from discussion
# runtime 104 ms, 36%; memory 17.6 MB, 5.5%
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q, ret = [root], []
        while any(q):
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret

# above without using any()
# runtime 100 ms, 50%; 17.6 MB, 5.5%
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q, ret = [root], []
        while q:
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret
