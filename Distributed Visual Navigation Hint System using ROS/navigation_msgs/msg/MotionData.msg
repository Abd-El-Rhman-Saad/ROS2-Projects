# navigation_msgs/msg/MotionData.msg

std_msgs/Header header

float32 avg_dx            # Average horizontal displacement (pixels)
float32 avg_dy            # Average vertical displacement (pixels)
float32[] displacements_x # Per-ROI horizontal displacements
float32[] displacements_y # Per-ROI vertical displacements
int32 num_matches         # Number of ROIs used for motion estimation
float32 confidence        # 0.0 = unreliable, 1.0 = highly reliable
