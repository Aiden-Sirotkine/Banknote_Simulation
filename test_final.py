import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as stats


def run_simulation(r, n, k):
  # r = the number of types
  # n = the total number of cards of a type 
  # k = the number of cards than have already been picked 

  if k > n:
    return 0

  # all_cards_different = np.zeros((r, n), dtype=bool)

  all_cards = np.full(n, r, dtype=int)

#   If k is non-zero, I need to draw k cards specifically making sure 
#   I don't get a pair 
  done_k = False 
  for i in range(k):

    # drawing a random card without replacement NEVER GETTING A MATCH

    draw_success = False 
    card_drawn = -1
    index = -1
    while not draw_success:
      index = random.randint(0, n-1)

      card_drawn = all_cards[index]

      if card_drawn == r:
        draw_success = True

    # print(card_drawn)
    # print(index)
    all_cards[index] -= 1



    #now that k cards have been picked, we start the regular counting. 

  done = False 
  count = 0 
  while not done:
    count += 1

    # drawing a random card without replacement 

    draw_success = False 
    card_drawn = -1
    index = -1
    while not draw_success:
      index = random.randint(0, n-1)

      card_drawn = all_cards[index]

      if card_drawn != r:
        if (random.random() > (card_drawn / r)):
          continue 
        else: 
          draw_success = True 
      else: 
        draw_success = True 

    # print(card_drawn)
    # print(index)
    all_cards[index] -= 1

    # print

    if all_cards[index] <= (r - 2):
      done = True 

  return count



if __name__ == "__main__":

    print(run_simulation(2, 365, 1))

    sum = 0
    sum_k = 0
    for i in range(100):
        sum += run_simulation(2, 365, 0)
        sum_k += run_simulation(2, 365, 365)

    print(sum / 100)
    print(sum_k / 100)