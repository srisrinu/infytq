child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]
child_dict=dict(zip(child_id,chocolates_received))


def reward_child(child_id_rewarded,extra_chocolates):
    if(extra_chocolates<1):
        return("Extra chocolates is less than 1")
    if(child_id_rewarded not in child_id):
        return("Child id is invalid")
    else:
        child_dict[child_id_rewarded]+=extra_chocolates
    return(sum(child_dict.values()))
print(reward_child(20,0))