Code for running a social tipping experiment at Leiden University,  based on code from Zan Mlakar.
Eveline de Bie and Anne Urai, 2024

Questions? Contact a.e.urai@fsw.leidenuniv.nl.


To be able to measure reaction times during the game in milliseconds, the lines of code stated below can be used. The reaction times can be measured for different pages and are stored in the main output file (so the responsetimes date file no longer has to be used for this). The code lines stated here are only to track the reaction times on the choice pages; add each of the lines of code to every page you want to track the time of, if this is multiple, give it different names for it to be stored in separate columns.

In the otree_moral file:
thesis_game:
  Choice.html: code lines 26-39
  models.py: code line 169
  pages.py: code line 19

 
The code was adapted from this comment by oTree user Katy Tabero: https://groups.google.com/g/otree/c/uobj5Yat8tE/m/grNBMOA_AwAJ
