#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/MichaelGrupp/evo/blob/master/contrib/multiply_timestamps.py

from evo.tools import file_interface

DESC = """multiply the timestamps of a TUM trajectory file by a factor"""

def main(traj_file_ref, traj_file_to_correct):
    traj_ref = file_interface.read_tum_trajectory_file(traj_file_ref)
    traj_to_correct = file_interface.read_tum_trajectory_file(traj_file_to_correct)
    timestamp_ratio = traj_to_correct.timestamps[0]/traj_ref.timestamps[0]
    factor = round(timestamp_ratio, -len(str(int(timestamp_ratio)))+1)

    print(factor)

    traj_to_correct.timestamps = traj_to_correct.timestamps / factor
    file_interface.write_tum_trajectory_file(traj_file_to_correct, traj_to_correct)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument("traj_file_ref", help="trajectory in TUM format")
    parser.add_argument("traj_file_to_correct", help="trajectory in TUM format")
    args = parser.parse_args()
    main(args.traj_file_ref, args.traj_file_to_correct)