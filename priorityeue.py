from typing import Any


class PriorityQueueItem:
    def __init__(self, priority, value, next_=None):
        self.priority = priority
        self.value = value
        self.next = next_

    def __repr__(self):
        return f"(priority={self.priority!r}, value={self.value!r})"


class PriorityQueue:
    _head: PriorityQueueItem | None = None

    def enqueue(self, priority: int, value: Any) -> None:
        if self._head is None:
            self._head = PriorityQueueItem(priority, value)
            return
        cur_item = self._head
        next_item = cur_item.next
        if next_item is None:
            if cur_item.priority < priority:
                self._head = PriorityQueueItem(priority, value, cur_item)
                return
        while cur_item:
            if next_item is None:
                cur_item.next = PriorityQueueItem(priority, value)
                return
            if next_item.priority < priority:
                cur_item.next = PriorityQueueItem(priority, value, next_item)
                return
            cur_item = next_item
            next_item = cur_item.next

    def dequeue(self) -> Any:
        if self._head is None:
            return None
        head_item = self._head
        self._head = self._head.next
        return head_item.value

    def __repr__(self):
        queue_list = []
        cur_item = self._head
        while cur_item:
            queue_list.append(cur_item.value)
            cur_item = cur_item.next
        return str(queue_list)


if __name__ == "__main__":
    queue = PriorityQueue()
    queue.enqueue(0, 'q')
    queue.enqueue(3, 'F')
    queue.enqueue(3, 'f')
    queue.enqueue(1, 'X')
    print(queue)  # must be [F, f, X, q]
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
