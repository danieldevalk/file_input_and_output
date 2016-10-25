def make_backwards_phonebook(phbook_file,back_phbook_file):
    file_object = open(phbook_file+".tsv", 'r')
    phone_book = file_object.read()
    phone_list = phone_book.split('\t')
    phonebook = {}
    reverse_phonebook={}
    for num in phone_list:
        if num[0].isdigit() and num[-1].isalpha():
            phonebook[num[13:]] = num[0:12]
    print(phonebook)
    for key in phonebook.keys():
        reverse_phonebook[phonebook[key]]=key
    print(reverse_phonebook)

    new_file_object = open(back_phbook_file+".tsv", 'w')
    
    for num in reverse_phonebook:
        new_file_object.write(reverse_phonebook[num])
        new_file_object.write(num)
        new_file_object.write("\t")
        print("new")
        print(num)
        print(reverse_phonebook[num])
        
        
def user_input_make_bw_phonebook():
    input_filename = input('What file are you inputting?')
    output_filename = input('What file are you outputting?')
    try:
        make_backwards_phonebook(input_filename, output_filename)
    except:
        print("There was an error with your file name!")
    
make_backwards_phonebook('009_phone', '009_phone_back')

def holidays_with_dates():
    new_message=''
    holidays = {'Christmas':'12/25/2015', 'Halloween':'10/31/2015', 'Thanksgiving':'11/24/2015', "Valentines":'2/14/2015', "Passover":'3/17/2015', "Easter":'3/23/2015', "Birthday":'12/31/2015'}
    message=input("Please type a message. ")
    for num in message:
        message=message.replace(".","")
        message=message.replace("?","")
        message=message.replace("!","")
    message.lower()
    split_message=message.split()

    for num in split_message:
        if num in holidays:
            split_message[split_message.index(num)] = holidays[num]
    for num in split_message:
        new_message+=num
        new_message+=' '
    print(new_message)
holidays_with_dates()
    

def word_freq(text_file,back_text_file):
    word_dictionary={}
    string=''
    text_file = open(text_file+".txt", 'r')
    new_dictionary = open(back_text_file+".tsv", 'w')
    all_lines = text_file.readlines()
    for line in all_lines:
        #line = "i am a line"
        words = line.split(" ")
        #words = ["i","am","a","line"]
        for word in words:
            print("word is:",word)
            strip_word = word.strip(".?!,'\"\n\t")
            if strip_word in word_dictionary:
                word_dictionary[strip_word]=word_dictionary[strip_word]+1
            else:
                word_dictionary[strip_word] = 1
            print("stripped word is:",strip_word)
            string += strip_word + " "
        string+=' '
    print(string)

    for num in word_dictionary:
        new_dictionary.write(num + ':')
        new_dictionary.write(str(word_dictionary[num]))
        new_dictionary.write('\t')
    
word_freq("example_text", "nonexample")
