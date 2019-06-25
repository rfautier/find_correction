# Find A Correction at 42 !

This script list all peaple who is log and validated / register to the project.

## Exemple

```
(venv) $> python find_correction.py "Malloc"
rfautier : e2r3p13
aaklpote : e3r8p1
ccaballero : e3r2p2
llompal : e3r5p20
sgueko : e3r9p3
(venv) $> script  
```

## Prerequisites

You need to have python3 (brew install python3)

You need to have a token (UID and Secret).

To do this, go to https://profile.intra.42.fr/oauth/applications/new and create an application (You can enter Fake-Informations)

Then export to your environement your UID and SECRET

```
export FT42_UID="yourUIDHere"
```

```
export FT42_SECRET="yourSecretHere"
```

Or you can enter this envionnement variable in your rc (~/.zshrc)

Clone the project

```
git clone TOFILL HERE
```

Set the python3 environnement and requirement

```
virtualenv -p python3 venv && source venv/bin/activate && pip3 install -r requirement.txt
```

## Quickstart

```
python find_correction.py your_project
```


The first time, It's gonna be little long deppending of the projet.
Your gonna download all users who make the project. So next time, it's much much faster !
The download is in your current directory like hidden file (`ls -a` to see them).

## Parameters

--campus CAMPUS  You can specifie a campus. Paris is the default.

--update        To re-download the register user to a project
