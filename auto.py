
from keras.models import load_model

m=load_model("model.h5")

predicted_label=["ka","ga","ee"]
i=0
d={"ka":1,"ga":1,"ee":4}
output=[]
while i<len(predicted_label):
	a=False
	if d[predicted_label[i]]==4:#this is for the velanti
		i+=1
		if d[predicted_label[i]]==2:#this is for khanha
			i+=1
			if d[predicted_label[i]]==1:#this is for letter
				if predicted_label[i]=="ga" or predicted_label[i]=="naa":
					#it should have an extra kanha
					i+=1
					if predicted_label[i]==2:
					    output.append(2)#give output
					else:
						break
				else:
					output.append(1)#give output
			else:
				#invalid 
				break

		elif d[predicted_label[i]]==1:#this is for second velanti
			if predicted_label[i]=="ga" or predicted_label[i]=="naa":
				#it should have an extra kanha
				i+=1
				if predicted_label[i]==2:
					i+=1	
					if d[predicted_label[i]]==2:
						output.append(3)#give output
					else:
						break
				else:
					break
			i+=1	
			if d[predicted_label[i]]==2:
				output.append(4)#give output
			else:
				break	
		else:
			break
	#this is commented since we have not segmented the ukar part
	# else if d[predicted_label[i]]==5:#this is for the ukar
	# 	i+=1
	# 	if d[predicted_label[i]]==1:#this is for the letter
	# 		if predicted_label[i]=="ga" or predicted_label[i]=="naa":
	# 			#it should have an extra kanha
	# 			i+=1
	# 			if predicted_label[i]==2:
	# 				out.append()#give output
	# 			else: 
	# 				break
	# 		else:
	# 			out.append()#give output		
	elif d[predicted_label[i]]==3:#this is for the matra
		i+=1
		if d[predicted_label[i]]==1:#this is for the letter
			if predicted_label[i]=="ga" or predicted_label[i]=="naa":
				#it should have an extra kanha
				i+=1
				if predicted_label[i]==2:
					i+=1
					if predicted_label[i]==2:#if the letter is goo or gaoo i.e extra kanhna
						output.append(6)#give output
					else:
						i-=1#there is no extra kanha so it is completely different letter
						output.append(7)#id it is gey or geay
				else: 
					break
			else:
				#for other letters
				i+=1
				if predicted_label[i]==2:#letter with extra kanha i.e koo or kau
					output.append(8)
				else:#key or kaey
					i-=1#there is no extra kanha so it is completely different letter
					output.append(10)
		else:
			break		
			
	elif d[predicted_label[i]]==1:#this is for the letter 
			if predicted_label[i]=="ga" or predicted_label[i]=="naa":
				#it should have an extra kanha
				i+=1
				if predicted_label[i]==2:
					i+=1
					if predicted_label[i]==2:#if gaa 
						output.append(12)#give output
					else:
						i-=1#there is no extra kanha so it is completely different letter
						output.append(14)
				else: 
					break
			else:
				#for other letters
				i+=1
				if predicted_label[i]==2:#letter with extra kanha i.e kaa
					output.append(3)
				else:#ka simply letter
					i-=1#there is no extra kanha so it is completely different letter
					output.append(4)
 
	else:
		break
	
	a=True
		


	
	
