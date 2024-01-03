import threading
import time

class ResourceManager:
    def __init__(self, resource_limit):
        self.resource_limit = resource_limit
        self.available_resources = threading.Semaphore(value=resource_limit)

    def use_resource(self, thread_id):
        with self.available_resources:
            print(f"Thread {thread_id} is using the resource.")
            time.sleep(2)  # Simulate resource usage
            print(f"Thread {thread_id} has released the resource.")

def worker_function(resource_manager, thread_id):
    resource_manager.use_resource(thread_id)

def main():
    resource_manager = ResourceManager(resource_limit=2)  # Allow 2 threads to use the resource concurrently

    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker_function, args=(resource_manager, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

