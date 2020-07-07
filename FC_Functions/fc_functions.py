import queue,threading,concurrent.futures
import concurrent.futures
import time

q = queue.Queue()
# q = multip
t1 = time.perf_counter()
def consumer():
    while True:
        item = q.get(True)
        print(f'Working on item{item}')
        time.sleep(0.5)
        t2 = time.perf_counter()
        print(f'Finished item{item} in {t2-t1}seconds')
        q.task_done()

threading.Thread(target=consumer).start()

# def producer(label):
#     time.sleep(5)
#     q.put(label)

# for item in range(10):
#     threading.Thread(target=producer,args=(item,)).start()
# print('producer is finished...')
items = list[range(10)]
def producer(item,timeout):
    time.sleep(0.5)
    q.put(item)

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as excutor:
    future_item = {excutor.submit(producer,item,30): item for item in items}
    print(type(future_item))





q.join()
print('All work done')
