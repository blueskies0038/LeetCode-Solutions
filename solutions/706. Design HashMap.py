class MyHashMap(object):
    
    def __init__(self):
        self.A = [-1] * 100000
​
    def put(self, key, value):
        self.A[key] = value
        
    def get(self, key):
        return self.A[key]
        
    def remove(self, key):
        self.A[key] = -1
        
​
​
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
