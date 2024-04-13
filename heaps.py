import heapq
# //max heap
heap = []
heapq.heappush(heap,-3)
heapq.heappush(heap,-8)
heapq.heappush(heap,-1)
print([-x for x in heap])

#min heap
books = []
heapq.heappush(books,9)
heapq.heappush(books,8)
heapq.heappush(books,5)
print(books)

# //nums = [-15,132,188, 0,100, 45,19]

helo = []
heapq.heappush(helo,23)
heapq.heappush(helo,26)
heapq.heappush(helo,10)
print(helo)

#creating a heap
nums = [12,43,14,25,16]

print(heapq.heapify(nums))

#deleting the last element in a heap
print(heapq.heappop(nums))

#inserting an element
heapq.heappush(nums, 42)

print(nums)