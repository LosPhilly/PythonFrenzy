import time

def stopwatch():
    print("Stopwatch has started!")
    start_time = time.perf_counter()

    while True:
        elapsed_time = time.perf_counter() - start_time
        formatted_time = time.strftime("%M:%S", time.gmtime(elapsed_time))
        print("Elapsed Time:", formatted_time, end="\r")
        user_input = input("\n Press 's' to stop the stopwatch: ")
        if user_input == "s":
            print("\nElapsed Time:", elapsed_time)
            break
        
if __name__ == "__main__":
    stopwatch()
