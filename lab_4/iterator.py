from collections.abc import Iterable, Iterator

class Section:
    title: str
    children: tuple[Section, ...] = ()

class CourseIterator(Iterator[Section]):
    def __init__(self, root: Section) -> None:
        self._stack = [root]

    def __iter__(self) -> "CourseIterator":
        return self

    def __next__(self) -> Section:
        if not self._stack:
            raise StopIteration

        section = self._stack.pop()
        self._stack.extend(reversed(section.children))
        return section

class Course(Iterable[Section]):
    def __init__(self, root: Section) -> None:
        self._root = root

    def __iter__(self) -> CourseIterator:
        return CourseIterator(self._root)

def create_example_course() -> Course:
    root = Section(
        "Курс Python",
        (
            Section("Основы", (Section("Переменные"), Section("Функции"))),
            Section("ООП", (Section("Классы"), Section("Паттерны"))),
        ),
    )
    return Course(root)

def main() -> None:
    course = create_example_course()
    for section in course:
        print(f"- {section.title}")


if __name__ == "__main__":
    main()
