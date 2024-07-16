# -*- coding: utf-8 -*-
# %%
 marketing_z_elementami = ['loyality program', 'client promotion', 'market research']
 
 # %%
 marketing_z_elementami.append('public relations')
 
# %%
marketing_z_elementami[2]

# %%
marketing_z_elementami.insert(1, 'investor relations')

# %%
emailMarketing = marketing_z_elementami.copy()

# %%
emailMarketing.sort()

# %%
internalEmails = ['internal communication']

# %%
emailMarketing.extend(internalEmails)

# %%
emailTuple = tuple(emailMarketing)