# https://leetcode.com/problems/linked-list-cycle-ii/
# https://leetcode.com/articles/linked-list-cycle-ii/ [Premium]
# Solutions below <see PDF also>


# runtime: 44 ms, 100%; memory 18.4 MB, 16.15%
# runtime: 44 ms, 73%; memory 18.6 MB, 16.09%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = set()
        while head:
            if head in seen:
                return head
            else:
                seen.add(head)
            head = head.next


# runtime 36 ms, 97%; memory 18.7 MB, 11%
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next


"""
Solution (premium)
Approach 1: Hash Table

Intuition
If we keep track of the nodes that we've seen already in a `Set`, we can traverse the list and return the first duplicate node.

Algorithm
First, we allocate a `Set` to store `ListNode` references. Then, we traverse the list checking `visited` for containment of the current node. If the node has already been seen, then it is necessarily the entrance to the cycle. If any other node were the entrance to the cycle, then we would have already returned that node instead. Otherwise, the `if` condition will never be satisfied, and our function will return `null`.

The algorithm necessarily terminates for any list with a finite number of nodes, as the domain of input lists can be divided into two categories: cyclic and acyclic lists. An acyclic list resembles a `null`-terminated chain of nodes, while a cyclic list can be thought of as an acyclic list with the final `null` replaced by a reference to some previous node. If the `while` loop terminates, we return `null`, as we have traversed the entire list without encountering a duplicate reference. In this case, the list is acyclic. For a cyclic list, the `while` loop will never terminate, but at some point the `if` condition will be satisfied and cause the function to return.

<solution below>

Complexity Analysis
- Time complexity : O(n)
    For both cyclic and acyclic inputs, the algorithm must visit each node exactly once. This is transparently obvious for acyclic lists because the nnnth node points to `null`, causing the loop to terminate. For cyclic lists, the `if` condition will cause the function to return after visiting the nnnth node, as it points to some node that is already in `visited`. In both cases, the number of nodes visited is exactly nnn, so the runtime is linear in the number of nodes.
- Space complexity : O(n)
    For both cyclic and acyclic inputs, we will need to insert each node into the `Set` once. The only difference between the two cases is whether we discover that the "last" node points to `null` or a previously-visited node. Therefore,because the `Set` will contain nnn distinct nodes, the memory footprint is linear in the number of nodes.

"""

class Solution(object):
    def detectCycle(self, head):
        visited = set()

        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next

        return None


"""
Solution (premium)
Approach 2: Floyd's Tortoise and Hare

Intuition
What happens when a fast runner (a hare) races a slow runner (a tortoise) on a circular track? At some point, the fast runner will catch up to the slow runner from behind.

Algorithm
Floyd's algorithm is separated into two distinct phases. In the first phase, it determines whether a cycle is present in the list. If no cycle is present, it returns `null` immediately, as it is impossible to find the entrance to a nonexistant cycle. Otherwise, it uses the located "intersection node" to find the entrance to the cycle.

Phase 1
Here, we initialize two pointers - the fast `hare` and the slow `tortoise`. Then, until `hare` can no longer advance, we increment `tortoise` once and `hare` twice.(Footnote1) If, after advancing them, `hare` and `tortoise` point to the same node, we return it. Otherwise, we continue. If the `while` loop terminates without returning a node, then the list is acyclic, and we return `null` to indicate as much.  [Footnote1: It is sufficient to check only `hare` because it will always be ahead of `tortoise` in an acyclic list.]

To see why this works, consider the image below:
Phase 1
                          1
                       ^    \
                      /      >
-3 --> -2 --> -1 --> 0        2
                     ^        /
                      \      <
                       4 <-- 3

Here, the nodes in the cycle have been labelled from 0 to C−1, where C is the length of the cycle. The noncyclic nodes have been labelled from −F to -1, where F is the number of nodes outside of the cycle. After F iterations, `tortoise` points to node 0 and `hare` points to some node h, where F≡h(modC). This is because `hare` traverses 2F nodes over the course of F iterations, exactly F of which are in the cycle. After C−h more iterations, `tortoise` obviously points to node C−h, but (less obviously) `hare` also points to the same node. To see why, remember that `hare` traverses 2(C−h) from its starting position of h:

h+2(C−h)=2C−h
        ≡C−h(modC)​

Therefore, given that the list is cyclic, `hare` and `tortoise` will eventually both point to the same node, known henceforce as the intersection.

Phase 2
Given that phase 1 finds an intersection, phase 2 proceeds to find the node that is the entrance to the cycle. To do so, we initialize two more pointers: `ptr1`, which points to the head of the list, and `ptr2`, which points to the intersection. Then, we advance each of them by 1 until they meet; the node where they meet is the entrance to the cycle, so we return it.

Use the diagram below to help understand the proof of this approach's correctness.
<diagram>

We can harness the fact that `hare` moves twice as quickly as `tortoise` to assert that when `hare` and `tortoise` meet at node h, `hare` has traversed twice as many nodes. Using this fact, we deduce the following:

2⋅distance(tortoise)=distance(hare)
              2(F+a)=F+a+b+a
              2F+2a = F+2a+b
                  F = b

Because F=b, pointers starting at nodes h and 0 will traverse the same number of nodes before meeting.

To see the entire algorithm in action, check out the animation below:
<slide video>

Complexity Analysis
- Time complexity : O(n)
    For cyclic lists, `hare` and `tortoise` will point to the same node after F+C−h iterations, as demonstrated in the proof of correctness. F+C−h≤F+C=n, so phase 1 runs in O(n) time. Phase 2 runs for F<n iterations, so it also runs in O(n) time.
    For acyclic lists, `hare` will reach the end of the list in roughly n\2 iterations, causing the function to return before phase 2. Therefore, regardless of which category of list the algorithm receives, it runs in time linearly proportional to the number of nodes.
- Space complexity : O(1)
    Floyd's Tortoise and Hare algorithm allocates only pointers, so it runs with constant overall memory usage.
"""

class Solution(object):
    def getIntersect(self, head):
        tortoise = head
        hare = head

        # A fast pointer will either loop around a cycle and meet the slow
        # pointer or reach the `null` at the end of a non-cyclic list.
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return tortoise

        return None

    def detectCycle(self, head):
        if head is None:
            return None

        # If there is a cycle, the fast/slow pointers will intersect at some
        # node. Otherwise, there is no cycle, so we cannot find an entrance to
        # a cycle.
        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        # To find the entrance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1
