
def get_all():
	global dictionary
	print(dictionary)

def set_parallel(a,b):
	global dictionary
	dictionary['parallel'].add((a,b))

	if ((a=='sb7' and b=='sc6') or (a=='sc6' and b=='sb7')):
		sc6()
		sb7()

def set_perpendicular(a,b):
	global dictionary
	dictionary['perpendicular'].add((a,b))

def set_equal(a,b):
	global dictionary
	dictionary['equal'].add((a,b))

def set_fraction(a,b,frac):
	global dictionary
	dictionary['fraction'].add((a,b,frac))

def set_sum_value(a,b,sum):
	global dictionary
	dictionary['sum_value'].add((a,b,sum))

def set_similar(a,b):
	global dictionary
	dictionary['similar'].add((a,b))

def set_congruent(a,b):
	global dictionary
	dictionary['congruent'].add((a,b))

def set_tan(a,b):
	global dictionary
	dictionary['tan'].add((a,b))

def sc6():
	global dictionary

	values = dictionary.get('parallel')
	for i in values:
		if i==('sb7','sc6') or i==('sc6', 'sb7'):	
			set_equal('b2','a1')
			set_equal('a3','c4')
			set_similar('ar2','ar1')
			set_similar('ar3','ar4')

			#always true in setup 1
			set_equal('c1','a5')
			set_equal('c2','b1')
			set_equal('c3','b4')
			set_equal('b5','a4')
			set_sum_value('c2','d2',180)
			set_sum_value('b1','d2',180)
			set_sum_value('c1','d4',180)
			set_sum_value('a5','d4',180)
			set_sum_value('d3','c3',180)
			set_sum_value('d3','b4',180)
			set_sum_value('d5','a4',180)
			set_sum_value('b5','d5',180)

	values = dictionary.get('perpendicular')
	for i in values:
		#if i==['sc6','sc7'] or i==['sc7','sc6']:
			#NIL

			# b2angle = 90
			# set_sum_value(dictionary,'a3','d1',90)
			# set_sum_value(dictionary,'a2','c2',90)
		if i==('sc6','sa7') or i==('sa7','sc6'):
			set_sum_value('b3','c3',90)
			set_sum_value('b2','d1',90)


			#always true in setup 1
			set_equal('c1','a5')
			set_equal('c2','b1')
			set_equal('c3','b4')
			set_equal('b5','a4')
			set_sum_value('c2','d2',180)
			set_sum_value('b1','d2',180)
			set_sum_value('c1','d4',180)
			set_sum_value('a5','d4',180)
			set_sum_value('d3','c3',180)
			set_sum_value('d3','b4',180)
			set_sum_value('d5','a4',180)
			set_sum_value('b5','d5',180)

def sc7():
	global dictionary

	values = dictionary.get('parallel')
	for i in values:
		if i==('sc7','sa6') or i==('sa6','sc7'):
			set_equal('a1','b5')
			set_sum_value('a1','d5',180)
			set_sum_value('d1','d3',180)
			set_equal('d1','c3')
			set_similar('ar1','ar5')


			#always true in setup 1
			set_equal('c1','a5')
			set_equal('c2','b1')
			set_equal('c3','b4')
			set_equal('b5','a4')
			set_sum_value('c2','d2',180)
			set_sum_value('b1','d2',180)
			set_sum_value('c1','d4',180)
			set_sum_value('a5','d4',180)
			set_sum_value('d3','c3',180)
			set_sum_value('d3','b4',180)
			set_sum_value('d5','a4',180)
			set_sum_value('b5','d5',180)
		
	values = dictionary.get('perpendicular')
	#for i in values:
		#if i==['sc6','sc7'] or i==['sc7','sc6']:
			#NIL

			#b2angle = 90
			#set_sum_value(dictionary,'a3','d1',90)
			#set_sum_value(dictionary,'a2','c2',90)


def sa7():
	global dictionary

	values = dictionary.get('parallel')
	for i in values:
		if i==('sa7','sb6') or i==('sb6','sa7'):
			set_equal('d1','c2')
			set_sum_value('d1','d2',180)
			set_similar('ar5','ar4')


			#always true in setup 1
			set_equal('c1','a5')
			set_equal('c2','b1')
			set_equal('c3','b4')
			set_equal('b5','a4')
			set_sum_value('c2','d2',180)
			set_sum_value('b1','d2',180)
			set_sum_value('c1','d4',180)
			set_sum_value('a5','d4',180)
			set_sum_value('d3','c3',180)
			set_sum_value('d3','b4',180)
			set_sum_value('d5','a4',180)
			set_sum_value('b5','d5',180)

	values = dictionary.get('perpendicular')
	for i in values:
		#if i==['sc6','sa7'] or i==['sa7','sc6']:
			#NIL

			#set_sum_value(dictionary,'b3','c3',90)
			#set_sum_value(dictionary,'b2','d1',90)
		if i==('sa7','sa6') or i==('sa6','sa7'):
			set_sum_value('a4','c4',90)
			set_sum_value('a3','b3',90)
			b4angle = 90

			#always true in setup 1
			set_equal('c1','a5')
			set_equal('c2','b1')
			set_equal('c3','b4')
			set_equal('b5','a4')
			set_sum_value('c2','d2',180)
			set_sum_value('b1','d2',180)
			set_sum_value('c1','d4',180)
			set_sum_value('a5','d4',180)
			set_sum_value('d3','c3',180)
			set_sum_value('d3','b4',180)
			set_sum_value('d5','a4',180)
			set_sum_value('b5','d5',180)


def sb6():
	global dictionary

	values = dictionary.get('perpendicular')
	for i in values:
		if i==('sb6','sb7') or i==('sb7','sb6'):
			set_equal('c2','d2')
			set_equal('c2','b1')
			set_equal('d2','b1')
			c2angle = 90
			d2angle = 90
			b1angle = 90
			set_sum_value('a2','b2',90)
			set_sum_value('a1','c1',90)
			set_similar('ar5','ar4')

			#always true in setup 1
			set_equal('c1','a5')
			set_equal('c2','b1')
			set_equal('c3','b4')
			set_equal('b5','a4')
			set_sum_value('c2','d2',180)
			set_sum_value('b1','d2',180)
			set_sum_value('c1','d4',180)
			set_sum_value('a5','d4',180)
			set_sum_value('d3','c3',180)
			set_sum_value('d3','b4',180)
			set_sum_value('d5','a4',180)
			set_sum_value('b5','d5',180)

	values = dictionary.get('equal')
	for i in values:
		if i==('sa6','sb6') or i==('sb6','sa6'):
			set_equal('a2','b3')

def sa6():
	global dictionary

	values = dictionary.get('parallel')
	for i in values:
		if i==('sc7','sa6') or i==('sa6','sc7'):
			set_equal('a1','b5')
			set_sum_value('a1','d5',180)
			set_sum_value('d1','d3',180)
			set_equal('d1','c3')
			set_similar('ar1','ar5')

			#always equal in setup 1
			set_equal('c1','a5')
			set_equal('c2','b1')
			set_equal('c3','b4')
			set_equal('b5','a4')
			set_sum_value('c2','d2',180)
			set_sum_value('b1','d2',180)
			set_sum_value('c1','d4',180)
			set_sum_value('a5','d4',180)
			set_sum_value('d3','c3',180)
			set_sum_value('d3','b4',180)
			set_sum_value('d5','a4',180)
			set_sum_value('b5','d5',180)


	values = dictionary.get('equal')
	for i in values:
		if i==('sa6','sb6') or i==('sb6','sa6'):
			set_equal('a2','b3')


def sb7():
	global dictionary

	values = dictionary.get('perpendicular')
	for i in values:
		if i==('sb6','sb7') or i==('sb7','sb6'):
			set_equal('c2','d2')
			set_equal('c2','b1')
			set_equal('d2','b1')
			c2angle = 90
			d2angle = 90
			b1angle = 90
			set_sum_value('a2','b2',90)
			set_sum_value('a1','c1',90)
			
			#always true in setup 1
			set_equal('c1','a5')
			set_equal('c2','b1')
			set_equal('c3','b4')
			set_equal('b5','a4')
			set_sum_value('c2','d2',180)
			set_sum_value('b1','d2',180)
			set_sum_value('c1','d4',180)
			set_sum_value('a5','d4',180)
			set_sum_value('d3','c3',180)
			set_sum_value('d3','b4',180)
			set_sum_value('d5','a4',180)
			set_sum_value('b5','d5',180)



	values = dictionary.get('parallel')
	for i in values:
		if i==('sb7','sc6') or i==('sc6', 'sb7'):
			#print("True")	
			set_equal('b2','a1')
			set_equal('a3','c4')
			set_similar('ar2','ar1')
			set_similar('ar3','ar4')

			#always true in setup 1
			set_equal('c1','a5')
			set_equal('c2','b1')
			set_equal('c3','b4')
			set_equal('b5','a4')
			set_sum_value('c2','d2',180)
			set_sum_value('b1','d2',180)
			set_sum_value('c1','d4',180)
			set_sum_value('a5','d4',180)
			set_sum_value('d3','c3',180)
			set_sum_value('d3','b4',180)
			set_sum_value('d5','a4',180)
			set_sum_value('b5','d5',180)


def a5():
	global dictionary

	values = dictionary.get('equal')
	for i in values:
		if i==('a5','b5') or i==('b5','a5'):
			set_equal('sb5','sa5')

			#always equal in setup 1
			set_equal('c1','a5')
			set_equal('c2','b1')
			set_equal('c3','b4')
			set_equal('b5','a4')
			set_sum_value('c2','d2',180)
			set_sum_value('b1','d2',180)
			set_sum_value('c1','d4',180)
			set_sum_value('a5','d4',180)
			set_sum_value('d3','c3',180)
			set_sum_value('d3','b4',180)
			set_sum_value('d5','a4',180)
			set_sum_value('b5','d5',180)


def a4():
	global dictionary

	values = dictionary.get('equal')
	for i in values:
		if i == ('a4','b4') or i==('b4','a4'):
			set_equal('sa4','sb4')

			#always equal in setup 1
			set_equal('c1','a5')
			set_equal('c2','b1')
			set_equal('c3','b4')
			set_equal('b5','a4')
			set_sum_value('c2','d2',180)
			set_sum_value('b1','d2',180)
			set_sum_value('c1','d4',180)
			set_sum_value('a5','d4',180)
			set_sum_value('d3','c3',180)
			set_sum_value('d3','b4',180)
			set_sum_value('d5','a4',180)
			set_sum_value('b5','d5',180)





def ar2():
	values = dictionary.get('congruent')
	for i in values:
		if i==('ar2','ar3') or i==('ar3','ar2'):
			set_equal('c3','c2')
			set_equal('a2','b3')
			set_equal('a3','b2')
			set_equal('sa3','sb2')
			set_equal('sb3','sa2')
			set_equal('sc2','sc3')
			
			#always equal in setup 1
			set_equal('c1','a5')
			set_equal('c2','b1')
			set_equal('c3','b4')
			set_equal('b5','a4')
			set_sum_value('c2','d2',180)
			set_sum_value('b1','d2',180)
			set_sum_value('c1','d4',180)
			set_sum_value('a5','d4',180)
			set_sum_value('d3','c3',180)
			set_sum_value('d3','b4',180)
			set_sum_value('d5','a4',180)
			set_sum_value('b5','d5',180)




dictionary={
	'parallel': set(),
	'perpendicular': set(),
	'equal': set(),
	'fraction': set(),
	'sum_value': set(),
	'similar': set(),
	'congruent': set(),
	'tan': set()
}

if __name__=='__main__':
	
	set_parallel('sb7','sc6')

	get_all()


