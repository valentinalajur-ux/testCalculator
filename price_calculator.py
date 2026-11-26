class PriceCalculator:
    def calculate(self, age: int) -> int:
        if age < 0:
            raise ValueError("Åldern kan inte vara negativ.")

        if age < 13:
            return 50

        if age < 65:
            return 100



        return 80