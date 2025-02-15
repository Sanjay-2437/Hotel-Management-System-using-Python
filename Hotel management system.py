import random
import datetime

# Global List Declaration 
name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []

# Global Variable Declaration

i = 0

# Home Function
def Home():
	
	print("\t\t\t\t\t\t WELCOME TO HOTEL CONDOTIERRE\n")
	print("\t\t\t 1 Booking\n")
	print("\t\t\t 2 Rooms Info\n")
	print("\t\t\t 3 Payment\n")
	print("\t\t\t 4 Record\n")
	print("\t\t\t 0 Exit\n")

	ch=int(input("->"))
	
	if ch == 1:
		print(" ")
		Booking()
	
	elif ch == 2:
		print(" ")
		Rooms_Info()
	
	elif ch == 3:
		print(" ")
		Payment()
	
	elif ch == 4:
		print(" ")
		Record()
	
	else:
		exit()


# Booking function 
def Booking():
	
		# used global keyword to 
		# use global variable 'i'
		global i
		print(" BOOKING ROOMS")
		print(" ")
		
		while 1:
			n = str(input("Name: "))
			p1 = str(input("Phone No.: "))
			a = str(input("Address: "))
			
			# checks if any field is not empty
			if n!="" and p1!="" and a!="":
				name.append(n)
				add.append(a)
				break
				
			else:
				print("\tName, Phone no. & Address cannot be empty..!!")
			
		cii=str(input("Check-In: "))
		checkin.append(cii)
		cii=cii.split('/')
		ci=cii
		ci[0]=int(ci[0])
		ci[1]=int(ci[1])
		ci[2]=int(ci[2])
		
		
		coo=str(input("Check-Out: "))
		checkout.append(coo)
		coo=coo.split('/')
		co=coo
		co[0]=int(co[0])
		co[1]=int(co[1])
		co[2]=int(co[2])
		
		# checks if check-out date falls after 
		# check-in date
		if co[1]<ci[1] and co[2]<ci[2]:
			
			print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
			name.pop(i)
			add.pop(i)
			checkin.pop(i)
			checkout.pop(i)
			Booking()
		elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
			
			print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
			name.pop(i)
			add.pop(i)
			checkin.pop(i)
			checkout.pop(i)
			Booking()
		else:
			pass
		
	
		d1 = datetime.datetime(ci[2],ci[1],ci[0])
		d2 = datetime.datetime(co[2],co[1],co[0])
		d = (d2-d1).days
		day.append(d)
		
		print("\n----SELECT ROOM TYPE----")
		print(" 1. Standard Room")
		print(" 2. Family-Size Room")
		print(" 3. Studio Room")
		print(" 4. Suite Room")
		print(("\t\tPress 0 for Room Prices"))
		
		ch=int(input("->"))
		
		# if-conditions to display allotted room
		# type and it's price
		if ch==0:
			print(" 1. Standard Room - Rs. 3500")
			print(" 2. Family-Size Room - Rs. 4000")
			print(" 3. Studio Room - Rs. 4500")
			print(" 4. Suite Room - Rs. 5000")
			ch=int(input("->"))
		if ch==1:
			room.append('Standard Room')
			print("Room Type- Standard Room") 
			price.append(3500)
			print("Price- 3500")
		elif ch==2:
			room.append('Family-Size Room')
			print("Room Type- Family-Size Room")
			price.append(4000)
			print("Price- 4000")
		elif ch==3:
			room.append('Studio Room')
			print("Room Type- Studio Room")
			price.append(4500)
			print("Price- 4500")
		elif ch==4:
			room.append('Suite Room')
			print("Room Type- Suite Room")
			price.append(5000)
			print("Price- 5000")
		else:
			print(" Wrong choice..!!")


		# randomly generating room no. and customer 
		# id for customer
		rn = random.randrange(40)+300
		cid = random.randrange(40)+10
		
		
		# checks if allotted room no. & customer 
		# id already not allotted
		while rn in roomno or cid in custid:
			rn = random.randrange(60)+300
			cid = random.randrange(60)+10
			
		rc.append(0)
		p.append(0)
			
		if p1 not in phno:
			phno.append(p1)
		elif p1 in phno:
			for n in range(0,i):
				if p1== phno[n]:
					if p[n]==1:
						phno.append(p1)
		elif p1 in phno:
			for n in range(0,i):
				if p1== phno[n]:
					if p[n]==0:
						print("\tPhone no. already exists and payment yet not done..!!")
						name.pop(i)
						add.pop(i)
						checkin.pop(i)
						checkout.pop(i)
						Booking()
		print("")
		print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
		print("Room No. - ",rn)
		print("Customer Id - ",cid)
		roomno.append(rn)
		custid.append(cid)
		i=i+1
		n=int(input("0-BACK\n ->"))
		if n==0:
			Home()
		else:
			exit()

# ROOMS INFO 
def Rooms_Info():
	print("		 ------ HOTEL ROOMS INFO ------")
	print("")
	print("STANDARD Room")
	print("---------------------------------------------------------------")
	print("Room amenities include: Single bed with attached washroom and AC\n")
	print("Family-Size Room")
	print("---------------------------------------------------------------")
	print("Room amenities include: Double bed with attached washroom and AC\n")
	print("Studio Room")
	print("---------------------------------------------------------------")
	print("Room amenities include: 1 Double bed and 1 Single Bed with 2 attached washrooms, AC and private balcony\n")
	print("Suite Room")
	print("---------------------------------------------------------------")
	print("Room amenities include: 2 Double Beds with 2 attached washrooms, centralised AC and 2 private balconies\n\n")
	print()
	n=int(input("0-BACK\n ->"))
	if n==0:
		Home()
	else:
		exit()
	
				
# PAYMENT FUNCTION			 
def Payment():
	
	ph=str(input("Phone Number: "))
	global i
	f=0
	
	for n in range(0,i):
		if ph==phno[n] :
			
			# checks if payment is
			# not already done
			if p[n]==0:
				f=1
				print(" Payment")
				print(" --------------------------------")
				print(" MODE OF PAYMENT")
				
				print(" 1- Credit/Debit Card")
				print(" 2- NetBanking")
				print(" 3- Using UPI")
				print(" 4- Cash")
				x=int(input("-> "))
				print("\n Amount: ",(price[n]*day[n])+rc[n])
				print("\n		 Pay For your stay in Hotel Condotierre")
				print(" (y/n)")
				ch=str(input("->"))
				
				if ch=='y' or ch=='Y':
					print("		 Hotel Condotierre")
                    
					print("			 Bill\n")
					print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
					print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t")
					print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t")

					print("\n Total Amount: ",(price[n]*day[n])+rc[n],"\t")
					print(" --------------------------------")					
                  
					print(" Thank You, Visit Again :)")
					print(" --------------------------------\n")
					p.pop(n)
					p.insert(n,1)
					
					# pops room no. and customer id from list and 
					# later assigns zero at same position
					roomno.pop(n)
					custid.pop(n)
					roomno.insert(n,0)
					custid.insert(n,0)
					
			else:
				
				for j in range(n+1,i):
					if ph==phno[j] :
						if p[j]==0:
							pass
						
						else:
							f=1
							print("\n\tPayment has been Made :)\n\n") 
	if f==0: 
		print("Invalid Customer Id")
		
	n = int(input("0-BACK\n ->"))
	if n == 0:
		Home()
	else:
		exit()

# RECORD FUNCTION 
def Record():
	
	# checks if any record exists or not
	if phno!=[]:
		print("	 *** HOTEL RECORD ***\n")
		print("| Name | Phone No. | Address	 | Check-In | Check-Out	 | Room Type | Price	 |")
		print("----------------------------------------------------------------------------------------------------------------------")
		
		for n in range(0,i):
			print("|",name[n],"\t |",phno[n],"\t|",add[n],"\t|",checkin[n],"\t|",checkout[n],"\t|",room[n],"\t|",price[n])
		
		print("----------------------------------------------------------------------------------------------------------------------")
	
	else:
		print("No Records Found")
	n = int(input("0-BACK\n ->"))
	if n == 0:
		Home()
		
	else:
		exit()

# Driver Code 
Home()
