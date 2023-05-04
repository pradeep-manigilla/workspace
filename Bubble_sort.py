def sort(a):
  print ('Initializing the sorting process')
  for i in range(len(a) - 1, -1, -1):
    for j in range(i):
      if (a[j] > a [j+1]):
        t = a[j]
        a[j] = a[j+1]
        a[j+1] = t
  print ('Sorted Array is: ',a)
  
def main():
  a=[]
  n = int(input('Number of Integers in the Array:'))
  for i in range (0, n):
    j = int(input())
    a.append(j)
  sort(a)

if __name__ == "__main__":
  main()
