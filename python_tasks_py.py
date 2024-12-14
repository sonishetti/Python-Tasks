# -*- coding: utf-8 -*-
"""Python Tasks.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LsmnqqlM4Eo6_bHazQq_hDNYtJUO6Eh2

Task 13 : Binary Search Algorithm
"""

def binary_search(arr, target):
  left, right = 0 , len(arr) - 1

  while left <= right:
    mid = (left + right)

    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid- 1

  return -1

arr = [1,3,5,7,9]
target =7
index = binary_search(arr, target)

if index != -1:
  print(f"Found at index {index}")
else:
  print("Not Found")

"""Task 14 : Count word Frequency"""

def count_word_freq(para):
  word_count = {}
  words = para.split()

  for word in words:
    word_count[word] = word_count.get(word, 0) + 1

  return word_count

para = "apple banana apple orange banana banana"
word_freq = count_word_freq(para)

for word, count in word_freq.items():
  print(f"{word}: {count}")