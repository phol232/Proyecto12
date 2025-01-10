
class PrimeCounter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def count_primes(self):
        prime_count = 0
        for number in range(self.start, self.end + 1):
            if self.is_prime(number):
                prime_count += 1
        return prime_count

# Ejemplo de uso
start = int(input("Ingresa el inicio del rango: "))
end = int(input("Ingresa el final del rango: "))
counter = PrimeCounter(start, end)
print(f"Cantidad de números primos en el rango {start} a {end}: {counter.count_primes()}")
