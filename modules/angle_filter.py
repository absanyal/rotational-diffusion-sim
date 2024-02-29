
def angle_filter(theta, theta_min, theta_max):
    theta_range = theta_max - theta_min
    if theta < theta_min:
        return angle_filter(theta + theta_range, theta_min, theta_max)
    elif theta > theta_max:
        return angle_filter(theta - theta_range, theta_min, theta_max)
    else:
        return theta