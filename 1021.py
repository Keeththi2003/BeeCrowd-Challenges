N = float(input()) * 100  # Convert input to cents
notes = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]  # Values in cents

print("NOTAS:")
for note in notes[:6]:
    M = int(N)
    numbers = M // note
    print(f"{numbers} nota(s) de R$ {(note / 100):.2f}")
    N %= note

print("MOEDAS:")
for coin in notes[6:]:
    numbers_2 = int(N // coin)
    print(f"{numbers_2} moeda(s) de R$ {(coin / 100):.2f}")
    N %= coin