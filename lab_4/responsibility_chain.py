from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class ExpenseRequest:
    purpose: str
    amount: int

    def __post_init__(self) -> None:
        if self.amount <= 0:
            raise ValueError("Сумма заявки должна быть положительной.")

class Approver(ABC):
    def __init__(self) -> None:
        self._next: Approver | None = None

    def set_next(self, approver: Approver) -> Approver:
        self._next = approver
        return approver

    def handle(self, request: ExpenseRequest) -> str | None:
        result = self.try_approve(request)
        if result is not None:
            return result
        if self._next is not None:
            return self._next.handle(request)
        return None

    @abstractmethod
    def try_approve(self, request: ExpenseRequest) -> str | None:
        raise NotImplementedError

class TeamLead(Approver):
    def try_approve(self, request: ExpenseRequest) -> str | None:
        if request.amount <= 10_000:
            return "Руководитель команды"
        return None

class DepartmentHead(Approver):
    def try_approve(self, request: ExpenseRequest) -> str | None:
        if request.amount <= 50_000:
            return "Начальник отдела"
        return None


class Director(Approver):
    def try_approve(self, request: ExpenseRequest) -> str | None:
        if request.amount <= 200_000:
            return "Директор"
        return None


def create_approval_chain() -> Approver:
    team_lead = TeamLead()
    team_lead.set_next(DepartmentHead()).set_next(Director())
    return team_lead


def main() -> None:
    chain = create_approval_chain()
    requests = (
        ExpenseRequest("Клавиатуры", 5_000),
        ExpenseRequest("Мониторы", 30_000),
        ExpenseRequest("Оснащение лаборатории", 120_000),
        ExpenseRequest("Сервер", 300_000),
    )
    for request in requests:
        approver = chain.handle(request)
        result = approver if approver is not None else "Никто: лимиты превышены"
        print(f"{request.purpose} ({request.amount} руб.) -> {result}")


if __name__ == "__main__":
    main()
