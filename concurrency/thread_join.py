import threading


def worker1():
    for i in range(10000):
        print(f"worker1 {i}")


def main():
    t1 = threading.Thread(target=worker1)

    t1.start()
    #t1.join()

    print("Exiting main")

if __name__ == "__main__":
    main()

