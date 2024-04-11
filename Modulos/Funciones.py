def generate_player_stats(names,goals,goals_avoided,assist):
    """ Genera una lista de diccionarios con las estadisticas de los jugadores.

      Args:
         names(list): Lista con nombre de jugadores
         goals(list): Una lista con la cantidad de goles de cada jugador.
         goals_avoided(list): Una lista con la cantidad de goles evitados por jugador.
         assist(list): Una lista con la cantidad de goles asistidos por jugador.

      Returns:
         List: Lista de diccionarios con las estadisticas de cada uno de los jugadores. """
    
    player_stats=[]
    for i in range(len(names)):
        player={"name": names[i],"goals": goals[i],"goals_avoided": goals_avoided[i], "assist": assist[i]}
        player_stats.append(player)
    return player_stats


def find_goleador (players_stats):
    """ Encuentra en la lista de diccionarios al jugador con mayor cantidad de goles.

    Args:
        players_stats(list): Lista, la cual contiene diccionarios. Debe contener la clave goals.
    Returns: 
        goleador(dict): Diccionario que representa al goleador.
    """
    goleador=max(players_stats, key=lambda x: x['goals'])
    return goleador

def most_influential(players_stats):
    """ Encuentra al jugador más influyente, multiplicando sus estadisticas utilizando una tabla de valores dada. 

    Args:
        players_stats(list): Lista, la cual contiene diccionarios. Debe contener la clave goals, goals_avoided y assist.

    Returns: 
        player(dict): Diccionario que representa al jugador más influyente.
    """
    player= max(players_stats, key=lambda x: x["goals"]*1.5 + x["goals_avoided"]*1.25 + x["assist"])
    return player

def get_promedio(players_stats,games):
    """ Calcula el promedio de los goles del equipo.

    Args:
        players_stats(list): parametro el cual contiene diccionarios. Debe contener la clave goals.
        games(integer): parametro que contiene la cantidad de partidos jugados.
    
    Returns:
        float: Devuelve el promedio de goles en el equipo.
    """
    total_goals= sum(player["goals"] for player in players_stats)
    return total_goals/games

def get_promedio_goleador(goals,games):
    """ Calcula el promedio de los goles del goleador.
    Args:
        goals(integer): parametro que contiene los goles del goleador.
        games(integer): parametro que contiene la cantidad de partidos jugados.
    
    Returns:
        float: Devuelve el promedio de goles por patidos del jugador.
    """
    return goals/games