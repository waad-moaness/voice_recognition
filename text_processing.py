import re
import contractions
from num2words import num2words

text = "I'm in college now, and I'm testing the model against real noise."
text2 = "I am in college now, and I am testing the model against real noise."
t3= "Let's go to the café for a croissant."
t4 = "Rice is often served in round bowls."
t5 = "rice's often served in round bowls"
tt = "John's car"
ttt= "has it been a long time since i've talked"
numstr = "the total is 19.99 $"
numstr2 = "the total is nineteen point ninety nine "

def text_preprocessing(text):
    text = text.lower().strip()
    text = contractions.fix(text)
    # handle decimals 
    def convert_decimal(match):
        number = match.group(0)
        integer, decimal = number.split(".")
        integer_words = num2words(int(integer))
        decimal_words = num2words(int(decimal))
        return f"{integer_words} point {decimal_words}"
    # convert decimal numbers first
    text = re.sub(r"\b\d+\.\d+\b", convert_decimal, text)
    # convert integers
    text = re.sub(r"\b\d+\b", lambda x: num2words(int(x.group(0))), text)
    # remove punctuation
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.split()


print(text_preprocessing(text))
print(text_preprocessing(text2))
print(text_preprocessing(t3))
print(text_preprocessing(t4))
print(text_preprocessing(t5))
print(text_preprocessing(tt))
print(text_preprocessing(ttt))
print(text_preprocessing(numstr))
print(text_preprocessing(numstr2))
print(text_preprocessing("temperature is 4.05 degrees"))