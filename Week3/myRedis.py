from redis import Redis

def getRedis():
    return Redis(host='47.97.18.187', port=6379,db=0,decode_responses=True)

def redisKey(r):
    r.set('key', 'test')
    print(f"1:{r.get('key')}")

    value = r.get('key')
    print(f"2: {value}")

    r.set('key', 'newTest')
    print(f"3: {r.get('key')}")

    r.delete('key')
    print(f"4: {r.get('key')}")

def redisHash(r):
    key = 'student'
    r.hset(key,'name','zzz')
    r.hset(key,'age',23)

    print(r.hgetall(key))

    r.hset(key,'age',24)
    print(r.hgetall(key))
    
    r.delete(key)
    print(r.hgetall(key))

def redisList(r):
    key = 'message'
    r.lpush(key,'a','b','c')
    r.lpop(key)
    r.rpush(key,'d')
    r.rpop(key)

def redisSet(r):
    key = 'message'
    r.sadd(key,'a','b','c')



if __name__=='__main__':
    r = getRedis()
    # redisKey(r)
    # redisHash(r)
    redisList(r)
    redisSet(r)
    