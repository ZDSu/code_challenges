// https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem


// Complete the insertNodeAtHead function below.
/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */
function insertNodeAtHead(head, data) {
    if (head == null) {
        head = new SinglyLinkedListNode(data)
    } else {
        const node = new SinglyLinkedListNode(data)
        node.next = head
        head = node
    }
    return head
}