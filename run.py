from markov_python.cc_markov import MarkovChain
mc = MarkovChain() 
mc.add_file('Romeo.txt')
lines = (mc.generate_text(20))
line = " ".join(lines)
newLine = line[0].upper()
for char in line[1:]:
	newLine = newLine + char
print (newLine)
