class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return 'Length: {} Data: {}'.format(self.length, self.data)

    def get(self, index):
        return self.data[index]

    def append(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length-1]
        del(self.data[self.length-1])
        self.length -= 1
        return last_item

    def delete(self, index):
        item = self.data[index]
        self.shift_items(index)
        return item

    def shift_items(self, index):
        for i in range(self.length):
            if index <= i < self.length-1:
                self.data[i] = self.data[i+1]
        del(self.data[self.length-1])
        self.length -= 1


new_arr = MyArray()
new_arr.append('hi')
new_arr.append('you')
new_arr.append('suh dude')
new_arr.append('woooow')
new_arr.pop()
new_arr.delete(1)
print(new_arr)
