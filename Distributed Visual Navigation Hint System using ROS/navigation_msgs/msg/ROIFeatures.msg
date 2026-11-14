# ROI Features message
uint32 num_rois
uint32[] roi_ids          # ROI index (0..N-1)
float32[] centroids_x     # x coordinate of ROI centroid
float32[] centroids_y     # y coordinate
float32[] mean_hue        # average hue in ROI
float32[] mean_saturation # average saturation
float32[] mean_value      # average value (brightness)
float32[] keypoint_count  # number of keypoints detected in ROI
# Optional: bounding boxes (x, y, width, height)
float32[] bbox_x
float32[] bbox_y
float32[] bbox_w
float32[] bbox_h
