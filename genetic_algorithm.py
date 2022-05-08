from random import randint, choice

def createPopulation(pop_size):
    """Generates the beetle population and returns it"""
    beetle_list=[]
    while pop_size>0:
        v1=randint(0,255)
        v2=randint(0,255)
        v3=randint(0,255)
        bettle=[v1,v2,v3]
        beetle_list.append(bettle)
        pop_size-=1
    return beetle_list

def fitnessFunction(beetle):
    """Fitness function to filter beetle sums equal or less than 500"""
    beetle_sum=beetle[0]+beetle[1]+beetle[2]
    if beetle_sum<=500:
        return True
    else:
        return False


def getSmallestBeetle(beetle_list):
    """Get the smallest beetle in a beetle list and its position """
    smallest_sum=beetle_list[0][0]+beetle_list[0][1]+beetle_list[0][2]
    smaller_beetle=beetle_list[0]
    smaller_pos=0
    for i in range(len(beetle_list)-1):
        beetle_sum_next=beetle_list[i+1][0]+beetle_list[i+1][1]+beetle_list[i+1][2]
        if smallest_sum>beetle_sum_next:
            smaller_beetle=beetle_list[i+1]
            smallest_sum=beetle_sum_next
            smaller_pos=i+1
    return [smaller_beetle,smaller_pos]

def selectParents(beetle_list):
    """Selects the top three smallest beetles in a beetle list"""
    parents=[]
    parents_amount=3
    for i in range(0,parents_amount):
        smallest_beetle_info=getSmallestBeetle(beetle_list)
        pos_smallest=smallest_beetle_info[1]
        smallest_beetle=smallest_beetle_info[0]
        parents.append(smallest_beetle)
        del beetle_list[pos_smallest] #removes the previously smallest beetle
    return parents     

    
def selection(beetle_list):
    """Selects the beetles with the smallest sums in a population"""
    first_win_list=[]
    final_win_list=[]
    pop_size=len(beetle_list)
    for i in range(pop_size):
        if fitnessFunction(beetle_list[i]):
            first_win_list.append(beetle_list[i])
    final_win_list=selectParents(first_win_list)
    return final_win_list

def crossOver(beetle_list):
    """Making cross-over among two beetles"""
    positions=[]
    first_beetle=choice(beetle_list)
    second_beetle=choice(beetle_list)
    if first_beetle==second_beetle:
        second_beetle=choice(beetle_list)
    for i in range(1,4):
        randpos=randint(0,2)
        positions.append(randpos)
    new_beetle=[first_beetle[positions[0]],second_beetle[positions[1]],second_beetle[positions[2]]]
    return new_beetle

def mutation(beetle_list):
    """Generates a new beetle via mutation"""
    mut_values=[-40,40]
    rand_beetle=choice(beetle_list)
    pos=randint(0,2)
    new_beetle=[]
    mut=choice(mut_values)
    check=rand_beetle[pos]+mut
    if check >= 0 and check <= 255:
        new_beetle=rand_beetle
        new_beetle[pos]+=mut
    else:
       mut=mut*-1
       new_beetle=rand_beetle
       new_beetle[pos]+=mut
       new_beetle=rand_beetle
    return new_beetle


def getGenSum(beetle_list):
    """Calculates the generation sum of values"""
    sum=0
    for i in range(len(beetle_list)):
        sum+=beetle_list[i][0]+beetle_list[i][1]+beetle_list[i][2]
    return sum

def compareBeetles(first_beetle,second_beetle):
    """Compares two beetles and says what is the best for the dark forest"""
    sum1=first_beetle[0]+first_beetle[1]+first_beetle[2]
    sum2=second_beetle[0]+second_beetle[1]+second_beetle[2]
    if sum1<sum2:
        return "first"
    else:
        return "second"

def geneticAlg(pop_size, gen_amount):
    """The Genetic Algorithm"""
    initial_population=createPopulation(pop_size)
    print("The initial population was: ", initial_population)
    population=initial_population
    sum_gen=getGenSum(initial_population)
    best_gen=[]
    best_beetle=getSmallestBeetle(initial_population)[0]
    for i in range(0,gen_amount):
        selected_beetles=selection(population)
        new_generation=selected_beetles
        for i in range(0,4): #Generate four beetles using cross-over
            cross_beetle=crossOver(population)
            new_generation.append(cross_beetle)
        for i in range(0,3): #Generate three beetles using mutation
            mut_beetle=mutation(population)
            new_generation.append(mut_beetle)
        sum_newgen=getGenSum(new_generation)
        if sum_gen>sum_newgen:
            sum_gen=sum_newgen
            best_gen=new_generation
        beetle=getSmallestBeetle(new_generation)[0]
        if compareBeetles(best_beetle,beetle)=="second":
            best_beetle=beetle
    print("The best generation was: ", best_gen)
    print("The best beetle was:", best_beetle)

def main():
    pop_size=10
    gen_amount=100
    geneticAlg(pop_size,gen_amount)

main()
