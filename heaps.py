import heapq


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

#creating a heap from a list
nums = [12,43,14,25,16]
heapq.heapify(nums)
print(nums)

#deleting the last element in a heap
print(heapq.heappop(nums))

#inserting an element
heapq.heappush(nums, 42)
print(nums)

#to get the smallest values
small_elements = heapq.nsmallest(2,nums)
print(small_elements)

#to get the largest values
large_elements = heapq.nlargest(2,nums)
print(large_elements)

