class ROSNode:
    def __init__(self):
        self.subscribers = {}
        self.publishers = {}

    def publish(self, topic, msg):
        if topic in self.subscribers:
            for callback in self.subscribers[topic]:
                callback(msg)

    def subscribe(self, topic, callback):
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(callback)

ros = ROSNode()

def camera_callback(data):
    print("Camera received:", data)

ros.subscribe("camera", camera_callback)
ros.publish("camera", "New frame captured")