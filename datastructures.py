class Datastructures:
    def __init__(self):
        self.set_list = None
        self.queue_list = None
        self.dequeue_list = None
        self.heap_list = None




def main():
    ds = Datastructures()
  
    #SET
    ds.set_list = set()
    ds.set_list.add(5)
    ds.set_list.add(7)
    ds.set_list.remove(5)
    v = 6 in ds.set_list 
    print(v)






if __name__=="__main__":
    main()
    