import etcd3
import asyncio


class flask_etcd:

    def __init__(self):
        self.etcd_client = etcd3.client(host='localhost', port=2379)
        # 创建一个事件来控制协程的暂停状态
        self.stop_event = asyncio.Event()
        # 观察者
        self.watcher = ""

    def callback(self, event):
        print("Event type:", event.event_type)
        print("Key:", event.key)
        print("Value:", event.value)

    def watch_stop(self):
        # 停止
        self.etcd_client.cancel_watch(self.watcher)

    def watch_callback(self, watch_key):
        self.watcher = self.etcd_client.add_watch_callback(watch_key, self.callback)


