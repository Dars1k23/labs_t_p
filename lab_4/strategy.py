from abc import ABC, abstractmethod

class DeliveryStrategy(ABC):

    @abstractmethod
    def calculate(self, weight_kg: int) -> int:
        raise NotImplementedError


class StandardDelivery(DeliveryStrategy):
    def calculate(self, weight_kg: int) -> int:
        return 200 + 50 * weight_kg


class ExpressDelivery(DeliveryStrategy):
    def calculate(self, weight_kg: int) -> int:
        return 500 + 120 * weight_kg


class Pickup(DeliveryStrategy):
    def calculate(self, weight_kg: int) -> int:
        return 0


class DeliveryCalculator:
    def __init__(self, strategy: DeliveryStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: DeliveryStrategy) -> None:
        self._strategy = strategy

    def calculate(self, weight_kg: int) -> int:
        if weight_kg <= 0:
            raise ValueError("Вес посылки должен быть положительным.")
        return self._strategy.calculate(weight_kg)


def main() -> None:
    weight_kg = 3
    calculator = DeliveryCalculator(StandardDelivery())
    print(f"Посылка: {weight_kg} кг")
    print(f"Обычная доставка: {calculator.calculate(weight_kg)} руб.")

    calculator.set_strategy(ExpressDelivery())
    print(f"Экспресс-доставка: {calculator.calculate(weight_kg)} руб.")

    calculator.set_strategy(Pickup())
    print(f"Самовывоз: {calculator.calculate(weight_kg)} руб.")


if __name__ == "__main__":
    main()
