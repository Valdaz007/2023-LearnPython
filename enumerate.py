myList = ['Victor', 'Absalom', 'Arnold', 'Zuriel', 'Ezekiel']

def main(alist):
  for index, item in enumerate(alist):
    print(f"{index} {item}")

if __name__ == "__main__":
  main(myList)
  
# Expected Output:
# 0 Victor
# 1 Absalom
# 2 Arnold
# 3 Zuriel
# 4 Exekiel
