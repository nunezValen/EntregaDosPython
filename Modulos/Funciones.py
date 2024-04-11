
def generate_player_stats(names,goals,goals_avoided,assist):
    """ Genera una lista de diccionarios con las estadisticas de los jugadores.

      Args:
         names: Lista con nombre de jugadores
        goals: Una lista con la cantidad de goles de cada jugador
         goals_avoided: Una lista con la cantidad de goles evitados por jugador
         assist: Una lista con la cantidad de goles asistidos por jugador

      Returns:
         return: tipo diccionario """
    
    player_stats=[]
    for i in range(len(names)):
        player={"name": names[i],"goals": goals[i],"goals_avoided": goals_avoided[i], "assist": assist[i]}
        player_stats.append(player)
    return player_stats


def find_goleador (players_stats):
    """ Encuentra en la lista de diccionarios al jugador con mayor cantidad de goles.

    Args:
        players_stats: parametro de tipo lista, la cual contiene diccionarios. Debe contener la clave goals.
    Returns: 
        dict:un unico elemento de tipo diccionario que representa al goleador
    """
    goleador=max(players_stats, key=lambda x: x['goals'])
    return goleador
