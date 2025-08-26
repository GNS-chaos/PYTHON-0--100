def greet():
    print("YO")
greet()

#def function(somethin):

def greet_with_name(name, location):
    print(f"hello {name}")
    print(f"what is it like in {location}")
greet_with_name("bem", "ankara")

#positional arguments^^
#keyword assoiaon da yer öemli değil, name=x diye belirtiyorsun


        
def calculate_love_score(girl, boy):
    girl=input("woman's name: ").lower()
    boy=input("man's name: ").lower()
    name=girl+boy
    t=0
    r=0
    u=0
    e=0
    l=0
    o=0
    v=0
    
    for letter in name:
        if letter=="t":
            t+=1 
        elif letter=="r":
            r+=1 
        elif letter== "u":
            u+=1 
        elif letter=="e":
            e+=1 
    print(f"T occurs {t} times\n R occurs {r} times\n U occurs {u} times\n E occurs {e} times \n Total = {t+r+u+e}")
    
    
    for letter in name:
        if letter=="l":
            l+=1 
        elif letter=="o":
            o+=1 
        elif letter== "v":
            v+=1 
    print(f"L occurs {l} times\n O occurs {o} times\n V occurs {v} times\n E occurs {e} times \n Total = {l+o+v+e}")
    
    print(f"Love score = {t+r+u+e}{l+o+v+e}")
    
calculate_love_score("Angela Yu", "Jack Bauer")

#caesar cipher
import string # string.ascii_lowercase kullanmak daha iyi bir pratiktir

# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet = list(string.ascii_lowercase) # Alfabe listesini dinamik oluşturma
def caesar(original_text, shift_amount, encode_or_decode):
    caesar_text = ""
    
    # Şifre çözme işlemi için kaydırma miktarını negatif yap
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter in alphabet: # Harfin alfabede olup olmadığını kontrol et
            position = alphabet.index(letter)
            # Yeni pozisyonu hesapla ve alfabenin sınırları içinde tutmak için modül operatörünü kullan
            shifted_position = (position + shift_amount) % len(alphabet)
            
            # Yeni harfi al ve şifreli/çözülmüş metne ekle
            caesar_text += alphabet[shifted_position]
        else:
            # Alfabe dışındaki karakterleri olduğu gibi ekle (boşluk, noktalama, sayı vb.)
            caesar_text += letter
            
    print(f"Here's the {encode_or_decode}d result: {caesar_text}")

# Oyunun başlangıçta çalışmasını sağlayın ve döngüyü kontrol edin
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift=int(input("Type the shift number: \n"))

    # Caesar fonksiyonunu doğru değişken isimleriyle çağırın
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Kullanıcıya tekrar oynamak isteyip istemediğini sorun ve döngü bayrağını güncelleyin
    cont_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if cont_input == "no":
        should_continue = False # Eğer 'no' girilirse döngüyü sonlandır
        print("goodbye")

