#hangman
#make a diagram of the game/problem. flow chart programming

import random

word_list=["aardvark", "baboon", "camel"]

word_chosen=random.choice(word_list)
print(f"Chosen word is {word_chosen}") # Hata ayıklama için kelimeyi göster

# 1. Başlangıçta kelimenin her harfi yerine alt çizgi göster
display = []
for _ in range(len(word_chosen)):
    display.append("_")

print(" ".join(display)) # Listeyi aralarında boşluk bırakarak yazdır

game_over = False
lives = 6 # Oyuncunun kaç canı olduğunu burada belirleyebiliriz (örneğin 6 can)

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Eğer oyuncu zaten bu harfi tahmin etmişse
    if guess in display:
        print(f"You've already guessed {guess}. Try another letter.")
        continue # Bir sonraki döngüye geç

    # Tahmin edilen harfi kelimede ara ve display'i güncelle
    found_letter_in_word = False
    for position in range(len(word_chosen)):
        letter = word_chosen[position]
        if letter == guess:
            display[position] = guess # Doğru pozisyona harfi yerleştir
            found_letter_in_word = True
    
    # Eğer harf kelimede yoksa canı azalt
    if not found_letter_in_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(f"You have {lives} lives remaining.")
        if lives == 0:
            game_over = True
            print("You lose! The word was:", word_chosen)

    print(" ".join(display)) # Güncellenmiş display'i yazdır

    # Oyun kazanma kontrolü
    if "_" not in display: # Eğer display'de hiç alt çizgi kalmadıysa, tüm harfler bulunmuştur.
        game_over = True
        print("You win! Congratulations!")
