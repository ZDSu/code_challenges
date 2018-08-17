// https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem


// Complete the insertNodeAtTail function below.
/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */
function insertNodeAtTail(head, data) {
    if (head == null) {
        head = new SinglyLinkedListNode(data)
    } else {
        let current = head
        while (current.next) {
            current = current.next
        }
        current.next = new SinglyLinkedListNode(data)
    }
    return head
}