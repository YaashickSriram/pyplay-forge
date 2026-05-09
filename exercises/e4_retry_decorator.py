import time

def retry(times, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                 return func(*args, **kwargs)
                except Exception:
                    if attempt == times-1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

if __name__ == "__main__":
    attempts = {"count" : 0}

    @retry(times=3, delay=1)
    def flaky_function():
        attempts["count"]+=1
        print(f"Trying Attempt...{attempts['count']}")
        if attempts["count"]<3:
            raise ValueError("Not Yet!")
        return "Success!"
    
result = flaky_function()
print(f"Final Result : {result}")  
