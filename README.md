# covid-compliance: central role of superspreaders

A stochastic network compartmental model is adapted from publicly available code https://github.com/ryansmcgee/seirsplus. This model uses a modified version of the SEIRS Network model class. 

Test2.1.py shows the 4 separate infections from 4 levels of compliances of non-superspreaders and superspreaders (ss). Code can be manipulated and run depending on selected population.

Test2.2.py shows the combined 4 compliance levels of non-ss and ss.

Test2.3.py shows the division of ss in a general population. SS is categorised as the top 20% of individuals in a population.

# Types of interactions:

- Local interactions (p_local), i.e. with close contacts. These are individuals with whom one has repeated, sustained, and/or physical interactions on a regular basis. Examples include housemates, family members, close coworkers or friends.

- Global interactions (p_global), i.e. with casual contacts. These are individuals with whom one has incidental, brief, or superficial contact on an infrequent basis. Examples include one-off or random acquaintances at the grocery store, on transit or in an elevator. Global interactions are represented in the models in the form of a parallel mode of mean-field global transmission. 



# Compliance is categorised into 4 levels:

- Full (or 100%) compliance: complying strictly with guidelines and minimising local and global connectivity. 
- Partial compliance is divided into two parts: 

    (i): complying with travel restrictions, meaning reducing the global contacts whilst maintaining close family and friends contact. 

    (ii): complying with close contacts, meaning reducing local network but increasing rare acquaintances in global connectivity. 
- No (or 0%) compliance: Ignoring social distancing guidelines and maximising local and global connectivity. 

##

Parameters p_local and p_global represent local and global connections respectively.
