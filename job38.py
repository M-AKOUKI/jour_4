def fds(type,saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("poire, fraise, cassis")
    elif type == "légume" and saison =="hiver":
        print("carotte, topinambour et endive")
    else:
        if type == "légume" and saison == "été":
            print("artichaut, aubergine, navet")

fds("fruits","hiver")
fds("fruits","été")
fds("légume","hiver")
fds("légume","été")