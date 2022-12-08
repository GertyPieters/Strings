# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_0 = 'Ruud Gullit '
scorer_1 = 'Marco Van Basten '

goal_0 = 32
goal_1 = 54

scorers = scorer_0 + f'{goal_0}', scorer_1 + f'{goal_1}'
scorers = scorer_0 + str(goal_0), scorer_1 + str(goal_1)
print(scorers) 

report = f'{scorer_0}scored in the {goal_0}nd minute \n{scorer_1}scored in the {goal_1}th minute'
print(report)

player = 'Ronald Koeman'
space = player.find(" ")
print(space)

first_name = player [0:space]
print(first_name)

last_name = player [space +1:]
print(last_name)
print(len(last_name))

name_short = player [0:1] + '. ' + last_name
print(name_short)

name = first_name + '! '
x = (len(first_name))
chant = name * x
print(chant[:-1])

good_chant = (chant[:-1] !=" ")
print(good_chant)
