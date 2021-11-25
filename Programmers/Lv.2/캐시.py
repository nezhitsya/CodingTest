def solution(cacheSize, cities):
    if not cacheSize: return len(cities) * 5
    
    cache = []
    time = 0
    
    for i in cities:
        i = i.lower()
        
        if i in cache:
            time += 1
            cache.remove(i)
            cache.append(i)
            continue
        time += 5
        
        if len(cache) == cacheSize:
            cache.pop(0)
        cache.append(i)
    return time

# def solution(cacheSize, cities):
#     import collections
#     cache = collections.deque(maxlen=cacheSize)
#     time = 0
#     for i in cities:
#         s = i.lower()
#         if s in cache:
#             cache.remove(s)
#             cache.append(s)
#             time += 1
#         else:
#             cache.append(s)
#             time += 5
#     return time