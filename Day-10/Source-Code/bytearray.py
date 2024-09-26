site = "ManishShiwakoti.com"
arr1 = bytearray(site,'utf-8')
arr2 = bytearray(site,'utf-16')
m_view = memoryview(arr1)
print(list(m_view[0:]))
print(arr1)
print(arr2)

size = 4
arr = bytearray(4)
print(arr)