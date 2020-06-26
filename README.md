# AIMA-Pac-Man

The *Pac-Man* project was developed for **UC Berkeley's** ***"Introductory Artificial Intelligence"*** course, ***[CS 188](http://ai.berkeley.edu./project_overview.html)***. They apply an array of AI techniques to playing Pac-Man. 

This particular implementation of the aforementioned project was developed for the class of ***"Artificial Intelligence"***, in the Informatics Department, and was awarded with the maximum possible score by the auto-grader script *(50/50)*.

The whole project was implemented with *python2*.

### Table of Contents

[Part 1: Search](#search)

[Part 2: Multi-Agent Search](#multiagent)


<a name="search"/>

## [ Part 1: Search](http://ai.berkeley.edu./search.html)

In this part, the *Pac-Man* agent finds paths through his maze world, both to reach a particular location and to collect food efficiently. General search algorithms were built and applied to *Pac-Man* scenarios.

A makefile is provided. You can use the command ```$ make ``` for auto-grading and ```$ make clean``` to delete all generated *.pyc* files.

You can also check the full list of available commands in the [commands.txt](./search/commands.txt) file.

**Edited files:**
- [search.py](./search/search.py) : Where all the search algorithms reside.
- [searchAgents.py](./search/searchAgents.py) : Where all the search-based agents reside.

> Auto-grader evaluation:

```
Provisional grades
==================
Question q1: 3/3
Question q2: 3/3
Question q3: 3/3
Question q4: 3/3
Question q5: 3/3
Question q6: 3/3
Question q7: 5/4
Question q8: 3/3
------------------
Total: 26/25
```


<a name="multiagent"/>

## [Part 2: Multi-Agent Search](http://ai.berkeley.edu./multiagent.html)

In this part, agents for the classic version of *Pac-Man*, including ghosts, were designed.     

Along the way, both *minimax* and *expectimax* search were implemented. 

Efficient evaluation functions were also developed.

A makefile is provided. You can use the command ```$ make ``` for auto-grading and ```$ make clean``` to delete all generated *.pyc* files.

**Edited files:**

- [multiAgents.py](./multiagent/multiAgents.py) : Where all the multi-agent search agents reside.

> Auto-grader evaluation:
```
Provisional grades
==================
Question q1: 4/4
Question q2: 5/5
Question q3: 5/5
Question q4: 5/5
Question q5: 6/6
------------------
Total: 25/25
```