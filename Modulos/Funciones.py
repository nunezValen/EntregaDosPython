
def generate_player_stats(names,goals,goals_avoided,assist):
    """ Genera un diccionario a partir de los parametros ingresados que representaran el valor de cada clave. Para lograrlo iterara sobre la longitud de names.
      names: parametro de tipo lista
      goals: parametro tipo lista
      goals_avoided: parametro tipo lista
      assist: parametro tipo lista 
      return: tipo diccionario """
    player_stats=[]
    for i in range(len(names)):
        player={"name": names[i],"goals": goals[i],"goals_avoided": goals_avoided[i], "assist": assist[i]}
        player_stats.append(player)
    return player_stats


