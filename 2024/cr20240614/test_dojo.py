"""
Guiding test vs test den wir recyclen?
* Guiding test ist gut aber verlangt viel auf einmal
* Alte Tests sollten stehen bleiben können wie sie sind
Wann testen wir zu viel?

Approval Schritt forciert Kontextwechsel und das ist hilfreich, wir
sehen nur mehr die Daten und nicht mehr den Code
Es gibt eine kleine Pause

TODO
Problem mit der Darstellung: Koordinaten/Gitter falsch?
Alle Animationen in einem Fenster?
"""


from approvaltests import verify_as_json, verify
import attrs
import cattrs
import pytest

@attrs.define
class Coordinate:
    x: int
    y: int

@attrs.define
class Square:
    coordinate: Coordinate
    color: int = 1


@attrs.define
class Ant:
    coordinate: Coordinate = Coordinate(0, 0)
    orientation: int = 0

    def turn_right_and_move(self):
        moved_coordinate = Coordinate(1, 0) if self.orientation == 0 else Coordinate(0, 1)
        moved_orientation = self.orientation-90
        return Ant(moved_coordinate, orientation=moved_orientation)

    def turn_left_and_move(self):
        moved_coordinate = Coordinate(-1, 0)
        moved_orientation = self.orientation+90
        return Ant(moved_coordinate, orientation=moved_orientation)

    def move(self, color):
        if color == 0:
            moved_ant = self.turn_right_and_move()
        else:
            moved_ant = self.turn_left_and_move()
        return moved_ant


@attrs.define
class State:
    squares: list[Square]
    ant: Ant = Ant()

    def transform(self):
        ant_is_on_white_square = True
        for square in self.squares:
            if square.coordinate == self.ant.coordinate:
                ant_is_on_white_square = square.color == 0
                break

        if ant_is_on_white_square:
            color_at_ant = 0
            squares = self.squares + [Square(self.ant.coordinate, color=1)]
        else:
            color_at_ant = 1
            squares = []

        moved_ant = self.ant.move(color_at_ant)
        return State(squares=squares, ant=moved_ant)


@attrs.define
class Config:
    title: str
    figsize: int = 5
    gridsize: int = 5


def test_simulation_with_one_square():

    config = Config("Simulation")
    config_unstructured = cattrs.unstructure(config)

    coordinate = Coordinate(0, 0)
    square = Square(coordinate)
    state = State([square])

    state_unstructured = cattrs.unstructure(state)

    simulation_data = {
        "config": config_unstructured,
        "states": [
            state_unstructured
        ],
    }

    verify_as_json(simulation_data)


def test_simulation_with_ant():

    config = Config("Simulation")
    config_unstructured = cattrs.unstructure(config)

    coordinate = Coordinate(0, 0)
    ant = Ant(coordinate, orientation=0)
    states = [State(squares=[], ant=ant)]
    states_unstructured = cattrs.unstructure(states)

    simulation_data = {
        "config": config_unstructured,
        "states": states_unstructured,
    }

    verify_as_json(simulation_data)


def test_simulation_with_moving_ant():

    config = Config("Simulation")
    config_unstructured = cattrs.unstructure(config)

    starting_position = Coordinate(0, 0)
    state_initial = State(squares=[], ant=Ant(starting_position, orientation=0))

    state_transformed = state_initial.transform()

    states = [
        state_initial,
        state_transformed
    ]
    states_unstructured = cattrs.unstructure(states)

    simulation_data = {
        "config": config_unstructured,
        "states": states_unstructured,
    }

    verify_as_json(simulation_data)

def test_simulation_with_ant_facing_left():

    config = Config("Simulation")
    config_unstructured = cattrs.unstructure(config)

    starting_position = Coordinate(0, 0)
    state_initial = State(squares=[], ant=Ant(starting_position, orientation=90))

    state_transformed = state_initial.transform()

    states = [
        state_initial,
        state_transformed
    ]
    states_unstructured = cattrs.unstructure(states)

    simulation_data = {
        "config": config_unstructured,
        "states": states_unstructured,
    }

    verify_as_json(simulation_data)


def test_simulation_with_ant_starts_from_colored_square():

    config = Config("Simulation")
    config_unstructured = cattrs.unstructure(config)

    starting_position = Coordinate(0, 0)
    state_initial = State(squares=[Square(starting_position, color=1)], ant=Ant(starting_position, orientation=0))

    state_transformed = state_initial.transform()

    states = [
        state_initial,
        state_transformed
    ]
    states_unstructured = cattrs.unstructure(states)

    simulation_data = {
        "config": config_unstructured,
        "states": states_unstructured,
    }

    verify_as_json(simulation_data)


def test_simulation_with_ant_starts_from_white_square_next_to_colored_square():

    config = Config("Simulation")
    config_unstructured = cattrs.unstructure(config)

    starting_position = Coordinate(0, 0)
    state_initial = State(squares=[Square(Coordinate(1, 1), color=1)], ant=Ant(starting_position, orientation=0))

    state_transformed = state_initial.transform()

    states = [
        state_initial,
        state_transformed
    ]
    states_unstructured = cattrs.unstructure(states)

    simulation_data = {
        "config": config_unstructured,
        "states": states_unstructured,
    }

    verify_as_json(simulation_data)