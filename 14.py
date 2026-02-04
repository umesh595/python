class RateLimitError(Exception):
    pass
class RateLimiter:
    def __init__(self,max_requests:int):
        self._max_requests=max_requests
        self._current_request={}
    def rate_limit(self,user_id:int):
        current_count=self._current_request.get(user_id,0)
        if current_count>=self._max_requests:
            raise RateLimitError("Cant exceed maximum requests")
        self._current_request[user_id]=current_count+1
        return True
limiter=RateLimiter(3)
try:
    print(limiter.rate_limit("user1"))
    print(limiter.rate_limit("user1"))
    print(limiter.rate_limit("user1"))
    print(limiter.rate_limit("user1"))
except RateLimitError:
    print("limit exceeded")