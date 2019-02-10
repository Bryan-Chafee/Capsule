# setup of questions
length = 100
node = []
for i in range(length):
	node.append({})


node[0]['description'] = "You awake to the sounds of a low and dull thump. There it is again. The shadows that surround you are dispelled by a blinding red flash as the thump comes once more. But this time louder. You tear your head from the cryo-gel, to hear a shrill screech before a loud crack fills your chamber."
node[0]['question'] = "What do you do?"
node[0]['choices'] = ["Look around your compartment ","Try to see as much as you can through the glass around you","Do nothing"]
node[0][0] = node[1]
node[0][1] = node[2]
node[0][1] = node[3]


node[1]['description'] = "After taking a short look, you recall that you were put to sleep before a long journey. Resting on the interior is a red lever labelled ,?EMERGENCY?. Beside it is a monitor display."
node[1]['question'] = "What do you do?"
node[1]['choices'] = ["Pull the red lever","Interact with the Monitor","Do nothing"]
node[1][0] = node[2]
node[1][1] = node[11]
node[1][2] = node[5] #Do nothing

node[2]['description'] = "As the black mass above you leans away to strike the glass above you, you pull the red lever down. With a faint pop, the lid of your cryochamber shoots off, knocking the insectoid onto its back."
node[2]['question'] = "What do you do?"
node[2]['choices'] = ["Climb out of the chamber.","Hastily climb out of the chamber","Let out a hearty laugh."]
node[2][0] = node[7]
node[2][1] = node[8] #get out and cut yourself
node[2][2] = node[9] #Do nothing

node[3]['description'] = "Saliva drips over the glass surrounding you, and looking both ways you see isles of shattered containers and gored bodies strewn across the grated floors. All being illuminated by flashes of red. Hanging above you is a black carapace, with several black eyes staring straight at you. As it moves to crash its head down onto the cracked glass above you, you see large drooping wires still lit with sparks."
node[3]['question'] = "What do you do?"
node[3]['choices'] = ["Do nothing"]
node[3][0] = node[9] #Do nothing but give them option to electricute monster

node[4]['description'] = "A shattering crash fills your ears, followed by the scrambling, skittering and scraping of metal and bone. A rancid odor pools into your oxygen intake, and reaching towards your face is two rows of blackened teeth surrounded by four large pincers."
node[4]['question'] = "What do you do?"
node[4]['choices'] = ["Attack the creature", "Reach around for a glass shard, then attack the creature", "Look around","Do nothing"]
node[4][0] = node[6]
node[4][1] = node[5]
node[4][1] = node[5]
node[4][1] = node[5]

node[5]['description'] = "Grabbing your head with its long and grappling pincers, you are eviscerated as you are eaten alive"
node[5]['question'] = "Game Over"
node[5]['choices'] = ["Restart","End Game"]
node[5][0] = node[1]
node[5][1] = None

node[10]['description'] = "Grabbing your head with its long and grappling pincers, you are eviscerated as you are eaten alive"
node[10]['question'] = "Well, it's not up to you."
node[10]['choices'] = ["Restart","End Game"]
node[10][0] = node[1]
node[10][1] = None

##################################################################

node[6]['description'] = "Throwing your arms infront of yourself, you grab onto the pincers like handles, and do your best to hold them back. After a moments struggle, you feel your arms begin to bend out and away from your body, until a thundering snap. A sharp pain jets through your body, but no screams are heard as the monster wraps your face with his jaws."
node[6]['question'] = "Game Over"
node[6]['choices'] = ["Accept your fait", "Do not accept your fait"]
node[6][0] = node[5]
node[6][1] = node[10]

node[7]['description'] = "Manuevering over the broken glass, you firmly plant your feet. Now standing over the frantic insectoid."
node[7]['question'] = "What do you do?"
node[7]['choices'] = ["Attack the creature while it is vulnerable","Do Nothing"]
node[7][0] = node[11]
node[7][1] = node[13]

node[8]['description'] = "In your haste, you catch yourself on the edge of the chamber, landing face first in the shards of broken glass. You are not hurt, but you are bleeding. What do you do?"
node[8]['question'] = "What do you do?"
node[8]['choices'] = ["Get up and take a look at your surroundings","Do Nothing"]
node[8][0] = node[14]
node[8][1] = node[15]

node[9]['description'] = "Grabbing your head with its long and grappling pincers, you are eviscerated as you are eaten alive"
node[9]['question'] = "Game Over"
node[9]['choices'] = ["Restart","End Game"]
node[9][0] = node[1]
node[9][1] = None

def makeChoice(question, choice):
	alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", 
	"I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
	"S", "T", "U", "V", "W", "X", "Y", "Z"]
	valid = False

	print(question)

	for i in range(len(choice)):
		print("\t" + alphabet[i] + ": " + choice[i])

	while not valid:
		response = input(">>> ")
		if (response.upper() in alphabet) and (alphabet.index(response.upper()) <= len(choice)):
			valid = True
		else:
			print("Unable to processes this action. Try again.")

	return alphabet.index(response.upper())

def printDescription(text):
	counter = 0

	for i in range(len(text)):
		print(text[i], end="")
		counter += 1

		if (counter >= 50) and (text[i] == " "):
			counter = 0
			print("")

	print("\n")

def runGame(node):
	while node != None:
		printDescription(node['description'])
		next = makeChoice(node['question'], node['choices'])
		node = node[next]
	print("\nGame Over.")

runGame(node[0])