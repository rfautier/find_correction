# Find A Correction at 42 !

This script list all people who are log and validated / register a project.

## Example

```
(venv) $> python find_correction.py "Malloc"
rfautier : e2r3p13
aaklpote : e3r8p1
ccaballero : e3r2p2
llompal : e3r5p20
sgueko : e3r9p3
(venv) $> 
```

## Prerequisites

You need to have python3 (``` brew install python3 ```)

You need to have a token (UID and Secret).

To do this, go to https://profile.intra.42.fr/oauth/applications/new and create an application (You can enter Fake-Informations)

Then export to your environment your UID and SECRET

```
export FT42_UID="yourUIDHere"
```

```
export FT42_SECRET="yourSecretHere"
```

Or you can enter this environment variable in your RC (~/.zshrc)

Clone the project

```
git clone https://github.com/rfautier/find_correction.git && cd find_correction
```

Set the python3 environnement and requirement

```
virtualenv -p python3 venv && source venv/bin/activate && pip3 install -r requirement.txt
```

## Quickstart

```
python find_correction.py your_project
```


The first time, It's gonna be little longer depending on the projet.
Your gonna download all users who make the project. So next time, it's much,much faster !
The download is in your current directory, like an hidden files (`ls -a` to see them).

## Parameters

--campus CAMPUS  You can specify a campus. Paris is the default.

--update        To re-download all users register to an project
