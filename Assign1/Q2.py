import random
def simulate_dice():



   roll_number = 0
   msg = "Press Enter to Roll (or) Type 'Exit' to Close.\n\n"
   while True:
       if input(msg).lower() == 'exit':
           break

       roll_number += 1
       dice_value = random.randint(1, 6)
       print(f"{roll_number} --->> You got a {dice_value}\n")

       msg = "Press Enter to Roll Again! \n"


if __name__ == '__main__':
   simulate_dice()
