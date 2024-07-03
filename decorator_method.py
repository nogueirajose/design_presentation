import time

# Step 1: Create the decorator
def execution_time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Function '{func.__name__}' executed in: {execution_time:.4f} seconds")
        return result
    return wrapper

# Step 2: Apply the decorator
@execution_time_logger
def sample_function(seconds):
    """A sample function that sleeps for a given number of seconds."""
    time.sleep(seconds)
    return f"Slept for {seconds} seconds"

# Test the decorated function
result = sample_function(2)
print(result)
