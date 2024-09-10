---
title       : Essential Tools
author      : Haris Volos
description : This is an introduction to a few essential tools.
keywords    : tools, ansible, bash, gnuplot, wrk, nginx, benchmarking
marp        : true
paginate    : true
theme       : jobs
--- 

<style>
.img-overlay-wrap {
  position: relative;
  display: inline-block; /* <= shrinks container to image size */
  transition: transform 150ms ease-in-out;
}

.img-overlay-wrap img { /* <= optional, for responsiveness */
   display: block;
   max-width: 100%;
   height: auto;
}

.img-overlay-wrap svg {
  position: absolute;
  top: 0;
  left: 0;
}

</style>

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

<style>   

   .cite-author {     
      text-align        : right; 
   }
   .cite-author:after {
      color             : orangered;
      font-size         : 125%;
      /* font-style        : italic; */
      font-weight       : bold;
      font-family       : Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; 
      padding-right     : 130px;
   }
   .cite-author[data-text]:after {
      content           : " - "attr(data-text) " - ";      
   }

   .cite-author p {
      padding-bottom : 40px
   }

</style>

<!-- _class: titlepage -->

# Lab: Essential Tools
---

# Essential Tools

- Version control: Git and GitHub
- Configuration management: Ansible
- HTTP Benchmarking: wrk

---

# Git and GitHub

---

# Demystifying Git and GitHub

*Git* is the software that allows us to do version control

- Git tracks changes to your source code so that you don’t lose any history of your project

*Github* is an online platform where developers host their source code (and can share it the world)

- You can host remote repositories on https://github.com/
- You edit and work on your content in your local repository on your computer, and then you send your changes to the remote

---

# Why you should use Git

To be kind to yourself

To be kind to your collaborators

To ensure your work is reproducible

## Spillover benefits

👩‍🔬 📐 It imposes a certain discipline to your programming.

🤓 🔥 You can be braver when you code: if your new feature breaks, you can revert back to a version that worked!

---

# Workflow

![h:500 center](figures/git-remote-local.png)

---

# Working locally

```bash
# create a new directory, and initialize it with git-specific functions
git init my-repo

# change into the `my-repo` directory
cd my-repo

# create the first file in the project
touch README.md

# git isn't aware of the file, stage it
git add README.md

# take a snapshot of the staging area
git commit -m "add README to initial commit"
```

---

# Hosting your source code on GitHub

- Visit https://github.com/new to create a new GitHub repository

![bg width:80% right:50%](figures/github-create-repo-public.png)

---

# Pushing changes to the remote repository

```bash
# set a new remote
git remote add origin git@github.com:YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
# rename your local branch to main
git branch -M main
# push commits made on your local branch to a remote repository
git push -u origin main
```

---

# git pull

Use this to fetch changes from the remote and to merge them in to your local repository

- Your collaborators have been adding some awesome content to the repository, and you want to fetch their changes from the remote and update your local repository

```bash
git pull
```

- What this is doing under-the-hood is running a git fetch and then git merge.

---

# git clone

- Use this to get a copy of an existing Git repository

- To get a copy of the course's repository:

```
git clone https://github.com/ucy-coast/cs452-fa24.git
```

---

# More command line tips

---

# Tell Git who you are

As a first-time set up, you need to tell Git who you are.

```bash
git config --global user.name "Your name"
git config --global user.email "alice@example.com"
```

---

# git status

Use this to check at what stage of the workflow you are at

- You have made some local modifications, but haven't staged your changes yet

```bash
git status
```

```bash
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)
         modified:   penguins.R
no changes added to commit (use "git add" and/or "git commit -a")
```

---

# Adding files

To stage specific files in your repository, you can name them directly

```bash
git add penguins.R other-penguins.R
```

or you can add all of them at once

```bash
git add .
```

---

# Ignoring files

You might want to not track certain files in your local repository, e.g., sensitive files such as credentials. But it might get tedious to type out each file that you do want to include by name.

Use a `.gitignore` file to specify files to always ignore.

Create a file called `.gitignore` and place it in your repo. The content of the file should include the names of the files that you want Git to not track.

---

# git log

Use this to look at the history of your repository.

Each commit has a specific hash that identifies it.

```
git log
commit af58f79bfa4301643025dd6c8767e65349cf407a
Author: Name <Email address>
Date:   DD-MM-YYYY
    Add penguin script
```

You can also find this on GitHub, by going to github.com/user-name/repo-name/commits.

You can go back in time to a specific commit, if you know its reference.

---

# Undoing mistakes

Imagine you did some work, committed the changes, and pushed them to the remote repo. But you'd like to undo those changes.

Running git revert is a "soft undo".

Say you added some plain text by mistake to penguins.R. Running git revert will do the opposite of what you just did (i.e., remove the plain text) and create a new commit. You can then git push this to the remote.

```bash
git revert <hash-of-the-commit-you-want-to-undo>
git push
```

---
# Undoing mistakes

`git revert` is the safest option to use.

It will preserve the history of your commits.

```bash
git log
commit 6634a076212fb7bac16f9525feae1e83e0f200ca
Author: Name <Email address>
Date:   DD-MM-YYYY
     Revert "Add plain text to code by mistake"
     This reverts commit a8cf7c2592273ef6a28920222a92847794275868.
commit a8cf7c2592273ef6a28920222a92847794275868
Author: Name <Email address>
Date:   DD-MM-YYYY
    Add plain text to code by mistake
```

---

# Ansible 

---

# What is the problem?

- Configuration management 
  - CM == Writing some kind of system state description + 
    Using a tool to enforce that the servers are in that state
  - CLI is vendor dependent
- Ansible exposes a domain-specific language (DSL) that you use to describe the state of your servers
- Can also be used for Deployment and Orchestration

---

# What is Ansible?

- IT automation, configuration management and provision tool
- It uses playbooks to 
   - deploy, manage, build, test and configure 
   - anything from full server environments to website to custom compiled source code for application
   - a text file by YAML
      - Human readable

---

# How does it work?

<div class="columns">

<div>

![w:400 center](figures/ansible-webservers-yml.png)
  
</div>

<div>

![w:500 center](figures/ansible-webservers-architecture.png)

</div>

</div>

---

# Architecture

![w:800 center](figures/ansible-architecture.png)

---

# Push based vs. Pull based

- Tool like Puppet and Chef are pull based
   - Agents on the server periodically checks for the configuration information from central server (Master)
- Ansible is push based
   - Central server pushes the configuration information on target servers
   - You control when the changes are made on the servers
   - Ansible has official support for pull  mode, using a tool  it ships with called ansible-pull

---

# Push based vs. Pull based (cont'd)

![w:800 center](figures/ansible-push-vs-pull.png)

---

# Host inventory

- Ansible can manage only the servers it explicitly knows about
- Information about devices is provided by specifying them in an inventory file
- Each server needs a name that Ansible will use to identify it. You can use the hostname of the server.
- Pass additional arguments to tell Ansible how to connect to it
- Default location is /etc/ansible/hosts

---

# Inventory example

```ini
[webservers]
node1
```

---

# Modules

- Modules (also referred as task plugins or library plugins) are the ones which actually get executed inside playbook
- These are scripts that come packaged with Ansible and preform some kind of action on a host
- Example:
   - `apt`: Installs or removes packages using the apt package manager
   - `copy`: Copies a file from local machine to the hosts
   - `file`: Sets the attribute of a file, symlink, or directory
   - `service`: Starts, stops, or restarts a service

---

# YAML basics

- Start of file: `---`
- Comments: `#`
- List: `- <item>` or `[<item>, <item>]`
- Dictionary/Mapping: `<label>:<value>` or `{<label>:<value>}`
- Line Folding: `>`

---

# YAML example

```yaml
---
# This is a description by YAML
name: Alice
family: NA
Address: Wonderland, >
               Antipodes
ID:1111
Courses:
  - course_name: abc
    course_id: 123
  - course_name: xyz
    course_id: 456
```

---

# Ansible playbook

- Ansible’s configuration, deployment, and orchestration language 
- Written in YAML, declaratively define your configuration
- A playbook describes which hosts (what Ansible calls remote servers) to configure, and an ordered list of tasks to perform on those hosts.
- Command to run the playbook:

   ```
   ansible-playbook file.yml
   ```

---

# Playbook simple example

--- 

```
- name: a test playbook
  hosts: webservers
  tasks:
      - name: check connectivity
        ping:
      - name: just a touch
        command: touch /tmp/123.txt
```

---

# How does it work (in details)?

<div class="columns">

<div>

Ansible will do the following:
1. Generate a Python script that installs Nginx package
2. Copy the script to web1, web2, and web3
3. Execute the script on web1, web2, and web3
4. Wait for the script to complete execution on all hosts

  
</div>

<div>

![w:400 center](figures/ansible-webservers-yml.png)

![w:400 center](figures/ansible-webservers-architecture.png)

</div>

</div>

---

# Notes on running playbook 

- Ansible runs each task in parallel across all hosts
- Ansible waits until all hosts have completed a task before moving to the next task
- Ansible runs the tasks in the order that you specify them

---

# Handlers
- Handlers usually run after all of the tasks
- Handlers are triggered by `notify` command
- They run only once, even if they are notified multiple times. 
- If a play contains multiple handlers, the handlers always run in the order that they are defined in the handlers section, not the notification order.
- The official Ansible docs mention that the only common uses for handlers are for restarting services and for reboots

---

# Handler simple example

```yaml
--- 
- name: a test playbook
  hosts: test1
  handlers:
      - name: record new
        command: touch /tmp/new.txt
  tasks:
      - name: check connectivity
        ping:
      - name: just a touch
        command: touch /tmp/123.txt
        notify: record new
```

---

# Variables

- The simplest way to define variables is to put a `vars` section in your playbook with the names and values of variables
- `{{ variable_name }}` is substituted by its value
- To set the value of a variable based on the result of a task, we create a *registered variable* using the register clause when invoking a module.
   - The value of variable is the *dictionary*, we can access its fields

---

# Variables simple example

```yaml
--- 
- name: a test playbook
  hosts: test1
  vars:
      target_file: /tmp/123.txt
      new_file: /tmp/new.txt
  handlers:
      - name: save time
        shell: echo {{ date_var.stdout }} > {{ new_file }}
      - name: get time
        command: date
        register: date_var
        notify: save time
  tasks:
      - name: just a touch
        command: touch {{ target_file }}
        notify: get time
```

---
# Facts

- When Ansible gathers facts, it connects to the host and queries it for all kinds of details about the host
   - CPU architecture
   - operating system
   - IP addresses
   - memory info
   - ...
- This information is stored in variables that are called *facts*, and they behave just like any other variable.

---

# Facts simple example

```yaml
--- 
- name: Test Facts
  hosts: test1
  gather_facts: True
  tasks:
      - debug: var=ansible_distribution
      - debug: var=ansible_architecture
      - debug: var=ansible_bios_date
      - debug: var=ansible_devices
```

---

# Ansible features

- Easy-to-Read Syntax: built on top of YAML
- Agentless: no need for agent installation and management
- Built on top of Python and hence provides a lot of Python’s functionality
- Uses SSH for secure connections
- Follows Push based architecture for sending configurations
- Very easy and fast to setup, minimal requirements
- Built-in Modules
   - Ansible modules are *declarative*; you use them to describe the state you want the server to be in.
   - Modules are also *idempotent*. It means that it’s safe to run an Ansible playbook multiple times against a server

---

# Demo: Configure webserver with nginx

<div class="columns">

<div>

- Open a remote SSH terminal session to `node0`

- Create inventory file `hosts`

   ```
   [webservers]
   node1
   ```
- Create playbook file `nginx.yml`

- Run playbook

   ```
   ansible-playbook -i ./hosts nginx.yml
   ```
  
</div>

<div>

```
---
- name: Configure webserver with nginx
  hosts: webservers
  vars:
    web_root: "{{ ansible_env.HOME }}/static-site"
  tasks:
    - name: install nginx
      apt: 
        name: nginx 
        update_cache: yes
      become: yes
    
    - name: copy the nginx config file
      template:
        src: static_site.cfg.j2
        dest: /etc/nginx/sites-available/static_site.cfg
      become: yes
    
    - name: create symlink
      file:
        src: /etc/nginx/sites-available/static_site.cfg
        dest: /etc/nginx/sites-enabled/default
        state: link
      become: yes

    - name: ensure {{ web_root }} dir exists
      file:
        path: "{{ web_root }}"
        state: directory

    - name: copy index.html
      copy: 
        src: index.html
        dest: "{{ web_root }}/index.html"

    - name: restart nginx
      service: 
        name: nginx 
        state: restarted
      become: yes
```

</div>

</div>

---
# Demo: Configure webserver with nginx (cont'd)

- Visit `http://node1/index.html`

- Web page should look like this:

   ```
   nginx, configured by Ansible
   If you can see this, Ansible successfully installed nginx.
   ```

---

# HTTP Benchmarking with `wrk`

---

# `wrk`

- Modern HTTP benchmarking tool

- Measures the latency of your HTTP services at high loads

---

# Building `wrk` from source

```
git clone https://github.com/wg/wrk.git
cd wrk
make -j
```

Note: Use `-j` for parallel build

---

# Benchmarking nginx

<div class="columns">

<div>

![w:500](figures/wrk-application-overview.png)
  
</div>

<div>

- Benchmarking machine running `wrk`: `node0`

- Application machine running `nginx`: `node1`

</div>

</div>

---

# Run a simple benchmark test

<div class="columns">

<div>

```
wrk -t2 -c5 -d5s --timeout 2s http://node1/
```

Which means:

- `-t2`: Use two separate threads
- `-c5`: Open six connections (the first client is zero)
- `-d5s`: Run the test for five seconds
- `--timeout 2s`: Define a two-second timeout
- `--latency`: Print latency statistics  
- `http://node1/`: The target application is listening on `node1`
- Benchmark the `/` path of our application
  
</div>

<div>

![w:500](figures/wrk-architecture-structure.png)

</div>

</div>

---

# Sample output

```
Running 5s test @ http://node1/
  2 threads and 5 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   193.80us   54.14us   3.30ms   86.37%
    Req/Sec     9.91k   425.67    10.86k    72.55%
  Latency Distribution
     50%  175.00us
     75%  214.00us
     90%  257.00us
     99%  351.00us
  100509 requests in 5.10s, 43.03MB read
Requests/sec:  19707.66
Transfer/sec:      8.44MB
```
