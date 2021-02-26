nameList = []
def app():
	print('\nWhat u want to do?')
	print('1.Add Name \n2.See Name list \n3.Exit')
	counter = int(input())
	if counter == 1 : 
		print('Enter a new name')
		newName = str(input())
		nameList.append(newName)
		return app()
		
	elif counter == 2 :
		if len(nameList) == 0:
			print('\nName list is empty')	
		print('\nYour Name List: \n')	
		print('\n'.join(nameList))	
		return app()
	elif counter == 3 :
    		return 0	
	else :
		print('U entered a wrong value')			
		return app()
app()