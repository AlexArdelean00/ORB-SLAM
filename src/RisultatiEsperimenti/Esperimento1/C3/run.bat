mkdir "2. correct_timestamp_data"

copy "1. origin_data\Exp1_GT.txt" "2. correct_timestamp_data\Exp1_GT.txt"

copy "1. origin_data\Exp2_GT.txt" "2. correct_timestamp_data\Exp2_GT.txt"

copy "1. origin_data\Exp1_ORB.txt" "2. correct_timestamp_data\Exp1_ORB.txt"

copy "1. origin_data\Exp2_ORB.txt" "2. correct_timestamp_data\Exp2_ORB.txt"

python .\timestamp_correction.py "2. correct_timestamp_data\Exp1_GT.txt" "2. correct_timestamp_data\Exp1_ORB.txt"

python .\timestamp_correction.py "2. correct_timestamp_data\Exp2_GT.txt" "2. correct_timestamp_data\Exp2_ORB.txt"



mkdir "3. scaled_rotated_and_translated_data"

copy "2. correct_timestamp_data\Exp1_GT.txt" "3. scaled_rotated_and_translated_data\Exp1_GT.txt"

copy "2. correct_timestamp_data\Exp2_GT.txt" "3. scaled_rotated_and_translated_data\Exp2_GT.txt"

copy "2. correct_timestamp_data\Exp1_ORB.txt" "3. scaled_rotated_and_translated_data\Exp1_ORB.txt"

copy "2. correct_timestamp_data\Exp2_ORB.txt" "3. scaled_rotated_and_translated_data\Exp2_ORB.txt"

cd "3. scaled_rotated_and_translated_data"

evo_traj tum --ref "Exp1_GT.txt" "Exp1_ORB.txt" --align --correct_scale --save_as_tum

evo_traj tum --ref "Exp2_GT.txt" "Exp2_ORB.txt" --align --correct_scale --save_as_tum

evo_traj tum "Exp1_GT.tum" "Exp1_ORB.tum" --plot --plot_mode xy --ros_map_yaml "../map_gt/corridorB.yaml"

evo_traj tum "Exp2_GT.tum" "Exp2_ORB.tum" --plot --plot_mode xy --ros_map_yaml "../map_gt/corridorB.yaml"

cd ..



mkdir "4. aligned_origin_data"

copy "3. scaled_rotated_and_translated_data\Exp1_GT.tum" "4. aligned_origin_data\Exp1_GT.tum"

copy "3. scaled_rotated_and_translated_data\Exp2_GT.tum" "4. aligned_origin_data\Exp2_GT.tum"

copy "3. scaled_rotated_and_translated_data\Exp1_ORB.tum" "4. aligned_origin_data\Exp1_ORB.tum"

copy "3. scaled_rotated_and_translated_data\Exp2_ORB.tum" "4. aligned_origin_data\Exp2_ORB.tum"

cd "4. aligned_origin_data"

python "../align_origin.py" "Exp1_GT.tum" "Exp1_ORB.tum"

python "../align_origin.py" "Exp2_GT.tum" "Exp2_ORB.tum"

evo_traj tum "Exp1_GT.tum" "aligned_Exp1_ORB.tum" --plot --plot_mode xy --ros_map_yaml "../map_gt/corridorB.yaml"

evo_traj tum "Exp2_GT.tum" "aligned_Exp2_ORB.tum" --plot --plot_mode xy --ros_map_yaml "../map_gt/corridorB.yaml"

cd ..



mkdir "5. results"

copy "4. aligned_origin_data\Exp1_GT.tum" "5. results\Exp1_GT.tum"

copy "4. aligned_origin_data\Exp2_GT.tum" "5. results\Exp2_GT.tum"

copy "4. aligned_origin_data\aligned_Exp1_ORB.tum" "5. results\aligned_Exp1_ORB.tum"

copy "4. aligned_origin_data\aligned_Exp2_ORB.tum" "5. results\aligned_Exp2_ORB.tum"

cd "5. results"

evo_ape tum .\Exp1_GT.tum .\aligned_Exp1_ORB.tum --plot --plot_mode xy --save_results ape_results_Exp1.zip

evo_rpe tum .\Exp1_GT.tum .\aligned_Exp1_ORB.tum --plot --plot_mode xy --save_results rpe_results_Exp1.zip

evo_ape tum .\Exp2_GT.tum .\aligned_Exp2_ORB.tum --plot --plot_mode xy --save_results ape_results_Exp2.zip

evo_rpe tum .\Exp2_GT.tum .\aligned_Exp2_ORB.tum --plot --plot_mode xy --save_results rpe_results_Exp2.zip

mkdir "tables"

cd "tables"

evo_res "..\ape_results_Exp1.zip" -p --save_table ape_results_table_Exp1.csv

evo_res "..\rpe_results_Exp1.zip" -p --save_table rpe_results_table_Exp1.csv

evo_res "..\ape_results_Exp2.zip" -p --save_table ape_results_table_Exp2.csv

evo_res "..\rpe_results_Exp2.zip" -p --save_table rpe_results_table_Exp2.csv