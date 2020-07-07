import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5,4,3,4,13]
        future_todo = [executor.submit(do_something,sec) for sec in secs]
        #xyz = concurrent.futures.as_completed(future_todo)
        for future in concurrent.futures.as_completed(future_todo):
            sec = future_todo[future]
            try:
                sth = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (sec,exc))
            else:
                print('%r finished normaly...' % (future))

        
        #results = executor.map(do_something, secs)
        #print(f"type of executor.submit_to  is {type(xyz)}")
        
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
