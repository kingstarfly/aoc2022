from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, List, Literal, Tuple, TypeAlias

here = Path(__file__).parent

Coord: TypeAlias = Tuple[int, int]  # Coordinate class
CoordMap: TypeAlias = DefaultDict[Coord, int]
CoordUpdate: TypeAlias = Literal[-1, 0, 1]


def signum(i: int) -> int:
    return i // abs(i) if i != 0 else 0


def coords_touching(c1: Coord, c2: Coord) -> bool:
    return max(abs(c1[0] - c2[0]), abs(c1[1] - c2[1])) <= 1  # Touching iff L-inf distance <= 1


def update_head(start: Coord, update_x: CoordUpdate, update_y: CoordUpdate) -> Coord:
    return (start[0] + update_x, start[1] + update_y)


def update_tail(new_H: Coord, T: Coord) -> Coord:
    if coords_touching(new_H, T):  # When touching after H moves, do nothing
        return (T[0], T[1])
    else:  # Need to move T diagonally
        return (T[0] + signum(new_H[0] - T[0]), T[1] + signum(new_H[1] - T[1]))


def propogate_motion(coords: List[Coord], head_x: CoordUpdate, head_y: CoordUpdate) -> List[Coord]:
    coords[0] = update_head(coords[0], head_x, head_y)
    for k in range(1, len(coords)):
        coords[k] = update_tail(coords[k - 1], coords[k])
    return coords


def simulate_motion(head_motions: List[str], num_knots: int = 2) -> CoordMap:
    coord_map_tail: CoordMap = defaultdict(int)
    cur_coords: List[Coord] = [(0, 0)] * num_knots
    coord_map_tail[(0, 0)] += 1
    for motion in head_motions:
        match motion.split():
            case ["R", steps]:
                for _ in range(int(steps)):
                    cur_coords = propogate_motion(cur_coords, 1, 0)
                    coord_map_tail[cur_coords[-1]] += 1
            case ["L", steps]:
                for _ in range(int(steps)):
                    cur_coords = propogate_motion(cur_coords, -1, 0)
                    coord_map_tail[cur_coords[-1]] += 1
            case ["U", steps]:
                for _ in range(int(steps)):
                    cur_coords = propogate_motion(cur_coords, 0, 1)
                    coord_map_tail[cur_coords[-1]] += 1
            case ["D", steps]:
                for _ in range(int(steps)):
                    cur_coords = propogate_motion(cur_coords, 0, -1)
                    coord_map_tail[cur_coords[-1]] += 1
    return coord_map_tail

motions = open(here / "input.txt").read().split("\n")
print("Part 1: ", len(simulate_motion(motions)))
print("Part 2: ", len(simulate_motion(motions, num_knots=10)))