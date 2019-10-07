# Introduction to Command Line

A command line interface (CLI) is a means of interacting with a computer system where the user (or client) issues commands to the system in the form of successive lines of text (command lines).

---

## Table of Contents

*   [Motivation](#motivation)
*   [Environment](#environment)
*   [Basics](#basics)
*   [Navigation](#navigation)
*   [Pipes & Redirection](#pipes-&-redirection)
*   [Files](#files)
*   [Permissions](#permissions)
*   [System](#system)
*   [Summary](#summary)

---

## Motivation 

Although they may seem archaic, command line interfaces are extremely practical:

*   Almost all major organizations use *powerful remote systems* that are 100 times faster than your average personal computer.

    These remote systems almost never use a Graphical User Interface and can be operated solely via commands.

*   With the rise of Cloud Computing, Big Data, Deep Learning and Blockchain, the *command line workflow has proven to be the best*.

*   Apart from its demand in the industry, command line expertise brings with it a *holistic idea about the operating system*.

*   Command line also provides *fine-grained control over a system* and various methods to *automate boring tasks*.

Using the command line interface is very similar to solving a puzzle. With the right approach, anything is possible. You just need to know the right commands from a large toolbox.

---

## Environment

Over the course of this workshop, we will work in a Linux environment.

The workspaces are mounted on a Telnet server, at `172.16.22.5`

To connect to it:

*   Open a terminal and run the following command if you are on Linux, macOS or other Unix based system:

    ```bash
    telnet 172.16.22.5
    ```

*   If you are on a Windows system:
    *   Ensure that the Telnet service is enabled by navigating to `Control Panel` > `Programs and Features` > `Turn Windows features on or off` > Check `Telnet Client`
    *   Hit `Windows` + `R` and enter the following command:
    
    ```powershell
    telnet 172.16.22.5
    ```

If you have followed the above instructions, you would have successfully connected to the telnet server. Enter your credentials to access your workspace.

Once successfully authenticated, you should see the following prompt:

```
[username@linuxbpdc1 ~]$
```

---

## Basics

Use the `echo` command to print stuff

```bash
echo "Hello, world."
```

```bash
echo 'Single quotes also work'
```

You can also use the `printf` command to **print** _stuff_ **f**ormatted

```bash
printf "Hello\nWorld!"
```

---

Write single line comments with `#`

```bash
# Anything to the right of the # is ignored by the command line interface
```

---

The `man` command gives the **man**ual for different commands

```bash
man echo # This gives a manual about "echo" . Press 'q' to exit
```

---

Using `ls` we can look at the contents of a directory or **l**i**s**t it 

```bash
ls
```

You can format the output using flags. Flags are options which are set to false by default. If specified, they change the working of a command. You will be using this command a lot so let's look into it in a bit more detail.

The `-l` flag stands for **l**ong format

```bash
ls -l # displays permissions, owner, size, last modified date, file name and much more!
```

In linux files whose names start with `.` are hidden, you can list **a**ll files using the `-a` flag

```bash
ls -a # displays all files (including hidden ones)
```

The file sizes are shown in bytes by default. The `-h` flag prints sizes in **h**uman readable format

```bash
ls -h # Sizes automatically adjusted to Kilobytes, Megabytes & Gigabytes
```

To **R**ecursively list files in a directory (including files in subdirectories) use the `-R` flag

```bash
ls -R # ls -aR lists all the files in a directory!
```

To print **one** entry per line use `-1` flag

```bash
ls -1 # numeric digit one
```

---

## Navigation

When working with a GUI, we navigate across the filesystem using a file explorer:

*   File Explorer (Windows)
*   Finder (macOS)
*   Dolphin, Nautilus, Thunar and many others! (Linux)

The `pwd` command allows you to **p**rint **w**orking **d**irectory

```bash
pwd # If you ever get lost,`pwd` will tell you exactly where you are
```
​
You are currently in your `HOME` directory which is the equivalent of `Desktop` on PCs.

---

The root directory or sometimes just the root is the "highest" directory in the system. You can think of it as the start of a particular folder structure. All files and directories on a computer system have a unique path based on the root that describes their location:

*   An **absolute path** refers to the same location in a file system relative to the *root directory*
*   A **relative path** points to a specific location in a file system relative to the *working directory*

Some important shorthand notations: 

*   `.` refers to the working directory
*   `..` refers to the parent of working directory
*   `/` refers to the root directory
*   `~` refers to the home directory

---

The `cd` command allows you to **c**hange **d**irectory

```bash
cd .. # Changes working directory to its parent. You can confirm this using "pwd"
```

---

You can chain `..` to climb up to a directory that is an ancestor of the working directory

```bash
cd ../../.. # in this case, it takes you to the root directory
```

To return to your `HOME` directory, run *ONE* of the following:

*   ```bash
    cd # not specifying a path teleports you back home
    ```

*   ```bash
    cd $HOME # The $HOME variable stores the absolute path of your HOME directory
    ```

*   ```bash
    cd ~ # ~ = $HOME
    ```

Jump back to root and try all the above options.

```bash
cd / # jumps back to root, since "/" is the absolute path for root
```

---

## Pipes & Redirection

Two powerful features of the Linux command line shell are redirection and pipes which allow the output (or even input) of a program to be sent to a file or another program.

*   Pipes

    Pipes allow you to funnel the output from one command into another where it will be used as the input.

    The following command will list all the files, with details
    
    <!-- TODO: Explain more first -->
    ```bash
    ls -aR / | less
    ```

*   Redirection

    Redirection is similar to pipes except using files rather than another program. Here is a directory listing again but this time redirected to a file

    ```bash
    ls -al > listing.txt
    ```
    <!-- Add input redirection -->

---

## Files

Once you are back home, **m**a**k**e **dir**ectory to store files

```bash
mkdir session-1 # creates a directory named 'session-1' in the pwd
```

Move into this new directory

```bash
cd session-1
```

Now, create a file

```bash
touch myfile.txt # creates a file named 'myfile.txt'
```
<!-- Please explain finger command and other kinky commands friend -->

You can use `ls` command to look at the details of this file

A little about files:

*   _All_ files contain data <!-- Quiz: What about empty files? -->
*   Files are stored in the computer's _secondary memory_
*   The file's data is stored in the form of _bytes_

For text files:

*   The bytes that represent this data take values in a _particular range_.
*   This range is determined by the _encoding_ used, which may be [ASCII](https://en.wikipedia.org/wiki/ASCII), [UTF-8](https://en.wikipedia.org/wiki/UTF-8) etc.
*   When being rendered, _specific characters_ that match the bytes of these files are shown.
*   Sometimes there are bytes that do not make sense so they don't get rendered properly.

Most systems have in-built text editors such as `vim` or `nano`. Let's first try `nano` since it is more user-friendly

```bash
nano myfile.txt # opens 'myfile.txt' with nano
```

Type something in.

The text that is shown are not the exact contents of the file. 
This data is held by the `nano` editor as a buffer and is residing in the RAM of the system.
To save the contents of the file:

*   Hit `Ctrl` + `X` to write the contents of the buffer into the file
*   Hit `Y` to confirm and `Enter`
*   Nano now shows the name of the file it is about to write into. You can change this if you like. Hit `Enter` to finish.

Use the `cat` command to display the contents of the file

```bash
cat myfile.txt
```

Use the `head` command to display the first few lines of the file

```bash
head myfile.txt # head prints the first 10 lines by default
```

You can change the number of lines by providing a flag

```bash
head myfile.txt -n 5 # prints the first 5 lines
```

Similarly, you can display the last few lines with `tail`

```bash
tail myfile.txt -n 8 # prints the last 8 lines of the file
```

Create files with the following content:

```
# billy.txt
Billy is a cat
```

```
# tommy.txt
Tommy is a dog
```

To avoid a messy workspace it is a good idea to organize your files.

Create a directory for 'cats' and 'dogs'

You should have the following files and directories
```
billy.txt  cats  dogs  myfile.txt  tommy.txt
```

We can move files into specific directories using the **m**o**v**e command

*   ```bash
    mv a.txt dir/   # Moves file with the same name into a directory named dir
    ```

*   ```bash
    mv a.txt dir/b.txt # Moves file a.txt with the name b.txt into a directory named dir
    ```

*   ```bash
    mv a.txt b.txt # Renames a.txt to b.txt, essentially the command mv a.txt ./b.txt
    ```

Try _one_ of the following commands to **m**o**v**e 'billy.txt' into 'cats':

*   ```bash
    mv billy.txt cats/ # billy.txt is moved into the directory 'cats' with the same name
    ```
*   ```bash
    mv billy.txt cats/billy.txt # renames billy.txt as 'cats/billy.txt' and hence moves it into 'cats'
    ```

Similarly, move 'tommy.txt' into 'dogs'.

> **Note:**
>
> When `/` is not specified at the end of the name of a directory, it renames the source to the destination instead of moving it inside.
> ```bash
> mv billy.txt cats # renames billy.txt to cats.
> ```
> In this case the `cats` directory is unchanged but `billy.txt` is renamed to `cats`.

To better visualize the contents of `pwd` use the `tree` command

```bash
tree # displays the names of files and directories in the pwd in a recursive manner
```

We can use the `cp` command to **c**o**p**y a file:

```bash
cp myfile.txt yourfile.txt # makes a copy of 'myfile.txt' and calls it 'yourfile.txt'
```

Copy `billy.txt` and `tommy.txt` into `pwd`

```bash
cp cats/billy.txt ./
cp dogs/tommy.txt ./
```

We can scale these operations to affect multiple files 

```bash
mkdir textfiles
mv *.txt textfiles/ # This moves all files that have '.txt' as their extension into the directory 'textfiles'
```

---

To copy files involving remote machines, we use the command `scp`

To copy file sample.txt from local machine to a remote machine

```bash
scp sample.txt username@remotemachine.com:/path-to-directory
```

To copy file sample.txt from a remote machine to a local machine

```bash
scp username@remotemachine.com:/path-to-source-file /path-to-destination-directory
```

To copy entire folders, use the recursive argument `-r`

---

## Permissions

Everything on a system has permissions attached with it.
Since files, directories & programs all have permissions of their own, there is a very elaborate permission mechanism.

View the details of the contents in the `pwd`

```bash
ls -al
```

You should see the following characters next to each entity in the directory

```
drwxr-xr-x
```

These characters represent the permissions for a particular entity:

*   The first character describes the type of entity
    *   **_-_** for a regular file
    *   **_d_** for **d**irectory
    *   **_b_** for **b**lock special file, disk or partition devices
    *   **_c_** for **c**haracter special file (see /dev for examples)
    *   **_l_** symbolic link
    *   Others: **_p_**, **_s_**, **_D_** see [unix file types](https://en.wikipedia.org/wiki/Unix_file_types) for details.
*   The next 9 characters are in fact 3 groups of characters that represent permissions for different users
    *   The *first 3* show the permissions for the **owner** of the file
    *   The *second 3* show the permissions for the **group** associated with that file
    *   The *last 3* show the permissions for the **rest** of the users
*   Each group of 3 characters represents the 3 major permissions
    *   ***r*** for **read** and is equivalent to *4*
    *   ***w*** for **write** and is equivalent to *2*
    *   ***x*** for **execute** and is equivalent to *1*

A permission of *5* allows only *read* and *execute* (4 + 1 = 5).

File permissions can be changed by:

*   The owner
*   `root` i.e. any superuser

Use the `chmod` command to change permissions

```bash
chmod 777 cats # allows anyone (owner, group and rest) to do anything (read, write and execute) to 'cats'
```

The `chown` command can be used to change the ownership of a file but can only be called by `root`

## System

You will generally ssh into different machines and it is a good idea to look at the sytem specifications before executing any commands.

You can use the `uname` command to display the basic software information like kernel name, version, hostname, release, architecture etc

```bash
uname -a # argument -a stands for list all
```

You can get the basic hardware, information use the command

```bash
sudo lshw # sudo permission is required to run this command
```

To get specific detailed hardware information, use the commands like

```bash
sudo lscpu # for cpu details
```

```bash
sudo lsusb # for connected usb devices
```

```bash
sudo lspci # for connected pci devices
```

---

## Miscellaneous


Use the `wc` command to count display:

*   The number of lines
*   The number of words
*   The number of characters

```bash
wc myfile.txt
```

You can use flags to limit the output to what you need

```bash
wc myfile.txt -l # shows the number of lines for 'myfile.txt'
```

Use the `grep` command to search for specific characters in a file

```bash
grep "cat" myfile.txt # shows the lines which have 'cat'
```

An import feature of the Bash shell is the pipe system. 
It enables the output of one command to be used as the input for another.
We can combine the two commands

```bash
grep "cat" myfile.txt | wc -l # shows the number of lines that have the word 'cat'
```

The `history` command shows your command history

```bash
history
```

Try to search for a particular command in your history

```
history | grep "cd"
```

---

## Summary