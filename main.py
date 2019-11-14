def make_dictionary():
	dictionary = dict()
	dictionary['parallel'] = []
	dictionary['perpendicular'] = []
	dictionary['equal'] = []
	dictionary['fraction'] = []
	dictionary['sum_value'] = []
	dictionary['similar'] = []
	dictionary['congruent'] = []
	dictionary['tan'] = []
	return dictionary

def get_all(dictionary):
	print(dictionary)

def set_parallel(dictionary,a,b):
	dictionary['parallel'].append([a,b])

def set_perpendicular(dictionary,a,b):
	dictionary['perpendicular'].append([a,b])

def set_equal(dictionary,a,b):
	dictionary['equal'].append([a,b])

def set_fraction(dictionary,a,b,frac):
	dictionary['fraction'].append([a,b,frac])

def set_sum_value(dictionary,a,b,sum):
	dictionary['sum_value'].append([a,b,sum])

def set_similar(dictionary,a,b):
	dictionary['similar'].append([a,b])

def set_congruent(dictionary,a,b):
	dictionary['congruent'].append([a,b])

def set_tan(dictionary,a,b):
	dictionary['tan'].append([a,b])

def sc6(dictionary):
	values = dictionary.get('parallel')
	#print(values)
	for i in values:
		if i==['sb7','sc6'] or i==['sc6', 'sb7']:
			#print("True")	
			set_equal(dictionary,'b2','a1')
			set_equal(dictionary,'a3','c4')
	values = dictionary.get('perpendicular')
	for i in values:
		if i==['sc6','sc7'] or i==['sc7','sc6']:
			b2angle = 90
			set_sum_value(dictionary,'a3','d1',90)
			set_sum_value(dictionary,'a2','c2',90)
		if i==['sc6','sa7'] or i==['sa7','sc6']:
			set_sum_value(dictionary,'b3','c3',90)
			set_sum_value(dictionary,'b2','d1',90)

def sc7(dictionary):
	values = dictionary.get('parallel')
	for i in values:
		if i==['sc7','sa6'] or i==['sa6','sc7']:
			set_equal(dictionary,'a1','b5')
			set_sum_value(dictionary,'a1','d5',180)
			set_sum_value(dictionary,'d1','d3',180)
			set_equal(dictionary,'d1','c3')
		
	values = dictionary.get('perpendicular')
	for i in values:
		if i==['sc6','sc7'] or i==['sc7','sc6']:
			b2angle = 90
			set_sum_value(dictionary,'a3','d1',90)
			set_sum_value(dictionary,'a2','c2',90)


def sa7(dictionary):
	values = dictionary.get('parallel')
	for i in values:
		if i==['sa7','sb6'] or i==['sb6','sa7']:
			set_equal(dictionary,'d1','c2')
			set_sum_value(dictionary,'d1','d2',180)

	values = dictionary.get('perpendicular')
	for i in values:
		if i==['sc6','sa7'] or i==['sa7','sc6']:
			set_sum_value(dictionary,'b3','c3',90)
			set_sum_value(dictionary,'b2','d1',90)
		if i==['sa7','sa6'] or i==['sa6','sa7']:
			set_sum_value(dictionary,'a4','c4',90)
			set_sum_value(dictionary,'a3','b3',90)
			b4angle = 90


def sb6(dictionary):
	values = dictionary.get('perpendicular')
	for i in values:
		if i==['sb6','sb7'] or i==['sb7','sb6']:
			set_equal(dictionary,'c2','d2')
			set_equal(dictionary,'c2','b1')
			set_equal(dictionary,'d2','b1')
			c2angle = 90
			d2angle = 90
			b1angle = 90
			set_sum_value(dictionary,'a2','b2',90)
			set_sum_value(dictionary,'a1','c1',90)

	values = dictionary.get('equal')
	for i in values:
		if i==['sa6','sb6'] or i==['sb6','sa6']:
			set_equal(dictionary,'a2','b3')

def sa6(dictionary):
	values = dictionary.get('parallel')
	for i in values:
		if i==['sc7','sa6'] or i==['sa6','sc7']:
			set_equal(dictionary,'a1','b5')
			set_sum_value(dictionary,'a1','d5',180)
			set_sum_value(dictionary,'d1','d3',180)
			set_equal(dictionary,'d1','c3')

	values = dictionary.get('equal')
	for i in values:
		if i==['sa6','sb6'] or i==['sb6','sa6']:
			set_equal(dictionary,'a2','b3')


def sb7(dictionary):
	values = dictionary.get('perpendicular')
	for i in values:
		if i==['sb6','sb7'] or i==['sb7','sb6']:
			set_equal(dictionary,'c2','d2')
			set_equal(dictionary,'c2','b1')
			set_equal(dictionary,'d2','b1')
			c2angle = 90
			d2angle = 90
			b1angle = 90
			set_sum_value(dictionary,'a2','b2',90)
			set_sum_value(dictionary,'a1','c1',90)
			
		if i==['sb7','sc6'] or i==['sc6', 'sb7']:
			#print("True")	
			set_equal(dictionary,'b2','a1')
			set_equal(dictionary,'a3','c4')


def ar2(dictionary):
	values = dictionary.get('congruent')
	for i in values:
		if i==['ar2','ar3'] or i==['ar3','ar2']:
			set_equal(dictionary,'c3','c2')
			set_equal(dictionary,'a2','b3')
			set_equal(dictionary,'a3','b2')
			set_equal(dictionary,'sa3','sb2')
			set_equal(dictionary,'sb3','sa2')
			set_equal(dictionary,'sc2','sc3')



def always_true(dictionary):
	set_equal(dictionary,'c1','a5')
	set_equal(dictionary,'c2','b1')
	set_equal(dictionary,'c3','b4')
	set_equal(dictionary,'b5','a4')
	set_sum_value(dictionary,'c2','d2',180)
	set_sum_value(dictionary,'b1','d2',180)
	set_sum_value(dictionary,'c1','d4',180)
	set_sum_value(dictionary,'a5','d4',180)
	set_sum_value(dictionary,'d3','c3',180)
	set_sum_value(dictionary,'d3','b4',180)
	set_sum_value(dictionary,'d5','a4',180)
	set_sum_value(dictionary,'b5','d5',180)

if __name__=='__main__':

	dictionary = make_dictionary()
	always_true(dictionary)

	set_parallel(dictionary,'sb7','sc6')
	
	#get_all(dictionary)
	sc6(dictionary)
	get_all(dictionary)


