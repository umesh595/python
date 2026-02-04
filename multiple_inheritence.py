class LoggerMixin:
    def log(self, msg):
        print(f"[LOG] {msg}")
class MetricsMixin:
    def record(self):
        print("Metric recorded")
class Service(LoggerMixin, MetricsMixin):
    def run(self):
        self.log("Service started")
        self.record()