import random
secure_random = random.SystemRandom()

lineA = ("From time to time", "Consider me", "Blowing from the west")
lineB = ("The clouds give rest", "The one who loved poetry", "Fallen leaves gather")
lineC = ("To the moon-beholders.", "And persimmons.", "In the east.")
#I stole most of the lines from pre-existing haikus: From time to time by Matsuo Basho, Consider me by Masaoaka Shiki, Blowing from the west -Yosa Buson
print(random.choice(lineA))
print(random.choice(lineB))
print(random.choice(lineC))
