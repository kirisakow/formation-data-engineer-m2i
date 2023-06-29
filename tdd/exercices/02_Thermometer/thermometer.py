def get_temp_closest_to_0(temperatures: list) -> int | float:
    closest_to_0 = 0
    liste_vide = not temperatures
    if not liste_vide:
        if len(temperatures) > 10000:
            raise ValueError('Trop de paramètres')
        positive_int_closest_to_0 = sorted([abs(t) for t in temperatures])[0]
        if -positive_int_closest_to_0 in temperatures:
            closest_to_0 = -positive_int_closest_to_0
        if positive_int_closest_to_0 in temperatures:
            closest_to_0 = positive_int_closest_to_0
    return closest_to_0
