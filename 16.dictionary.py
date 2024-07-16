# -*- coding: utf-8 -*-
# %%
chanels = {'Google' : 1480, 'Email' : 300, 'Natural Traffic' : 440, 'TV Sport' : 700}

# %%
chanels['Email']

# %%
chanelsUpdate = {'Natural Traffic' : 520, 'News' : 600}

# %%
chanels.update(chanelsUpdate)

# %%
chanels.keys()

# %%
chanels.pop('Email')