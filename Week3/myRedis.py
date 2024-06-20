from redis import Redis

r = Redis(host='47.97.18.187', port=6379, db=0, decode_responses=True)

r.set('key', 'test')
print(f"1:{r.get('key')}")

value = r.get('key')
print(f"2: {value}")

r.set('key', 'newTest')
print(f"3: {r.get('key')}")

r.delete('key')
print(f"4: {r.get('key')}")