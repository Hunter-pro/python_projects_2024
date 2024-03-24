
import pandas


data = pandas.read_csv('./nato_phenotics/nato_phonetic_alphabet.csv')

alpha_code_dict = {row.letter:row.code for (index,row) in data.iterrows() }

def generate_phenoticList():
    user_input = input('Enter a word:').upper()
    try:
        code_list = [alpha_code_dict[letter] for letter in user_input ]
    except KeyError:
        print('sorry,please enter a letter in alphabet')
        generate_phenoticList()
    else:
        print(code_list)

generate_phenoticList()
