# Update
You can directly go to [peerfinder.app](https://peerfinder.app) for find peer :D

# Find A Correction at 42 !

This script list all people who are log and validated / register a project.

## Example

```
(venv) $> python find_correction.py "Malloc"
Login     Project status          Validated    Final Mark    Position
--------  ----------------------  -----------  ------------  ----------
rfautier    in_progress             None         None          e3r5p11
aaklpote    in_progress             None         None          e3r10p5
ccaballero  in_progress             None         None          e2r4p4
llompal     finished                True         123           e3r5p19
sgueko      waiting_for_correction  None         None          e3r13p9

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

Set the python3 environment and requirement

```
virtualenv -p python3 venv && source venv/bin/activate && pip3 install -r requirement.txt
```

## Quickstart

```
python find_correction.py your_project
```
or, with Docker
```
docker build -t find_correction .
docker run -e FT42_UID="yourUIDHere" -e FT42_SECRET="yourSecretHere" find_correction your_project
```
(add `-v $PWD:/app` if you want to persist files)


The first time, It's gonna be little longer depending on the projet.
Your gonna download all users who make the project. So next time, it's much,much faster !
The download is in your current directory, like an hidden files (`ls -a` to see them).

## Parameters

``` --campus ``` CAMPUS  You can specify a campus. Paris is the default.

``` --update ```        To re-download all users register to an project
