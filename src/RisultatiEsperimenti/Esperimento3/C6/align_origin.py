import matplotlib.pyplot as plt
import numpy as np
from quaternion import Quat

class Pose:
    def __init__(self, time, x, y, z, qx, qy, qz, qw):
        self.time = time
        self.x = x
        self.y = y
        self.z = z
        self.qx = qx
        self.qy = qy
        self.qz = qz
        self.qw = qw
    
    def __str__(self):
        return f"{self.time} {self.x} {self.y} {self.z} {self.qx} {self.qy} {self.qz} {self.qw}"

def read_poses_from_file(filename):
    pose_list = []
    with open(filename, 'r') as file:
        righe = file.readlines()

        for riga in righe:
            [timestamp, x, y, z, qx, qy, qz, qw] = riga.split()
            p = Pose(float(timestamp), float(x), float(y), float(z), float(qx), float(qy), float(qz), float(qw))
            pose_list.append(p)
    return pose_list

def get_axix_relative_orientation(pose1, pose2):
    q1 = Quat(attitude=[pose1.qx, pose1.qy, pose1.qz, pose1.qw])
    q2 = Quat(attitude=[pose2.qx, pose2.qy, pose2.qz, pose2.qw])
    return q1*q2.inv()

def align_axix(poses1, poses2):
    pose1 = poses1[0]
    pose2 = poses2[0]
    relative_orientation = get_axix_relative_orientation(pose1, pose2)

    print(relative_orientation)

    for pose in poses2:
        q2 = Quat(attitude=[pose.qx, pose.qy, pose.qz, pose.qw])
        newq = relative_orientation*q2
        pose.qx = -newq.q[0]
        pose.qy = -newq.q[1]
        pose.qz = -newq.q[2]
        pose.qw = -newq.q[3]

def get_traslation(pose1, pose2):
    return [pose1.x-pose2.x, pose1.y-pose2.y, pose1.z-pose2.z]

def align_origin(poses1, poses2):
    pose1 = poses1[0]
    pose2 = poses2[0]
    traslation = get_traslation(pose1, pose2)
    for pose in poses2:
        pose.x += traslation[0]
        pose.y += traslation[1]
        pose.z += traslation[2]

def write_poses_to_file(filename, poses):
    with open(filename, 'w') as file:
        for pose in poses:
            file.write(str(pose)+"\n")

def main(ref_traj, traj_to_align):
    GT_filename = ref_traj
    ORB_filename = traj_to_align

    GT_poses = read_poses_from_file(GT_filename)
    ORB_poses = read_poses_from_file(ORB_filename)

    align_axix(GT_poses, ORB_poses)
    align_origin(GT_poses, ORB_poses)

    write_poses_to_file("aligned_"+traj_to_align, ORB_poses)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("ref_traj", help="ref trajectory in TUM format")
    parser.add_argument("traj_to_align", help="trajectory to be aligned")
    args = parser.parse_args()
    main(args.ref_traj, args.traj_to_align)