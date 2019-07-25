#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title:----------(type name of code here)

Created on Mon Jul  1 13:13:23 2019

Author:---------Ty Sterling
Contact:--------ty.sterling@colorado.edu
Instituion:-----University of Colorado Boulder
Department:-----Material Science & Physics

Description: (type code or project description here!)

"""

import numpy as np
import Grid 
import Particle
import matplotlib.pyplot as plt

### size of square grid
# can change to whatever you want
gridsize = 100
### number of particles 
# can change to whatever you want
num_particles = 1000

### create the grid
grid = Grid.grid(gridsize)

### seed nucleation sites
# can put as many as you want
# usage is grid.seed(col,row), i.e. the grid location to place the nucleation site.
grid.seed(50,40)
grid.seed(50,60)

### loop over the particles
# each iteration proceeds until the particle lands on a nucleation site, then moves on
# to the next particle
for i in range(num_particles):
    print('\tNow on particle {} out of {}'.format(i+1,num_particles))

    ### initialize the particle on a grid edge
    # can initialize on a particular edge by specifying 'top', 'bottom', 'left', or 'right'
    # or randomly by specifying 'random' (default). you can also choose where along the 
    # edge to start it by specify an index for starting_point or 'none' for a random point
    # along the edge (default). i didn't do any error handling so be careful
    particle = Particle.particle(grid,starting_edge='random',starting_point='random')

    ### random walk until it runs into a filled grid element
    found_filled_site = False 
    while found_filled_site == False:
        found_filled_site = particle.random_walk(grid)

### save the last run for plotting again
# change to whatever you want
np.savetxt('last_run.csv',grid.grid)

### shift all non-zero data to a large number for use with imshow
# if the resolution betweent he background ( == 0) and the blob is bad, change the 
# multiplication factor below to a larger number. it shifts all the non-zero points 
# up by the specified amount
mask = (grid.grid != 0).astype(int)*1000

### plot it all
# change cmap to whatever you want, see the matplotlib docs for more info
fig, ax = plt.subplots()
ax.imshow(grid.grid+mask,cmap='viridis')
for axis in ['top','bottom','left','right']:
  ax.spines[axis].set_linewidth(1.5)
ax.minorticks_on()
ax.tick_params(which='both', width=1)
ax.tick_params(which='major', length=5)
ax.tick_params(which='minor', length=3, color='k')
ax.set_xlabel('X-coord',labelpad=4,fontweight='normal',
              fontsize='large')
ax.set_ylabel('Y-coord',labelpad=3,fontweight='normal',
              fontsize='large')
fig.suptitle('N = {}, Grid = {}x{}'
             .format(num_particles,gridsize,gridsize),y=0.95)
# comment out savefig to keep from writing it or name it whatever you want
plt.savefig('dendrite.png',format='png',dpi=300,bbox_inches='tight')
plt.show()

