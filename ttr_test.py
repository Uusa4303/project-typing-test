"""#for generating random words from list for a certain amount of time and taking input simuntaneously
import time
import random
words = ['Trucks', 'are', 'heavy-duty', 'vehicles', 'designed', 'for', 'transporting', 'goods', 'and', 'materials.', 'They', 'are', 'used', 'in', 'various', 'industries', 'such', 'as', 'construction,', 'agriculture,', 'and', 'logistics.', 'Trucks', 'come', 'in', 'different', 'sizes', 'and', 'types,', 'from', 'small', 'pickup', 'trucks', 'to', 'large', 'semi-trailers.', 'They', 'are', 'equipped', 'with', 'powerful', 'engines,', 'durable', 'frames,', 'and', 'specialized', 'equipment', 'for', 'carrying', 'and', 'unloading', 'cargo.', 'Despite', 'their', 'importance', 'to', 'the', 'economy,', 'trucks', 'also', 'contribute', 'to', 'air', 'pollution', 'and', 'traffic', 'congestion,', 'leading', 'to', 'calls', 'for', 'cleaner', 'and', 'more', 'efficient', 'transportation', 'solutions.']
i=0
j=0
k=0
while i<2 and j<1000 and k<1000 :
    word = random.choice(words)
    print(word)
    response = input("type :")
    if response == word :
       print("correct")
       j+=1
    else :
      print("wrong")
      k+=1
    
    time.sleep(1)
    i+=1
    p=((j/i)*100)
print("accuracy:",p,"%")"""
#========================================================================================================================

#to take the sentences input and convert them into list ouput.
"""sentence = input("Enter a sentence: ")

# Split the sentence into a list of words
words = sentence.split()

# Print the list of words
print(words)"""
#=================================================================
#can check the accuracy and generate random words for one minute.
import time
import random

words = ['Trucks', 'are', 'heavy-duty', 'vehicles', 'designed', 'for', 'transporting', 'goods', 'and', 'materials.', 'They', 'are', 'used', 'in', 'various', 'industries', 'such', 'as', 'construction,', 'agriculture,', 'and', 'logistics.', 'Trucks', 'come', 'in', 'different', 'sizes', 'and', 'types,', 'from', 'small', 'pickup', 'trucks', 'to', 'large', 'semi-trailers.', 'They', 'are', 'equipped', 'with', 'powerful', 'engines,', 'durable', 'frames,', 'and', 'specialized', 'equipment', 'for', 'carrying', 'and', 'unloading', 'cargo.', 'Despite', 'their', 'importance', 'to', 'the', 'economy,', 'trucks', 'also', 'contribute', 'to', 'air', 'pollution', 'and', 'traffic', 'congestion,', 'leading', 'to', 'calls', 'for', 'cleaner', 'and', 'more', 'efficient', 'transportation', 'solutions.']

start_time = time.time()
elapsed_time = 0
i = 0
j = 0
k = 0

while elapsed_time < 60 and j < 1000 and k < 1000:
    word = random.choice(words)
    print(word)
    response = input("type: ")
    if response == word:
        print("correct")
        j += 1
    else:
        print("wrong")
        k += 1
    
    elapsed_time = time.time() - start_time
    i += 1
    p = ((j / i) * 100)

print("accuracy:", p, "%")
print("no.of words=",(i))