# Reasoning about concurrency and message ordering with PBP (Parts Based Programming)

3 variations
- sequential (./seq)
- parallel (./par) but arbitrary ordering of outputs
- ordered (./ordered) time-ordering guaranteed to output "Hello" before "World"
## usage:
`make init` in top directory
`cd seq` `make` to run sequential version
`cd par` `make` to run parallel, unordered version
`cd ordered` `make` to run parallel, ordered version

# Video
See the accompanying YouTube video ???, if you wish
# Part 1
Demo of building concurrent apps with PBP and for reasoning about event arrival and event ordering.

Github repository details are given in Part 2.

(† Message-passing events are called *mevents*)
# Part 2
To build a PBP project use pbp-kit available at https://github.com/guitarvydas/pbp-kit.

The final code for this demo can be cloned from https://github.com/guitarvydas/pbp-hello-world.

Part 2 of this video shows some of the initial steps for creating a "Hello World" project from first principles. For brevity, this video has been edited. 

The full set of steps for building "Hello World" are included in README.md of the pbp-hello-world repository. 

You can just look at the code and README.md in the "Hello World" repository instead of watching Part 2.

Part 2 of this video can be skipped or sped through. 

In essence, Part 2 shows how to:
- Create Leaf Parts in Python†.
- Modify Makefile(s) and main.py on a per-project basis.
- Transmogrify and run a PBP project.

(† Other videos will show how to use other languages for PBP projects)

Part 1 already showed how to create Container Parts using draw.io. (You *can* create Container parts in the usual way using a text editor, but draw.io and the PBP tools automate the process).

## Setup
[] go to https://github.com/guitarvydas/pbp-kit and choose "Use This Template"
[] create a new repo called "pbp-hello-world"
[] cd ~/Demo
[] git clone  https://github.com/guitarvydas/pbp-hello-world.git
[] create README.md
	[] cp README-hello-world.md into pbp-hello-world/README-hello-world
[] cd pbp-hello-world
[] mkdir seq
[] mkdir par
[] mkdir ordered
[] copy stock Makefile into ./ordered
[] mv stock main.py into ./ordered
[] modify Makefile at top level, include only  `init:` rule
	[] make
## generic hello.py and world.py Leaf Parts
[] create hello.py and world.py
	[] cheat: ../prefab
## Reasoning About Mevent Order
[] cd ordered
[] create empty ordered.drawio `open -a draw.io`
[] create Makefile
	[] name=ordered
	[] remove `init:`
	[] remove stock arg
	[] fix path in Makefile
		[] `node ../pbp/das/das2json.mjs $(NAME).drawio`
[]  modify main.py
	[] add ../ to path
	[] `sys.path.insert(0, '../pbp/kernel')`
	[] import hello, world
	[] install hello, world
### begin with sequential
[] create sequential Hello World diagram
	[] rename tab to `main`
[] make

(† See ./seq. subdirectory for final sequential version)
### intermediate step: parallel unordered
[] move and rewire
[] make
[] move World above Hello
[] make - same order (arbitrary)
[] change World to Hello, Hello to World
[] make - order is arbitrary, even though diagram reads like "Hello World", output is "World Hello"

(† See ./par/ subdirectory for final parallel version)

### parallel, ordered
[] add 1->2 part to specify order, reasoning about order
[] make - output is "Hello World" as specified

(† See ./ordered/ subdirectory for final parallel, ordered version)
