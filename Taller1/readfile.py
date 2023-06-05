path = r'C:\Users\andre\OneDrive\Documentos\pyton_Team_International\text_to_python.txt'

def read():
    
    with open(path, 'r') as archivo:    # Open the file and read its content
        content = archivo.read().lower()
        
        words = content.split()    # Split the content into words
        
        print(content)
        print(words)
    
    
    return words   # Return the list of words

def counter(word_list):
    
    count_times = {}  # Create an empty dictionary to store word counts
    
    
    for word in word_list:  
        
        if word not in count_times: 
            
            count_times[word] = 1   # If the word is not in the dictionary, add it with a count of 1
        else:
            
            count_times[word] += 1   # Step 9: If the word is already in the dictionary, increment its count by 1
    
    return count_times


word_list = read() 

word_count = counter(word_list)  # Count the occurrence of each word in the list

print(word_count)


