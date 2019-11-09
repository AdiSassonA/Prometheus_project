from prometheus_client import start_http_server, Summary, Gauge, Counter
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
c = Counter('my_failures', 'Description of counter')
g = Gauge('my_inprogress_requests', 'Description of gauge')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    time.sleep(t)
    c.inc()
    g.set(random.randrange(1, 1000))

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())