import time

start = time.perf_counter()

print("Hello world")
print("Hello tanaya")

finish = time.perf_counter()

time_taken = (finish - start) * 1000

print("Total time taken to execute the program is:", time_taken, "milliseconds")