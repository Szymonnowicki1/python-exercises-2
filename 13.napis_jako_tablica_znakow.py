# -*- coding: utf-8 -*-
# %%
q = "THE EYES"

# %%
q = 'THEY SEE'

# %%
q = 'a gentleman'

# %%
print(q[3]+q[6]+q[7]+q[2]+q[0]+q[4]+q[5]+q[1]+q[8:])

# %%
q = 'THE MORSE CODE'

# %%
print(q[1:3]+q[6]+q[2]+q[3]+q[10:12]+q[4]+q[2]+q[3]+q[-2]+q[-3]+q[0]+q[7])

# %%
line = 'Program "Kropka nad i" nadamy o: 22:00'

# %%
print(line.find(':'))

# %%
time = line[line.find(':') + 2:]

# %%
tmp = line.find('"')

# %%
tmp = line[8:]

# %%
title = line[:8]

# %%
print(title, time)

# %%
(43 * 5 + 50 ) * 20 +1021 - 2001

# %%
(3 * 2 + 10 ) / 2 -3

# %%
presence = 0.85
note =3.5
finalWorkOK = False

print('you need to be present and have good notes or do the final work',presence >=0.8 and note >=3 or finalWorkOK)
print('you need to be present and have good notes and do the final work',presence >=0.8 and note >=3 and finalWorkOK)
    


























