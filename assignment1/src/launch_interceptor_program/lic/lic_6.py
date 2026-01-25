from ..model import Parameters, Points
from .geometry import distance_between_points, distance_between_point_and_line

def lic_6(parameters: Parameters, points: Points):
    NUMPOINTS = len(points)
    N_PTS = parameters.N_PTS
    DIST = parameters.DIST
   
    if (NUMPOINTS < 3 or DIST < 0 or N_PTS < 3 or N_PTS > NUMPOINTS):
        return False
    
    for start_index in range(0, (NUMPOINTS - N_PTS) + 1): 
        current_set = [] 
        for i in range(start_index, start_index + N_PTS): 
            current_set.append(points[i])
        if (current_set[0] == current_set[N_PTS - 1]):
            for current_point in range(1, N_PTS - 1):
                calculated_distance = distance_between_points(current_set[0], current_set[current_point])
                if (DIST < calculated_distance):
                    return True
        else:
            for current_point in range(1, N_PTS - 1):
                calculated_distance = distance_between_point_and_line(current_set[current_point], current_set[0], current_set[N_PTS-1])
                if (DIST < calculated_distance):
                    return True
    return False

                



