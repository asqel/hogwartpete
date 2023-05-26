text = \
"""4|--D--C----- -------D--C----|
3|DD-DD-DDbDDa-DAbDD-DD-DDbD|

4|--------D--C------------D-|
3|D-a---DD-DD-DDbDDaDDAbDD-D|

4|-C------------D--C--------|
3|D-DDbDDa-----D-DD-DDbDDaD-|

4|----D--C------------D--C--|
3|AbDD-DD-DDbDDa----DD-DD-DD|

5|----------------fDfFdFAFd-|
5|-----------------dGffGGf--|
4|----------D--C------------|
3|bDDaDDAbDD-DD-DD--------DD|

4|D--C------------D--C------|
3|-DD-DDbDDaD-AbDD-DD-DDbDDa|

4|------D--C------------D--C|
3|----DD-DD-DDbDDaD-AbDD-DD-|

6|------D--D----------------|
5|--AFFFAFF-----------------|
5|---DAA-AA-----------------|
4|------------G--F--e--d--De|
3|DD--------GG-GG-GG-GG-GG--|

4|--G--F--e--d------G--F--e-|
3|GG-GG-GG-GG-----GG-GG-GG-G|

5|--------------DCD-DDD-----|
5|------------------G-------|
4|-----------------b---G----|
4|-d--De--G--F---bbG-bbb--D-|
3|G-GG--GG-GG-GG--------DD-D|

4|-C------------D--C--------|
3|D-DDbDDaD-AbDD-DD-DDbDDa--|

4|----D--C------------D--C--|
3|--DD-DD-DDbDDaDDAbDD-DD-DD|

5|----------c---------------|
4|--------cc-ccAccGccFccgG--|
3|bDDa--------------------AA|

4|A--G--F--e------D--C------|
3|-AA-AA-aG-----DD-DD-DDbDDa|

6|--------------------D-----|
5|------------D-DFF-DA------|
5|------------F--DD-F-------|
4|-------------F---F--------|
4|------D--C---AA--A----D--C|
3|DDAbDD-DD-DD--------DD-DD-|

4|------------D--C----------|
3|DDbDDaDDAbDD-DD-DDbDD-a---|

5|------------------------d-|
4|-------------------------f|
4|--D--C------------D--C--bA|
3|-----------D--------------|
3|DD-DD-DDbDDaD-AbDD-DD-DD--|

5|f-GdAf--------------------|
5|d-f-Gd--------------------|
4|-G------------------------|
4|-A--A---F--f--d--C--CD--F-|
3|------DD-DD-DD-DDDD---DD-D|

4|-f--D---c-----F--f--d--C--|
3|D-DD-DD-----DD-DD-DD-DD---|

6|----------D-D---D---------|
5|----------AFDADAAF--------|
5|------------AFFF-D--------|
4|----F--f------------b--A--|
3|--DD-DD-DD--------GG-GG-GG|

4|g--F--FG--b--A--G---F-----|
3|-GG-G---GG-GG-GG-GG-----GG|

5|----------------------DD-D|
5|----------------------C---|
4|------------------------G-|
4|b--A--g--F--FG--b--A---bbb|
3|-GG-GG-GG-GG--GG-GG-GG----|

5|GDD-----------------------|
5|D-------------------------|
4|---G----------------------|
4|-bbb--F--f--d--C--CD--F--f|
3|----DD-DD-DD-DD-D---DD-DD-|

4|--D---c-----F--f--d--C--CD|
3|DD-D------DD-DD-DD-DDDD---|

5|------------------F--f--D-|
4|--F--f--D--c----cc-cc-cc-c|
3|DD-DD-DD-DD---------------|

5|-c--cD--f--D--d-----------|
4|c-cc-------------A------F-|
3|------AA-AA-AA-aG-----DD-D|

5|--------------------Gf--AG|
5|---------------------d----|
4|----------------------Gd--|
4|-f--d--C--CD--F--f----Af--|
3|D-DD-DD-D---DD-DD-DD----A-|

5|f-------------------------|
5|d-------------------------|
4|-f------------------------|
4|AGd-D---------------------|"""

m :list[dict[int,list[str]]]=[{}]

lines = text.split("\n")
for i in lines:
    if i == '':
        m.append({})
        continue
    oct = int(i[0])
    m[-1][oct] = []
    for k in range(2, i.find("|", 2)):
        note = i[k]
        if i[k].lower() == i[k] and i[k] != "-":
            note = i[k].upper()+"#"
        m[-1][oct].append(note)

from json import *
print(dumps(m,indent=1))


def to_temple_os_music(music):
    final_text = "e" #because e -> 0.125 and notes are between 1/5 and 1/6
    for i in music:
        ...