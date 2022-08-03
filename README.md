# SSH Password-Based authentication to connect to the node from Master node


# Installation Ansible on Ubuntu 20.04.
 
   Syntax: $sudo apt update
 
   Syntax: $sudo apt install ansible -y
  

# Once installation done check the Ansible version

   Syntax: $ansible --version
 



# Installing sshpass  act as SSH authentication mechanism.
 
   Syntax: $sudo apt install sshpass
 


# Now, configure the ansible hosts inventory file which is come with default ansible inventory file.
 
   Syntax: $Sudo vim /etc/ansible/hosts
   
            [server]
            172.31.84.8 ansible_ssh_user=ec2-user    # IP of Host_node1 and user_name
            172.31.19.21 ansible_ssh_user=ec2-user   # IP of Host_node2 and user_name

 Once finish with this setup in host file
 
 
 # Now do make some changes inside /etc/ansible/ansible.cfg file
   
   Syntax: $sudo vim /etc/ansible/ansible.cfg
            #inventory /etc/ansible/hosts   # Remove commit 
 
 

# Now, List of inventories below syntax

    Syntax: $ansible-inventory --list -y
            all:
              children:
                server:
                  hosts:
                    172.31.84.8:
                      ansible_ssh_user: ec2-user
                    172.31.19.21 
                      ansible_ssh_user: ec2-user
                ungrouped: {}


# Now, Connect Password based SSH logging or Connection testing and need to append the option --ask-pass that means will make ansible prompt for the password of the host-node user. 

   Validity of SSH credentials (node user)

         Syntax: $ansible all -m ping --ask-pass
     SSH password:
             172.31.84.8 | SUCCESS => {
                 "ansible_facts": {
                     "discovered_interpreter_python": "/usr/bin/python"
                 },
                 "changed": false,
                 "ping": "pong"
             }
             172.31.19.21 | SUCCESS => {
                 "ansible_facts": {
                     "discovered_interpreter_python": "/usr/bin/python"
                 },
                 "changed": false,
                 "ping": "pong"
             }

Note: You must set the password for the user of the node server which will be the default user or you can create new one give them sudo privileged. 
 


# SSH with Passwordless Logging

# Create SSH Key-pair like Private and Public Key pair on the Ansible Master node.

   Syntax: $ssh-keygen -t rsa
 


# Copy the Public Key to my both Host-node machine (node1 and node2) below an example.
   
   Syntax: $sudo ssh-copy-id -i ~/.ssh/id_rsa.pub ec2-user1@172.31.19.21 #Host_node_1
  
   Syntax: $sudo ssh-copy-id -i ~/.ssh/id_rsa.pub ec2-user2@172.31.19.21 #Host_node_2
 
 Once triggered this command it will copy the content of id_rsa.pub key in user side inside the /home/user_name/.ssh/authorized_key file in the node server 



# Now, SSH testing to host-node without a password from Master node 
   
   Syntax: $ssh ec2-user@172.32.84.8
 


# This allow to control host-node without a password from Master-node side

    Syntax: $ansible -m ping all
             172.31.84.8 | SUCCESS => {
                 "ansible_facts": {
                     "discovered_interpreter_python": "/usr/bin/python"
                 },
                 "changed": false,
                 "ping": "pong"
             }
             172.31.19.21 | SUCCESS => {
                 "ansible_facts": {
                     "discovered_interpreter_python": "/usr/bin/python"
                 },
                 "changed": false,
                 "ping": "pong"
             }
   
 
 # Work with ansible-playbook defiend with variable to install httpd server
 
     Syntax: $vi vars.yml
              ---
              - hosts: demo
              user: ec2-user
              become: yes
              connection: ssh
              vars:
                      pkgname: httpd
              tasks:
                              - name: install HTTPD server on centos 7
                                action: yum name='{{pkgname}}' state=present

After setup the configuration and executed the vars.yml file to install httpd server for node server from master node below an output

    Syntax: $ansible-playbook vars.yml
             PLAY [demo] ********************************************************************

             TASK [Gathering Facts] *********************************************************
             ok: [172.31.20.162]

             TASK [install HTTPD server on centos 7] ****************************************
             changed: [172.31.20.162]

             PLAY RECAP *********************************************************************
             172.31.20.162              : ok=2    changed=1    unreachable=0    failed=0    skipped=0
             rescued=0    ignored=0

# Work with Handlers Section
  A handler is something that means same as a task, but it will run when called by another task
                                     or
  Hanlers are just like regular tasks in an ansible playbook, but are only run if the task contain a notify direction and also indicates that it change something.
  
    Syntax: $vi handlers.yml
             ---
             - hosts: demo
               user: ec2-user
               become: yes
               connection: ssh
               tasks:
                     - name: install httpd server on centos
                       action: yum name=httpd state=installed
                       notify: restart httpd
               handlers:
                       - name: restart httpd
                         action: service name=httpd state=restarted

-------First chech the code below the command------------------------------------------
   
      Syntax: $ansible-playbook handlers.yml --check # That means to check the bug or error within the code, but it will not execute the code
      
      
# Now run the handlers.yml file
      
      Syntax: $ansible-playbook handlers.yml
               PLAY [demo] ********************************************************************

               ASK [Gathering Facts] *********************************************************
               ok: [172.31.20.162]

               TASK [install httpd server on centos] ******************************************
               changed: [172.31.20.162]

               RUNNING HANDLER [restart httpd] ************************************************
               changed: [172.31.20.162]

               PLAY RECAP *********************************************************************
               172.31.20.162              : ok=3    changed=2    unreachable=0    failed=0    skipped=0
               rescued=0    ignored=0

   Now worked successfully the code and deploy httpp server on node-server side form master node

     
  
     
     
     
     
     
     
     
