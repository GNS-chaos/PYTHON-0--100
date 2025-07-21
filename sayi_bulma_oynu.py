import random

def game_starts():
    basamak = int(input("Kaç basamaklı tahmin oyunu oynayalım: "))

    # Benzersiz rakamlardan oluşan sayı üret
    rakamlar = list(range(10))
    random.shuffle(rakamlar)
    computer_number = rakamlar[:basamak]

    #print(f"(DEBUG - bilgisayarın sayısı: {computer_number})")  # test için

    while True:
        guess = input("Tahminin (sadece rakamlar, boşluksuz): ")

        if len(guess) != basamak or not guess.isdigit():
            print(f"Lütfen {basamak} basamaklı sadece rakamlardan oluşan bir sayı gir.")
            continue

        guess_digits = [int(x) for x in guess]

        dogru_yer = 0
        yanlis_yer = 0

        for i, digit in enumerate(guess_digits):
            if digit == computer_number[i]:
                dogru_yer += 1
            elif digit in computer_number:
                yanlis_yer += 1

        print(f"Doğru yerde: {dogru_yer}, yanlış yerde ama içinde olan: {yanlis_yer}")

        if guess_digits == computer_number:
            print("Tam 12'den vurdun, tebrikler!")
            again = input("Tekrar oynamak ister misin? (devam / tamam): ")
            if again.lower() == "devam":
                print("\n"*25)
                return game_starts()
            else:
                print("Güzel oyundu :)")
                break
# Oyunu başlat
game_starts()


