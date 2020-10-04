# Job Applications Backlog

Scrape Indeed job postings based on inputs and export results to CSV file.

## Contents

- [About](#about)
- [Installation](#installation)
  - [Windows](#windows)
  - [Linux](#linux)
- [Quick Start](#quick-start)

## About

This project is intended to provide an easy way for job seekers to gather unique Indeed job postings. The link to each job ad is shortened to fit nicely within the CSV file.

## Installation

### Windows

#### Interpreter

To install Python 3 on Windows, you can search for it in the Microsoft Store. There are two versions, [3.7](https://www.microsoft.com/en-us/p/python-37/9nj46sx7x90p?activetab=pivot:overviewtab) and [3.8](https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l?activetab=pivot:overviewtab), either one should work. Installing from Microsoft Store will handle PATH setup for the current user. It also includes `pip`, the package manager for Python.

#### Download Repo

You can clone this repo using [Git for Windows](https://git-scm.com/download/win).

Alternatively, link to the zip file: [Download zip](https://github.com/kennguyen01/job-applications-backlog/archive/master.zip)

#### Code Editor

There are many options available but I recommend [VSCode](https://code.visualstudio.com/) for Windows.

Open the repo directory from inside VSCode. You can check your version of Python and `pip` by using **Ctrl + `**. This will open up the Windows Powershell terminal. Then enter these two commands:

1. `Python --version`
2. `pip --version`

To upgrade `pip` to the latest version, run `python -m pip install --upgrade pip`.

#### Virtual Environment

To create an isolated virtual environment for this project, run `python3 -m venv venv`. A popup from VSCode will ask if you want to select this environment for your project, click Yes.

Now you want to activate the virtual environment you just installed but by default, running scripts is disabled in PowerShell so you will not be able to activate the virtual environment yet. Instead, go to **File > Preferences > Settings** and type in `automation`.

You will see the option for **Terminal > Integrated > Automation Shell: Windows**. Click on `Edit in settings.json`. Then add this line between the curly brackets:

- `"terminal.integrated.shellArgs.windows": ["-ExecutionPolicy", "Bypass"],`

Save the file and restart VSCode, open the terminal again. Then type in `venv\Scripts\activate`. You will see `(venv)` in front of your path now.

To deactivate the virtual environment later, just type `deactivate` into the terminal.

#### Install Dependencies

To install required packages, run `pip3 install -r requirements.txt`.

### Linux

If you are on Linux, run these commands in the terminal:

```shell
$ sudo apt update
$ sudo apt install python3-venv
$ sudo apt install git
$ git clone https://github.com/kennguyen01/job-applications-backlog.git
$ cd job-applications-backlog
$ python3 -m venv venv
$ . venv/bin/activate
(venv)$ pip3 install -r requirements.txt
(venv)$ deactivate
```

Then run the program in your editor.

## Quick Start

To run the program, go to `main.py` file and click on the green arrow in the top right corner of the editor if you are using VSCode. The program will generate a `job-postings.csv` file when it finishes running.

There are random delays after each request so the process will take some time if you search in multiple cities and states.

### Example:

```shell
Enter all jobs: junior developer, software engineer
Enter all states: tx, ok
Enter all cities in TX: houston, dallas
Enter all cities in OK: oklahoma city
Enter experience level (entry/mid/senior). Leave empty for all jobs: entry
...
Scraping complete. 877 jobs added.
```
