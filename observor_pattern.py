class subscriber:
    def update(self, channel_name, video_title):
        print(f"{channel_name} uploaded: {video_title}")

class utubechannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, sub): 
        self.subscribers.append(sub)  

    def unsubscribe(self, sub):
        self.subscribers.remove(sub)

    def upload(self, title):
        print(f"\nNew video uploaded: {title}")
        for sub in self.subscribers:
            sub.update(self.name, title)

channel = utubechannel("interview with AJ")

sub1 = subscriber()
sub2 = subscriber()

channel.subscribe(sub1)
channel.subscribe(sub2)

channel.upload("Task for DK")