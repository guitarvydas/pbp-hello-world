# Reasoning about concurrency and ordering

3 variations
- sequential (./seq)
- parallel (./par) but arbitrary ordering of outputs
- ordered (./ordered) time-ordering guaranteed to output "Hello" before "World"

see accompanying video ???, if you wish


## setup
[x] go to https://github.com/guitarvydas/pbp-kit and choose "Use This Template"
[x] create a new repo called "pbp-hello-world"
[x] cd ~/Demo
[x] git clone  https://github.com/guitarvydas/pbp-hello-world.git
[] create README.md
	[] cp README-hello-world.md into pbp-hello-world/README-hello-world
[x] cd pbp-hello-world
[] mkdir seq
[] mkdir par
[] mkdir ordered
[] copy stock Makefile into ./ordered
[] mv stock main.py into ./ordered
[] modify Makefile at top level, include only  `init:` rule
	[] make
## generic hello.py and world.py
[] create hello.py and world.py
	[] cheat: ../prefab
## ordered
[] cd ordered
[] create empty ordered.drawio `open -a draw.io`
[] create Makefile
	[] name=ordered
	[] remove `init:`
	[] remove stock arg
	[] fix path in Makefile
		[] `node ../pbp/das/das2json.mjs $(NAME).drawio`
		[] `sys.path.insert(0, '../pbp/kernel')`
[]  modify main.py
	[] add ../ to path
	[] import hello, world
	[] install hello, world
### begin with sequential
[] create sequential Hello World diagram
	[] rename tab to `main`
[ ] make
### intermediate step: parallel unordered
[] move and rewire
[] make
[] move World above Hello
[] make - same order (arbitrary)
[] change World to Hello, Hello to World
[] make - order is arbitrary, even though diagram reads like "Hello World", output is "World Hello"
### parallel, ordered
[] add 1->2 part to specify order, reasoning about order
[] make - output is "Hello World" as specified

