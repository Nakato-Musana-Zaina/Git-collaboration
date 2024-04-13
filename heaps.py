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


helo = []
heapq.heappush(helo,23)
heapq.heappush(helo,26)
heapq.heappush(helo,10)
print(helo)

#creating a heap
nums = [12,43,14,25,16]
heapq.heapify(nums)
print(nums)

#deleting the last element in a heap
print(heapq.heappop(nums))

#inserting an element
heapq.heappush(nums, 42)
print(nums)

#to get the smallest values
smallest_value = heapq.nsmallest(nums)
print(smallest_value)

largest_value = heapq.nlargest(nums)
print(largest_value)
