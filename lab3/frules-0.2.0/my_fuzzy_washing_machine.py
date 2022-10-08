import sys
from frules.expressions import Expression as E
from frules.expressions import ltrapezoid, trapezoid, rtrapezoid
from frules.rules import Rule as R

# TASK 1
# Dirtiness
almost_clean = E(ltrapezoid(0.25, 1.00), "almost_clean")
dirty = E(rtrapezoid(0.50, 1.00), "dirty")

# Delicateness
very_delicate = E(ltrapezoid(2.00, 4.00), "very_delicate")
delicate = E(trapezoid(3.00, 4.00, 6.00, 7.00), "delicate")
not_delicate = E(rtrapezoid(6.00, 7.00), "not_delicate")

# # Dirtiness
# def rule_almost_clean(arg):
#     almost_clean_set = R(dirtiness = almost_clean)
#     return almost_clean_set.eval(dirtiness = arg)
# def rule_dirty(arg):
#     dirty_set = R(dirtiness = dirty)
#     return dirty_set.eval(dirtiness = arg)

# #Delicateness
# def rule_very_delicate(arg):
#     very_delicate_set = R(delicateness = very_delicate)
#     return very_delicate_set.eval(delicateness = arg)
# def rule_delicate(arg):
#     delicate_set = R(delicateness = delicate)
#     return delicate_set.eval(delicateness = arg)
# def rule_not_delicate(arg):
#     not_delicate_set = R(delicateness = not_delicate)
#     return not_delicate_set.eval(delicateness = arg)

# TASK 2
def compute_degree(function, crisp_value):
    fuzzy_set = R(crisp = function)
    return fuzzy_set.eval(crisp = crisp_value)

# TASK 3
def AND_function(arg1, arg2):
    return min(arg1, arg2)
def OR_function(arg1, arg2):
    return max(arg1, arg2)

# TASK 4
# Amount of Dirt = Dirtiness | Fabric Weight = Delicateness
def rules(number, fabric_weight, amount_of_dirt):
    if number == 1:
        return compute_degree(very_delicate, fabric_weight)
    elif number == 2:
        return OR_function(compute_degree(delicate, fabric_weight), compute_degree(almost_clean, amount_of_dirt))
    elif number == 3:
        return AND_function(compute_degree(delicate, fabric_weight), compute_degree(dirty, amount_of_dirt))
    elif number == 4:
        return AND_function(compute_degree(not_delicate, fabric_weight), compute_degree(dirty, fabric_weight))

# def rule_1(fabric_weight):
#     return compute_degree(very_delicate, fabric_weight)
# def rule_2(fabric_weight, amount_of_dirt):
#     return OR_function(compute_degree(delicate, fabric_weight), compute_degree(almost_clean, amount_of_dirt))
# def rule_3(fabric_weight, amount_of_dirt):
#     return AND_function(compute_degree(delicate, fabric_weight), compute_degree(dirty, amount_of_dirt))
# def rule_4(fabric_weight, amount_of_dirt):
#     return AND_function(compute_degree(not_delicate, fabric_weight), compute_degree(dirty, fabric_weight))

# TASK 5
# ---- INPUT HERE ----
inputs = [[0.90, 6.50], [2, 9]]
# ---- INPUT HERE ----
print("")
print("\033[1m  TASK 5 \033[0m")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range(len(inputs)):
    print(" \033[1m Antecedents \033[0m for input number: " + str(i))
    print(" Rule 1 antecedents: " + str( rules(1, inputs[i][1], inputs[i][0]) ))
    print(" Rule 2 antecedents: " + str( rules(2, inputs[i][1], inputs[i][0]) ))
    print(" Rule 3 antecedents: " + str( rules(3, inputs[i][1], inputs[i][0]) ))
    print(" Rule 4 antecedents: " + str( rules(4, inputs[i][1], inputs[i][0]) ))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# TASK 6
def weighted_output_level(output_level, number, fabric_weight, amount_of_dirt):
    return output_level * rules(number, fabric_weight, amount_of_dirt)

# TASK 7
# ---- OUTPUT LEVEL HERE ----
output_levels = [10, 40, 60, 80]
# ---- OUTPUT LEVEL HERE ----
print("")
print("\033[1m  TASK 7 \033[0m")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range(len(inputs)):
    print(" \033[1m Weighted Output Level \033[0m for input number: " + str(i))
    print(" Rule 1 weighted output level: " + str( weighted_output_level(output_levels[0], 1, inputs[i][1], inputs[i][0]) ))
    print(" Rule 2 weighted output level: " + str( weighted_output_level(output_levels[1], 2, inputs[i][1], inputs[i][0]) ))
    print(" Rule 3 weighted output level: " + str( weighted_output_level(output_levels[2], 3, inputs[i][1], inputs[i][0]) ))
    print(" Rule 4 weighted output level: " + str( weighted_output_level(output_levels[3], 4, inputs[i][1], inputs[i][0]) ))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# TASK 8
def weighted_average(input_nr):
    sum_outputs = float(0)
    sum_antecedents = float(0)
    for rules_number in range(1, 5):
        sum_outputs = sum_outputs + weighted_output_level(output_levels[rules_number - 1], rules_number, inputs[input_nr][1], inputs[input_nr][0])
        sum_antecedents = sum_antecedents + rules(rules_number, inputs[input_nr][1], inputs[input_nr][0])
    return sum_outputs / sum_antecedents

# TASK 9
print("")
print("\033[1m  TASK 9 \033[0m")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range(len(inputs)):
    print(" For input number " + str(i) + " \033[1m Weighted Average/Crisp Output Value \033[0m is:  " + str(weighted_average(i)))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# TASK 10
# ---- TEMPERATURE RANGE HERE ----
temperature_range = [10, 90]
# ---- TEMPERATURE RANGE HERE ----

def temperature(input_nr):
    percentage = (temperature_range[1] - temperature_range[0]) * weighted_average(input_nr) / 100
    percentage = percentage + temperature_range[0]
    return percentage

print("")
print("\033[1m  TASK 10 \033[0m")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range(len(inputs)):
    print(" For input number " + str(i) + " \033[1m Temperature Value \033[0m is:  " + str(temperature(i)))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")