import colorama
import random
import time
import os


def main():
  prompt = []
  input("Press Enter when you're ready to begin...")
  lines = open(r'C:\Users\steph\Downloads\python\words.txt').read().splitlines()
  for i in range(3):
    for j in range(10):
      myline = random.choice(lines)
      print(colorama.Fore.GREEN + myline, end=" ")
      prompt.append(myline)
    print("")
  start_time = time.time()
  userinput = input(colorama.Style.RESET_ALL+"Start typing: ")
  end_time = time.time()
  userinput = userinput.split()  #splits into list
  correct_words = 0
  wrong_word_index = []
  if len(prompt) == len(userinput):
    for i in range(len(prompt)):
      if prompt[i] == userinput[i]:
        correct_words += 1
      else:
        wrong_word_index.append(userinput[i])
  else:
    try:
      for i in range(len(prompt)):
        if prompt[i] == userinput[i]:
          correct_words += 1
        else:
          wrong_word_index.append(i)
    except:
      pass

  elapsed_time = end_time - start_time
  #check # of correct words
  #print("words_correct/elapsedtime")
  wpm = (correct_words / (elapsed_time)) * 60
  print("WPM:", round(wpm, 2))
  #go through len and print all words, if input[i] is in wrong word index then make test red
  for i in range(len(userinput)):
    if i in wrong_word_index:
      print(colorama.Fore.RED + userinput[i], end=" ")
    else:
      print(colorama.Style.RESET_ALL + userinput[i], end=" ")
    if i%9 == 0 and i !=0:
        print("")
if (__name__ == "__main__"):
  main()
  print(colorama.Style.RESET_ALL + "")
