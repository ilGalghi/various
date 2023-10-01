import random
import statistics

def genera_numeri_casuali(n):
    numeri_casuali = [random.randint(1, 100) for _ in range(n)]
    return numeri_casuali

def calcola_media(numeri):
    somma = sum(numeri)
    media = somma / len(numeri)
    return media

def calcola_deviazione_standard(numeri):
    deviazione_std = statistics.stdev(numeri)
    return deviazione_std

def main():
    numero_di_elementi = 20
    numeri_casuali = genera_numeri_casuali(numero_di_elementi)
    
    print(f"Numeri casuali generati: {numeri_casuali}")
    
    media = calcola_media(numeri_casuali)
    print(f"Media dei numeri generati: {media}")
    
    deviazione_std = calcola_deviazione_standard(numeri_casuali)
    print(f"Deviazione standard dei numeri generati: {deviazione_std}")
    
    numeri_ordinati = sorted(numeri_casuali)
    print(f"Numeri generati ordinati: {numeri_ordinati}")

if __name__ == "__main__":
    main()
