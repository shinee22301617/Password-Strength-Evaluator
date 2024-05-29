import flask
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import nltk
# nltk.download('words')
from nltk.corpus import words
setofword = set(words.words())

#define function
def keyboard_table(c):
  x = -1
  y = -1
  if(c=='~' or c == '`'):
    x = 0
    y = 0
  elif(c=='1' or c == '!'):
    x = 1
    y = 0
  elif(c=='2' or c == '@'):
    x = 2
    y = 0
  elif(c=='#' or c == '3'):
    x = 3
    y = 0
  elif(c=='4' or c == '$'):
    x = 4
    y = 0
  elif(c=='5' or c == '%'):
    x = 5
    y = 0
  elif(c=='6' or c == '^'):
    x = 6
    y = 0
  elif(c=='7' or c == '&'):
    x = 7
    y = 0
  elif(c=='8' or c == '*'):
    x = 8
    y = 0
  elif(c=='9' or c == '('):
    x = 9
    y = 0
  elif(c=='0' or c == ')'):
    x = 10
    y = 0
  elif(c=='-' or c == '_'):
    x = 11
    y = 0
  elif(c=='=' or c == '+'):
    x = 12
    y = 0
  elif(c=='q' or c == 'Q'):
    x = 1
    y = 1
  elif(c=='w' or c == 'W'):
    x = 2
    y = 1
  elif(c=='e' or c == 'E'):
    x = 3
    y = 1
  elif(c=='r' or c == 'R'):
    x = 4
    y = 1
  elif(c=='t' or c == 'T'):
    x = 5
    y = 1
  elif(c=='y' or c == 'Y'):
    x = 6
    y = 1
  elif(c=='u' or c == 'U'):
    x = 7
    y = 1
  elif(c=='i' or c == 'I'):
    x = 8
    y = 1
  elif(c=='o' or c == 'O'):
    x = 9
    y = 1
  elif(c=='p' or c == 'P'):
    x = 10
    y = 1
  elif(c=='[' or c == '{'):
    x = 11
    y = 1
  elif(c==']' or c == '}'):
    x = 12
    y = 1
  elif(c=='\\' or c == '|'):
    x = 13
    y = 1
  elif(c=='a' or c == 'A'):
    x = 1
    y = 2
  elif(c=='s' or c == 'S'):
    x = 2
    y = 2
  elif(c=='d' or c == 'D'):
    x = 3
    y = 2
  elif(c=='F' or c == 'f'):
    x = 4
    y = 2
  elif(c=='g' or c == 'G'):
    x = 5
    y = 2
  elif(c=='h' or c == 'H'):
    x = 6
    y = 2
  elif(c=='j' or c == 'J'):
    x = 7
    y = 2
  elif(c=='k' or c == 'K'):
    x = 8
    y = 2
  elif(c=='l' or c == 'L'):
    x = 9
    y = 2
  elif(c==';' or c == ':'):
    x = 10
    y = 2
  elif(c=="'" or c == '"'):
    x = 11
    y = 2
  elif(c=='z' or c == 'Z'):
    x = 1
    y = 3
  elif(c=='x' or c == 'X'):
    x = 2
    y = 3
  elif(c=='c' or c == 'C'):
    x = 3
    y = 3
  elif(c=='v' or c == 'V'):
    x = 4
    y = 3
  elif(c=='b' or c == 'B'):
    x = 5
    y = 3
  elif(c=='n' or c == 'N'):
    x = 6
    y = 3
  elif(c=='m' or c == 'M'):
    x = 7
    y = 3
  elif(c==',' or c == '<'):
    x = 8
    y = 3
  elif(c=='.' or c == '>'):
    x = 9
    y = 3
  elif(c=='/' or c == '?'):
    x = 10
    y = 3
  
  return x,y


def cal_len(x):
  x=str(x)  
  return len(x)

def cal_capital(x):
  x=str(x)
  cnt=0
  for i in x:
    if(i.isupper()):
      cnt = cnt + 1
  return cnt

def cal_small(x):
  x=str(x)
  cnt=0
  for i in x:
    if(i.islower()):
      cnt = cnt + 1
  return cnt

def cal_spc(x):
  x=str(x)
  cnt = 0
  for i in x:
    if(i.isupper()):
      cnt = cnt + 1
    if(i.islower()):
      cnt = cnt + 1
    if(i.isnumeric()):
      cnt+=1
  return len(x)-cnt

def cal_num(x):
  x=str(x)
  cnt=0
  for i in x:
    if(i.isnumeric()):
      cnt+=1
  return cnt

def cal_adjacent(x):
  x=str(x)
  value = 0
  tmpx = -2
  tmpy = -2
  for i in x:
    x,y = keyboard_table(i)
    if(tmpx!=-2 and tmpy !=-2):
      value = value + abs(x-tmpx) + abs(y-tmpy)
    tmpy = y
    tmpx = x
  return value

def cal_adj_mean(x):
  #detect strings like abcde, 01234
  x=str(x)
  cnt = 0
  pos_alphabet = -1
  value_alphabet = 0
  lastpos_alphabet = -1
  pos_number = -1
  value_number = 0
  lastpos_number = -1
  value = 0
  for i in x:
    if(i.isnumeric()):
      pos_number = ord(i)
      if(lastpos_number!=-1):
        value_number = value_number + abs(pos_number-lastpos_number)
      lastpos_number = pos_number
    else:
      if(i.islower()):
        pos_alphabet = ord(i) - 97
        if(lastpos_alphabet!=-1):
          value_alphabet = value_alphabet + abs(pos_alphabet-lastpos_alphabet)
        lastpos_alphabet = pos_alphabet
      if(i.isupper()):
        pos_alphabet = ord(i) - 65
        if(lastpos_alphabet!=-1):
          value_alphabet = value_alphabet + abs(pos_alphabet-lastpos_alphabet)
        lastpos_alphabet = pos_alphabet
  value = value_alphabet+value_number
  return value

def cal_type(x):
  #calc how many type of character the string has
  x=str(x)
  flag = 0
  c_type = 0
  for i in range(0,len(x)):
    for j in range(0,i):
      if(x[j]==x[i]):
        flag = 1
        break
    if(flag == 0):
      c_type+=1
    flag = 0
  return c_type
  
def check_word(x):
  x = str(x)
  word = ""
  for i in range(0,len(x)):
    if(x[i].isalpha()):
      word = word + x[i]
  word = word.lower()
  for i in range(0,len(word)):
    for j in range(i,len(word)):
      tmpstr = word[i:j+1]
      # We don't detect word less than 2 characters
      if(len(tmpstr)<=2):
        continue
      if(tmpstr in setofword):
        return 1
  return 0

def check_long_word(x):
  x = str(x)
  word = ""
  for i in range(0,len(x)):
    if(x[i].isalpha()):
      word = word + x[i]
  word = word.lower()
  tmpp = 'hi'
  flag = 0
  for i in range(0,len(word)):
    for j in range(i,len(word)):
      tmpstr = word[i:j+1]
      # We don't detect word less than 2 characters
      if(len(tmpstr)<=2):
        continue
      if(tmpstr in setofword):
        flag+=1
        if(len(tmpstr)>len(tmpp)):
          tmpp = tmpstr
  return flag,tmpp

def passwd_to_input(password):
    l = []
    l.append(cal_len(password))
    l.append(cal_capital(password))
    l.append(cal_small(password))
    l.append(cal_spc(password))
    l.append(cal_num(password))
    l.append(cal_adjacent(password))
    l.append(cal_adj_mean(password))
    l.append(check_word(password))
    l.append(cal_type(password))
    return pd.DataFrame(l).T
#define function finished

#import model folder
model = keras.models.load_model("model/model")

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')



# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        password = flask.request.form['password']
        model_input = passwd_to_input(password)
        print('Input:',password)
        mi = model_input.to_numpy()

        count,longword = check_long_word(password)

        print(mi[0][1],mi[0][2],mi[0][4],mi[0][3])
        u = mi[0][1]
        l = mi[0][2]
        n = mi[0][4]
        s = mi[0][4]
        if(mi[0][1] > 0):
          u = 1
        else:
          u = 0
        
        if(mi[0][2] > 0):
          l = 1
        else:
          l = 0
        
        if(mi[0][4] > 0):
          n = 1
        else:
          n = 0
        
        if(mi[0][3] > 0):
          s = 1
        else:
          s = 0

        ax = np.array(['nanoseconds','microseconds','milliseconds','seconds','minutes',
        'hours','days','months','years','thousand years','million years','billion years',
        'trillion years','quadrillion years','quintillion years','sextillion years',
        'septillion','octillion','nonillion years'])
        ay = np.array([1000,1000,1000,60,60,24,30,365,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000])
        
        length = mi[0][0]

        mini = 0

        if(u):
            mini = mini + 26

        if(l):
            mini = mini + 26

        if(n):
            mini = mini + 10

        if(s):
            mini = mini + 10

        pico = pow(mini, (length.item()-1)) * 0.6

        i = 0
        while(pico > ay[i] and  i <= 17):
            pico = round(pico/ay[i],2)
            i = i+1
        
        print(pico,ax[i])
        pico = round(pico,2)
        prediction = model.predict(model_input).flatten()
        resulttf = tf.math.argmax(prediction, axis=0)
        finalresult = resulttf.numpy()
        print("result:",finalresult)
        
        red = 0
        yellow = 0
        green = 0

        if(finalresult == 0):
          red = 1
        elif(finalresult == 1):
          yellow = 1
        elif(finalresult == 2):
          green = 1

        
        finalresult = finalresult + 1

        

        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('main.html',
                                      upper = u,
                                      lower = l,
                                      num = n,
                                      sym = s,
                                      red = red,
                                      yellow = yellow,
                                      green = green,
                                      time = pico,
                                      unit = ax[i],
                                      count = count,
                                      word = longword,
                                      result = finalresult,
                                     )

if __name__ == '__main__':
    app.run()