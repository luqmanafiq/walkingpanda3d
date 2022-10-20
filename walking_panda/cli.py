from . import panda

import argparse

def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate",help="Suppress Rotation",
                        action="store_true")
    parser.add_argument("--scale=1",help="Suppress Scale",
                        action="store_true")
    parser.add_argument("--playsound",help="Suppress Sound",
                        action="store_true")
    parser.add_argument("--moonwalk", help="Suppress Walking",
                        action="store_true")
    parser.add_argument("--spin", help="Suppress Spinning",
                        action="store_true")
    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()