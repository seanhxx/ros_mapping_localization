#!/usr/bin/env python3
import os
import subprocess


def main():
    PKG_SRC_DIR = os.path.abspath(os.path.join(__file__, os.pardir))
    MAP_OUTPUT_DIR = os.path.abspath(os.path.join(PKG_SRC_DIR, os.pardir, 'maps'))
    if not os.path.exists(MAP_OUTPUT_DIR):
        os.makedirs(MAP_OUTPUT_DIR)

    player_proc = subprocess.Popen(['rosbag', 'play', '--clock', 'mapping.bag'], cwd=PKG_SRC_DIR)
    player_proc.wait()
    print("Finished playing bag file")
    map_proc = subprocess.Popen(['rosrun', 'map_server', 'map_saver', '-f', 'record_map'], cwd=MAP_OUTPUT_DIR)
    map_proc.wait()
    print(f"Finished saving map to {MAP_OUTPUT_DIR}/{'record_map'}.pgm and {MAP_OUTPUT_DIR}/{'record_map'}.yaml")


if __name__ == '__main__':
    main()
