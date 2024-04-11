
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
        goleador:un unico elemento de tipo diccionario que representa al goleador
    """
    goleador=max(players_stats, key=lambda x: x['goals'])
    return goleador

def most_influential(players_stats):
    """ Encuentra al jugador más influyente, multiplicando sus estadisticas utilizando una tabla de valores dada. 

    Args:
        player_stats: parametro de tipo lista, la cual contiene diccionarios. Debe contener la clave goals, goals_avoided y assist

    Returns: 
        player: un unico elemento de tipo diccionario que representa al jugador más influyente.
    """
    player= max(players_stats, key=lambda x: x["goals"]*1.5 + x["goals_avoided"]*1.25 + x["assist"])
    return player

def get_promedio(players_stats):
    """ Calcula el promedio de los goles del equipo.

    Args:
        player_stats: parametro de tipo lista, la cual contiene diccionarios. Debe contener la clave goals.
    
    Returns:
        total_goals/25: Devuelve un elemento de tipo float.
    """
    total_goals= sum(player["goals"] for player in players_stats)
    return total_goals/25