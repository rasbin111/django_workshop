import time

def calculate_time(view):
    def inner(request):
        start_time = time.time()
        view_value = view(request)
        end_time = time.time()
        time_consumed = end_time - start_time
        print("-"*40)
        print(f"Time elapsed: {time_consumed:.5f} seconds")
        print("-"*40)
        return view_value
    return inner
