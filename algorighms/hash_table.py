class HashTable:
    def __init__(self, size = 10):
        self.size = size
        self.table =[]
        self.count = 0
        for _ in range(0, self.size):
            self.table.append([])

    def _hash(self, key):
        total = 0
        for char in str(key):
            total += ord(char)
        return total % self.size


    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            k, v = bucket[i]
            if k == key:
                bucket[i] = (key, value)
                self.count += 1
                return
            
        bucket.append((key, value))
        self.count += 1
        
        if self.count/self.size > 0.7:
            self._rehash()


    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None
            
         
    def remove(self, key):
        """remove data by key"""
        index = self._hash(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
             k, v = bucket[i]
             if k == key:
                del bucket[i]
                return True
        return False
    def __str__(self):
        result = '{\n'
        for bucket in self.table:
            for k, v in bucket:
                result += f'{k}: {v}\n'
        result += "}"
        return result
    
    def _rehash(self):
        old_table = self.table
        self.size *= 2
        self.table = []
        for _ in range(self.size):
            self.table.append([])
        self.count = 0

        for buck in old_table:
             for k, v in buck:
                  self.insert(k, v)
                  

if __name__ == '__main__':
    ht = HashTable(size=5)

    ht.insert("apple", 32)
    ht.insert("phone", 43)
    ht.insert('phoneX', 55)
    ht.insert('phoneXS', 55)
    ht.insert('phoneXSMAX', 55)

    print(ht)
    print(ht.size)
    print(ht.get('apple'))
    print(ht.__str__())
