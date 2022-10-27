import pygame
from math import sin, cos, radians, pi

pygame.init()


class Line:
    def __init__(self, pos: pygame.Vector2, length: float, degree: float = 0) -> None:
        self.degree = degree
        self.radian = radians(degree)
        self.length = length
        self.pos1 = pos
        self.pos2 = pygame.Vector2(
            self.length * cos(self.radian) + self.pos1.x,
            self.length * sin(self.radian) + self.pos1.y,
        )

    def draw(self, screen):
        pygame.draw.aaline(screen, pygame.Color("green"), self.pos1, self.pos2)


def a(line: Line, length: float, degree: float):
    return Line(line.pos2, length, line.degree + degree)


def s(line: Line, length: float, degree: float):
    return Line(line.pos2, length, line.degree - degree)


def iter(lines: list[Line], line: Line):
    """F+F--F+F"""
    lines.remove(line)
    length = line.length / 3
    l1 = Line(line.pos1, length, line.degree)
    l2 = Line(l1.pos2, length, line.degree + 60)
    l3 = Line(l2.pos2, length, l2.degree - 120)
    l4 = Line(l3.pos2, length, l3.degree + 60)
    lines.extend((l1, l2, l3, l4))


def setup():
    lines: list[Line] = [Line(pygame.Vector2(480, 800), 900, 0)]
    lines.append(s(lines[0], lines[0].length, 120))
    lines.append(s(lines[1], lines[1].length, 120))
    return lines


def main():
    pygame.display.set_caption("Snowflake")
    screen = pygame.display.set_mode((1920, 1080))
    running = True

    lines = setup()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL]:
                running = False
            if keys[pygame.K_LSHIFT]:
                lines = setup()
            if keys[pygame.K_SPACE]:
                # for _ in range(len(lines)): (if you want to see it stage by stage)
                iter(lines, lines[0]) # you could also use a for loop of arbitrary loops

        screen.fill((0, 0, 0))

        for l in lines:
            l.draw(screen)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
