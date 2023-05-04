def sort(a):
  print ('Initializing Soting Process')
  for i in range(1,len(a)):
     for j in range(i-1, -1, -1):
        if (j == 0 and a[j] > a[i]) or (a[j-1] <= a[i] and a[j] > a[i]):
          t = a[i]
          for k in range(i-1, j-1, -1):
            a[k + 1] = a[k]
          a[j] = t
          break
  print ('Sorted Array: ', a)

def main():
  a=[]
  n=int(input('Number of Integers in the array'))
  for i in range(n):
      j=int(input())
      a.append(j)
  sort(a)

if __name__ == '__main__':
  main()
