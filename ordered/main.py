import sys
sys.path.insert(0, '../pbp/kernel')
sys.path.insert(0, '../')
import kernel0d as zd

import hello
import world

[palette, env] = zd.initialize_from_files (sys.argv[1], sys.argv[4:])
hello.install (palette)
world.install (palette)
top = zd.start (arg=sys.argv[2], part_name=sys.argv[3], palette=palette, env=env)
