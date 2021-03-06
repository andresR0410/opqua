
'''
Simple model
'''

from opqua.model import Model

model = Model()
model.newSetup('my_setup',default='vector-borne') # uses default parameters
model.newSetup('my_setup_2', contact_rate_host_vector=2e1, default='vector-borne')
    # uses default parameters, duplicate contact rate

model.newPopulation('my_population','my_setup')
model.addPathogensToHosts( 'my_population',{'AAAAAAAAAA':20} )

model.newIntervention( 10, model.addPathogensToHosts, [ 'my_population', {'TTTTTTTTTT':5, 'CCCCCCCCCC':5, } ] )
    # At time 10, adds pathogens of genomes TTTTTTTTTT and CCCCCCCCCC to 5 random hosts each

model.newIntervention( 20, model.addVectors, [ 'my_population', 10 ] )
    # At time 20, adds 10 healthy vectors to population
model.newIntervention( 20, model.newVectorGroup, [ 'my_population', '10_healthy_vectors', 10, True ] )
    # At time 20, selects 10 healthy hosts and stores them under the group id '10_healthy_hosts'
    # That last True argument is optional, it makes sure the random selected hosts are healthy
model.newIntervention( 20, model.addPathogensToVectors, [ 'my_population', {'GGGGGGGGGG':10}, '10_healthy_vectors' ] )
    # At time 20, adds pathogens of genomes TTTTTTTTTT and CCCCCCCCCC to 10
    # random hosts in the '10_new_vectors' group (so, all 10 of them)
    # The last '10_healthy_vectors' argument specifies which group to sample from
    # (if not specified, sampling occurs from whole population)

model.newIntervention( 50, model.setSetup, [ 'my_population', 'my_setup_2' ] )
    # At time 50, changes the parameters of my_population to those in my_setup_2

model.newIntervention( 70, model.protectHosts, [ 'my_population', 0.75, 'A' ] )
    # At time 70, protects a random 75% of the host population from pathogens with a 'A' in their genome

output = model.run(0,100)
data = model.saveToDataFrame('Intervention_examples.csv')
graph = model.compositionPlot('Intervention_examples.png', data,num_top_genomes=6)
