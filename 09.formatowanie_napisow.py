# -*- coding: utf-8 -*-
helloMessage = "Hello %s!"

# %%
print(helloMessage % ('Kate'))

# %%
helloMessage % ('Chris')

# %%
helloMessage = "Hello {0:s}!"

# %%
print(helloMessage.format('Kate'))

# %%
print(helloMessage.format('Chris'))

# %%
helloMessage = "%s has %d %s"

# %%
helloMessage % ('Kate', 1, 'animals')
helloMessage % ('Chris', 100000, '$')

# %%
helloMessage = "{0:s} has {1:d} {2:s}"
helloMessage.format('Kate', 1, 'animals')

# %%
line = '{0:20s} costs {1:6s}'
print(line.format('lody', '10'))


















