# demonstration-repo

##########SSH Password-Based authentication to connect to the node from Master node#########

Step1. Install and Configure Ansible on Ubuntu 20.04.
 
 sudo apt update
 
 sudo apt install ansible -y
  
 check Ansible version
 

Installing sshpass  act as SSH authentication mechanism.
 
 sudo apt install sshpass
 

Step2. Now, configure the ansible hosts inventory file which is come with default ansible inventory file.
 
 Sudo vim /etc/ansible/hosts

Once finish with this setup in host file
 
List of inventories below command

ansible-inventory --list -y
 

Step3. Now, Connect Password based SSH logging or Connection testing and need to append the option --ask-pass that means will make ansible prompt for the password of the host-node user. 

•	Validity of SSH credentials (node user)

ansible all -m ping --ask-pass

Note: You must create a password for the user of the node server which will be the default user no need to create new one. 
 

#############SSH with Passwordless Logging################ 

Step1. Create SSH Key-pair like Private and Public Key pair on the Ansible Master node.

ssh-keygen -t rsa
 

Copy the Public Key to my both Host-node machine (node1 and node2) below an example.
   
   sudo ssh-copy-id -i ~/.ssh/id_rsa.pub ec2-user1@172.31.19.21 #Host_node_1
  
   sudo ssh-copy-id -i ~/.ssh/id_rsa.pub ec2-user2@172.31.19.21 #Host_node_2
 
 Note: Once triggered this command it will copy the content of id_rsa.pub key under the .ssh file for ec2-user of the node server side 


Step2. Now, SSH testing to host node from Master node
   
   ssh ec2-user@172.32.84.8
 

Step3. This allow to control host-node without a password from Master-node side

ansible -m ping all
 
 

                                                                             
