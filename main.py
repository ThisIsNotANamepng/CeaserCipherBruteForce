  decrypt = input("What are you trying to decrypt? ")
  decrypt = decrypt.lower()


  chars = "abcdefghijklmnopqrstuvwxyz"
  rot1 = str.maketrans(chars, chars[1:]+chars[0])
  file1 = open('words.txt', 'r')
  Lines = file1.readlines()

  finished = False
  for i in chars:
    if finished == True:
      pass
    else:
      correct = 0
      decrypt = decrypt.translate(rot1)
      list = (decrypt.split())
      count = 0
      length = len(list)
      # Strips the newline character
      for line in Lines:
        count += 1
        lineword = ((line.strip()))
        if lineword in list:
          index = (list.index(lineword))
          list[index] = lineword
          correct+=1
      if correct/length>0.5:
        finished = True
        guess = ""
        for m in list:
          guess = guess+m+" "
        print("Finished")
        print("Our best guess is:", guess)

