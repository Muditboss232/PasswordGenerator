import random
print("Hello! I am a PASSWORD GENERATOR")
catchy= input("What is a catchy phrase: ")
alphabet = "-a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-"
cptalphabet = "-A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-WX-Y-Z-"
password2 = ''
password2 += random.choice(cptalphabet)
number = "123456789"
password1 = ''
password1 += random.choice(number)
password = ''
password += random.choice(alphabet)
print(password,password2,password,password2,catchy,password1,password1)