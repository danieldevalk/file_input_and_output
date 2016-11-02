def movie_ratings(users):
    user_responses = users
    user_ratings = []
    for num in range(user_responses):
        spotlight_rating = input("How would you rate Spotlight? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        the_big_short_rating = input("How would you rate The Big Short? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        bridge_of_spies_rating = input("How would you rate Bridge of Spies? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        brooklyn_rating = input("How would you rate Brooklyn? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        mad_max_rating = input("How would you rate Mad Max: Fury Road? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        the_martian_rating = input("How would you rate The Martian? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        the_revenant_rating = input("How would you rate The Revenant? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        room_rating = input("How would you rate Room? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        user_ratings.append([num+1, spotlight_rating, the_big_short_rating, bridge_of_spies_rating, brooklyn_rating, mad_max_rating, the_martian_rating, the_revenant_rating, room_rating])
        if num > 0:
            print("Thank you for the ratings. Pleasel allow the next user to rate.")

def add_oscar_opinions(file):
    new_file = open(file+".tsv", 'w')
    user_ratings = []
    users = input("How many users are rating? ")
    user_responses=int(users)
    for num in range(user_responses):
        spotlight_rating = input("How would you rate Spotlight? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        the_big_short_rating = input("How would you rate The Big Short? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        bridge_of_spies_rating = input("How would you rate Bridge of Spies? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        brooklyn_rating = input("How would you rate Brooklyn? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        mad_max_rating = input("How would you rate Mad Max: Fury Road? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        the_martian_rating = input("How would you rate The Martian? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        the_revenant_rating = input("How would you rate The Revenant? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        room_rating = input("How would you rate Room? (0 : I did not see the movie, 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic) ")
        if num > 0:
            print("Please let the next user rate.")
        user_ratings.append([num+1, spotlight_rating, the_big_short_rating, bridge_of_spies_rating, brooklyn_rating, mad_max_rating, the_martian_rating, the_revenant_rating, room_rating])
    for num in user_ratings:
        new_file.write(str(num))
        new_file.write("\t")

add_oscar_opinions("oscar_opinions")

def read_file(file):
    file_object = open(file+'.tsv', 'r')
    ratings = file_object.read()
    ratings=ratings.replace('[','')
    ratings=ratings.replace(',','')
    ratings=ratings.replace(']','')
    ratings=ratings.replace('"','')
    ratings=ratings.replace(' ','')
    ratings=ratings.replace("'",'')
    ratings_list = ratings.split('\t')
    
    
    spotlight_views=0
    the_big_short_views=0
    bridge_of_spies_views=0
    brooklyn_views=0
    mad_max_views=0
    the_martian_views=0
    the_revenant_views=0
    room_views=0

    spotlight_rating=0
    the_big_short_rating=0
    bridge_of_spies_rating=0
    brooklyn_rating=0
    mad_max_rating=0
    the_martian_rating=0
    the_revenant_rating=0
    room_rating=0
    
    for item in ratings_list:
        for num in range(len(item)):
            if num == 0:
                continue
            if num == 1:
                spotlight_views+=1
                spotlight_rating+=int(item[num])
            if num == 2:
                the_big_short_views+=1
                the_big_short_rating+=int(item[num])
            if num == 3:
                bridge_of_spies_views+=1
                bridge_of_spies_rating+=int(item[num])
            if num == 4:
                brooklyn_views+=1
                brooklyn_rating+=int(item[num])
            if num == 5:
                mad_max_views+=1
                mad_max_rating+=int(item[num])
            if num == 6:
                the_martian_views+=1
                the_martian_rating+=int(item[num])
            if num == 7:
                the_revenant_views+=1
                the_revenant_rating+=int(item[num])
            if num == 8:
                room_views+=1
                room_rating+=int(item[num])
    spotlight=str(spotlight_views)
    the_big_short=str(the_big_short_views)
    bridge_of_spies=str(bridge_of_spies_views)
    brooklyn=str(brooklyn_views)
    mad_max=str(mad_max_views)
    the_martian=str(the_martian_views)
    the_revenant=str(the_revenant_views)
    room=str(room_views)

    spotlight_avg=float(spotlight_rating)/spotlight_views
    the_big_short_avg=float(the_big_short_rating)/the_big_short_views
    bridge_of_spies_avg=float(bridge_of_spies_rating)/bridge_of_spies_views
    brooklyn_avg=float(brooklyn_rating)/brooklyn_views
    mad_max_avg=float(mad_max_rating)/mad_max_views
    the_martian_avg=float(the_martian_rating)/the_martian_views
    the_revenant_avg=float(the_revenant_rating)/the_revenant_views
    room_avg=float(room_rating)/room_views

    spotlight_str=str(spotlight_avg)
    the_big_short_str=str(the_big_short_avg)
    bridge_of_spies_str=str(bridge_of_spies_avg)
    brooklyn_str=str(brooklyn_avg)
    mad_max_str=str(mad_max_avg)
    the_martian_str=str(the_martian_avg)
    the_revenant_str=str(the_revenant_avg)
    room_str=str(room_avg)
    
    print(spotlight + " people saw Spotlight with an average rating of " + spotlight_str + "!")
    print(the_big_short + " people saw The Big Short with an average rating of " + the_big_short_str + "!")
    print(bridge_of_spies + " people saw Bridge of Spies with an average rating of " + bridge_of_spies_str + "!")
    print(brooklyn + " people saw Brooklyn with an average rating of " + brooklyn_str + "!")
    print(mad_max + " people saw Mad Max: Fury Road with an average rating of " + mad_max_str + "!")
    print(the_martian + " people saw The Martian with an average rating of " + the_martian_str + "!")
    print(the_revenant + " people saw The Revenant with an average rating of " + the_revenant_str + "!")
    print(room + " people saw The Room with an average rating of " + room_str + "!")

read_file("oscar_opinions")
    
team_data = [['Mets',10,5,5], ['Yankees',11,2,2], ['Bears',7,15,0], ['Senators',5,30,1], ['Clowns',10,50,1]]

def score(team):
    team_name, wins, losses, ties = team
    wins_int=int(wins)
    losses_int=int(losses)
    ties_int=int(ties)
    total_games = wins_int+losses_int+ties_int
    print(total_games)
    score = (wins_int + (ties_int*.5))/total_games
    return score

def sort_teams(team_file,sorted_team_file):
    team_object = open(team_file+".tsv", 'r')
    new_team_object = open(sorted_team_file+".tsv", 'w')
    teams = team_object.read()
    team_list = teams.split('\t')
    new_team_list=[]
    wins=0
    losses=0
    ties=0
    for item in range(len(team_list)):
        if item%4 == 0:
            name=team_list[item]
        if item%4 == 1:
            wins=team_list[item]
        if item%4 == 2:
            losses=team_list[item]
        if item%4 == 3:
            ties=team_list[item]
            new_team_list.append([name, wins, losses, ties])
    print(new_team_list)
    choice = input("Would you want to input additional team data?")
    if choice == 'yes' or choice == 'Yes':
        team_name = input("Input Team Name")
        wins = input("Number of Wins")
        losses = input("Number of Losses")
        ties = input("Number of Ties")
        wins2 = int(wins)
        losses2 = int(losses)
        ties2 = int(ties)
        new_team_list.append([team_name, wins2, losses2, ties2])
    
    sorted_teams = []
    for team in new_team_list:
        sorted_teams.append([score(team),team[0]])
    sorted_teams.sort()
    sorted_teams.reverse()
    for team in range(len(sorted_teams)):
        print(sorted_teams[team][0], ': ', sorted_teams[team][1])
    for num in sorted_teams:
        outstring=''
        for item in num:
            outstring=outstring+str(item)+'\t'
        new_team_object.write(outstring)

sort_teams('teams','sorted_teams')

def read_file(text_file,new_text_file):
    text=open(text_file+'.txt', 'r')
    read_lines=text.readlines()
    a_count=0
    e_count=0
    i_count=0
    o_count=0
    u_count=0
    for num in read_lines:
        for count in num:
            if 'a' in count:
                a_count+=1
            if 'e' in count:
                e_count+=1
            if 'i' in count:
                i_count+=1
            if 'o' in count:
                o_count+=1
            if 'u' in count:
                u_count+=1

    new_text=open(new_text_file+'.vowel_profile', 'w')
    new_text.write('There were ')
    new_text.write(str(a_count))
    new_text.write(" a's in this text!")
    new_text.write('\n')
    new_text.write('There were ')
    new_text.write(str(e_count))
    new_text.write(" e's in this text!")
    new_text.write('\n')
    new_text.write('There were ')
    new_text.write(str(i_count))
    new_text.write(" i's in this text!")
    new_text.write('\n')
    new_text.write('There were ')
    new_text.write(str(o_count))
    new_text.write(" o's in this text!")
    new_text.write('\n')
    new_text.write('There were ')
    new_text.write(str(u_count))
    new_text.write(" u's in this text!")
    new_text.write('\n')
    
read_file("example_text", "new_text")
