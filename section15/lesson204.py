from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register("get_queue", callable=lambda: queue)

manager = QueueManager(
    address=("127.0.0.1", 50000),
    authkey=b"abcde"
)
manager.connect()
queue = manager.get_queue()
queue.put("hello")
